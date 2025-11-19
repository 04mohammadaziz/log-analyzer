import re
import json
import csv

pattern = r'([A-Za-z]{3}\s\d{1,2}\s\d+:\d+:\d+)\s[A-Za-z0-9_-]+\ssshd\[\d+\]:\s([A-Za-z]+\s[A-Za-z]+)\sfor\s(?:invalid user\s)?([A-Za-z0-9_]+)\sfrom\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

events = []

with open('test_auth.log', 'r') as file:
    #content = file.read() loads whole file into memory
    for line in file: #streaming line by line is best practice due to the shear size of raw log data in the real world
        match = re.search(pattern, line)
        if match:
            timestamp = match.group(1)
            status = match.group(2)
            username = match.group(3)
            ip = match.group(4)


            event = {
                'timestamp': timestamp,
                'status': status,
                'username': username,
                'ip': ip
            }

            events.append(event)

            #for event in events:
                #print(event)

            #print(timestamp, status, username, ip)

'''
filename = 'events.json' #importing data to json file

with open(filename, 'w') as json_file:
    json.dump(events, json_file, indent=4)

print(f"Saved to {filename}")

filename = 'events.csv'

fieldnames = ['timestamp', 'status', 'username', 'ip']

with open(filename, 'w', newline = '') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for event in events:
        writer.writerow(event)
'''
count = len(events)

fail_counter = 0
success_counter = 0

usernameSet = set()
ipsSet = set()
failures_by_ip = {}

for event in events:
    if event['status'] == 'Failed password':
        fail_counter += 1
    else:
        success_counter += 1
    usernameSet.add(event["username"])
    ipsSet.add(event["ip"])

    if event['ip'] not in failures_by_ip:
        failures_by_ip[ip] = 0
    failures_by_ip[ip] += 1

usernameList = list(usernameSet)
ipsList = list(ipsSet)

print(
    f'Total events: {count}', 
      f'Failed attempts: {fail_counter}', 
      f'Successful logins: {success_counter}', 
      f'Unique usernames: {usernameList}', 
      f"Unique IPs: {ipsSet}", 
      f"{failures_by_ip}", sep='\n'
      )