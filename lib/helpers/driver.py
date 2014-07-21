#
# HamperDriver is a wrapper around the Selenium WebDriver class, adding HamperSingleton
# as a metaclass to provide singleton functionality to the WebDriver.
# 
# We wanted to have one browser window handle the whole process (certain tokens are passed to/from form submission
# which makes it a pain to have multiple browser windows handle the process)
#

from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
import singleton

class HamperDriver(Chrome):
	__metaclass__ = singleton.HamperSingleton

	def __init__(self):
		super(HamperDriver, self).__init__()
