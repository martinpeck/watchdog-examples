import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class ImageCreationHandler(PatternMatchingEventHandler):
	
	def __init__(self):		
		super().__init__(['*.png', '*.jpg'],
						None,
						ignore_directories = True,
						case_sensitive = False)
	
	def on_created(self, event):
		print("New image detected:")
		print(f"  src_path  : {event.src_path}")
		print(f"  event_type: {event.event_type}")
		
if __name__ == "__main__":
	observer = Observer()
	observer.schedule(ImageCreationHandler(), path='./test-folder')
	observer.start()
	
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	
	observer.join()		
