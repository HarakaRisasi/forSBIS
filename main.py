######################################################
#ChromeDriver - это отдельный исполняемый файл, который Selenium WebDriver использует для управления Chrome. 
# Он поддерживается командой Chromium с помощью участников WebDriver.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path="AC:/Drivers/chromedriver")
# Optional argument, if not specified will search path.
######################################################