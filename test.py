import re

pattern = r'([A-Za-z]{3}\s\d{1,2}\s\d+:\d+:\d+)\s[A-Za-z0-9_-]+\ssshd\[\d+\]:\s([A-Za-z]+\s[A-Za-z]+)\sfor\s(?:invalid user\s)?([A-Za-z0-9_]+)\sfrom\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

with open('test_auth.log', 'r') as file:
    #content = file.read() loads whole file into memory
    for line in file: #streaming line by line is best practice due to the shear size of raw log data in the real world
        match = re.search(pattern, line)
        if match:
            timestamp = match.group(1)
            status = match.group(2)
            username = match.group(3)
            ip = match.group(4)

            print(timestamp, status, username, ip)

