import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hasher import calculate_hash
from database import get_all_records

class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            new_hash = calculate_hash(event.src_path)
            print(f"[MODIFIED] {event.src_path}")
            print(f"New Hash: {new_hash}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"[NEW FILE] {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[DELETED] {event.src_path}")

def start_monitor(directory):
    observer = Observer()
    observer.schedule(MonitorHandler(), directory, recursive=True)
    observer.start()

    print(f"[MONITORING STARTED] {directory}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
