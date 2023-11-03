from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".cpp"):
            return
        new_file = os.path.basename(event.src_path)
        os.system(f"python3 automate.py {new_file}")

if __name__ == "__main__":
    path_to_watch = "Path to your cpp working repository"
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
