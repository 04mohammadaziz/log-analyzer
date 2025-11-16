def parse_auth_log_line(line: str) -> dict:
    return {}

if __name__ == "__main__":
    log_path = "data/auth.log"

    with open(log_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            print(line)