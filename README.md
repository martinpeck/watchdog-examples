# Watchdog Examples

Some examples of using the package `watchdog` to watch for file system changes.

You can see more information about Watchdog here:

- PyPI: <https://pypi.org/project/watchdog/>
- Docs: <https://pythonhosted.org/watchdog/>

## Setup

1. Make sure you're using Python 3.6 or better (I'm using 3.7.0)
2. Create a virtual environment using `python3 -m venv venv`
3. Activate that virtual environment with `source venv\bin\activate`
4. Update pip with `pip install --upgrade pip`
5. Install packages with `pip install -r requirements.txt`

## Examples

### watch_and_log.py

This example takes a single argument, and then uses a logger to report of file system events.

Run this example with the following command:

``` bash
python watch_and_log.py ./test-folder/
```

When you do this, and then create files in the `test-folder`, you'll see logging similar to the following:

```
2018-12-22 19:48:47 - Created file: ./test-folder/cheese.txt
2018-12-22 19:48:47 - Modified directory: ./test-folder
2018-12-22 19:48:47 - Modified file: ./test-folder/cheese.txt
```

### image_watcher.py

This example subclasses `PatternMatchingEventHandler` and then watches for the creation of images (files with a `*.png` or `*.jpg` file pattern)

Run this example with the following command:

``` bash
python image_watcher.py 
```

You can then try creating images within  `test-folder`. #

- If you create a file with a png or jpg extension you'll see this reported in the console,
- If you create any other type of file, you won't see anything reported.
- If you delete or modify an image file, you won't see anything reported.
