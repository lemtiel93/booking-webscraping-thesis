from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument("--enable-cookies")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

