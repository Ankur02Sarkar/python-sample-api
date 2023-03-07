from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess

class RestartHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'modified' and event.src_path.endswith('.py'):
            print(f'Restarting server...')
            os.system('pkill -f api.py')
            subprocess.Popen(['python', 'api.py'])

observer = Observer()
observer.schedule(RestartHandler(), '.', recursive=True)
observer.start()

print(f'Server started. Watching for changes...')

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
