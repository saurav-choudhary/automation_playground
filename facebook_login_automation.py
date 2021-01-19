from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import sys

username = sys.argv[1]
passwd = sys.argv[2]
text = sys.argv[3]

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\saura\AppData\Local\Google\Chrome\User Data")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_browser = webdriver.Chrome(options=options, executable_path=f'chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.facebook.com/')

time.sleep(2)

assert 'Log In' in chrome_browser.page_source

username_input = chrome_browser.find_element_by_id('email')
username_input.clear()
username_input.send_keys(username)

password_input = chrome_browser.find_element_by_id('pass')
password_input.clear()
password_input.send_keys(passwd)

time.sleep(2)
login_button = chrome_browser.find_element_by_id('u_0_f')
login_button.click()
time.sleep(2)
chrome_browser.find_element_by_class_name('sx_2a82c1').click()
time.sleep(2)
chrome_browser.find_element_by_class_name('sx_fe5422').click()
time.sleep(2)
action = ActionChains(chrome_browser)
action.send_keys(f'Selenium automation testing. This is an automated post. {text}')
action.send_keys(Keys.TAB * 10)
action.send_keys(Keys.ENTER)
action.perform()

# time.sleep(20)
# chrome_browser.quit()
