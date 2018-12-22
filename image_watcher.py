import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class ImageCreationHandler(PatternMatchingEventHandler):
	
	def __init__(self):
		patterns = ['*.png', '*.jpg']
		ignore_patterns = None
		
		super().__init__(patterns,
						None,
						ignore_directories = True,
						case_sensitive = False)
	
	def on_created(self, event):
		print("File created!")
		print(event)
		
		
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
