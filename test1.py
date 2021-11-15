from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="D:/0 - Everything/1 - My work space/2 - Coding\Professional/3 - Amitava Sir/Python/Pyhton special start up project/google search automation/chromedriver.exe")
driver.set_page_load_timeout("10")
driver.get("https://www.google.com")
driver.maximize_window()
q1=driver.find_element_by_name("q")
q1.send_keys("Modi India")
time.sleep(2)
q1.send_keys(Keys.RETURN)

