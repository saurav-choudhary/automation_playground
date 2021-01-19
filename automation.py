from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_browser = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.implicitly_wait(5)

assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title
ad_button = chrome_browser.find_element_by_id('at-cv-lightbox-close')
ad_button.click()
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I\'m a selenium NOOB')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert "I'm a selenium NOOB" in output_message.text

# chrome_browser.close()
chrome_browser.quit()
