import argparse
import os
import shutil
import tempfile
import time
import requests
import uuid
from PIL import Image
from selenium.common.exceptions import JavascriptException

_dir = tempfile.mkdtemp()
_execution_id = None
api_key="b5bd77ef-4da5-498e-92df-7d8cd2c9b355" #TODO PARAMETRIZE
def _upload_image(image):
    global _execution_id
    url = "https://us-central1-lince-232621.cloudfunctions.net/process_image-dev"
    files = {'file': open(image, 'rb')}
    r = requests.post(url, files=files, data={'execution_id': _execution_id})
    print(r)
    print(r.json())
    if not _execution_id:
        _execution_id = r.json()


def capture_screen(driver, title=None):
    """

    :param driver: Selenium driver used in automation.
    :param title: title to set the image. If none is specified, it will retrieve the websites title.
    :param duplicate_header: if there are floating headers, this will force it to absolute position.
    :return: Returns the final title of the image.
    """
    global _dir
    if not title:
        title = driver.title
    save_path = os.path.join(_dir, title)
    name, ext = os.path.splitext(save_path)
    if not ext or ext.lower() != 'png':
        save_path = save_path + ".png"
    _fullpage_screenshot(driver, save_path)
    
    _upload_image(save_path)
    # _upload_image("C:/Users/Potosin/Desktop/test_images/Capture2.png")
    print("Uploaded image {}\n".format(save_path))
    return title


def _fullpage_screenshot(driver, file):
    # Method pulled from github post https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver
    print("Starting chrome full page screenshot workaround ...")

    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    viewport_width = driver.execute_script("return document.body.clientWidth")
    viewport_height = driver.execute_script("return window.innerHeight")
    print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height, viewport_width, viewport_height))
    rectangles = []

    # Pad verticall scroll to deal with floating headers
    scroll_pad=200

    i = 0
    while i < total_height:
        ii = 0
        top_height = i + viewport_height

        if top_height > total_height:
            top_height = total_height

        while ii < total_width:
            top_width = ii + viewport_width

            if top_width > total_width:
                top_width = total_width

            print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
            rectangles.append((ii, i, top_width, top_height))

            ii = ii + viewport_width

        i = i + viewport_height - scroll_pad

    stitched_image = Image.new('RGB', (total_width, total_height - scroll_pad))
    previous = None
    part = 0

    for rectangle in rectangles:
        if not previous is None:
            try:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            except JavascriptException:
                driver.execute_script("document.body.scrollTop = 0;") #TODO implement logic for apptim similar website.
            print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
            time.sleep(0.2)

        file_name = "part_{0}.png".format(part)
        print("Capturing {0} ...".format(file_name))

        driver.get_screenshot_as_file(file_name)
        screenshot = Image.open(file_name)

        if rectangle[1] + viewport_height > total_height:
            offset = (rectangle[0], total_height - viewport_height)
        else:
            # We know that the first time the image was not cropped, we don't modify the offset.
            offset = (rectangle[0], rectangle[1]+scroll_pad if rectangle[1]>0 else 0)

        print("Adding to stitched image with offset ({0}, {1})".format(offset[0], offset[1]))
        if offset[1] > 0:
            w, h = screenshot.size
            screenshot = screenshot.crop((0, scroll_pad, w, h))
        stitched_image.paste(screenshot, offset)

        del screenshot
        os.remove(file_name)
        part = part + 1
        previous = rectangle

    stitched_image.save(file)
    print("Finishing chrome full page screenshot workaround...")
    return True


def dispose():
    """
    Makes sure to remove any temporary files created during execution.
    :return:
    """
    global _execution_id
    shutil.rmtree(_dir)
    print("To view a detailed report of the execution please navigate to http://127.0.0.1:5502/da"
          "shboard/src/results.html?id={}".format(_execution_id))