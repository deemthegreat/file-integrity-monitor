import os
import sys
from hasher import calculate_hash
from database import initialize_db, insert_record
from monitor import start_monitor

def create_baseline(directory):
    initialize_db()
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(path):
                size = os.path.getsize(path)
                modified = os.path.getmtime(path)
                checksum = calculate_hash(path)
                if checksum:
                    insert_record(path, size, checksum, modified)
                    print(f"[BASELINE CREATED] {path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 fim.py baseline <directory>")
        print("  python3 fim.py monitor <directory>")
        sys.exit(1)

    command = sys.argv[1].lower()
    directory = sys.argv[2]

    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        sys.exit(1)

    if command == "baseline":
        create_baseline(directory)
    elif command == "monitor":
        start_monitor(directory)
    else:
        print(f"Unknown command: {command}")
        print("Commands supported: baseline, monitor")
