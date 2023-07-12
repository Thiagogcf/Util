from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path_to_webdriver = "/path/to/webdriver"

login_url = "https://www.example.com/login"

driver = webdriver.Chrome(path_to_webdriver)

driver.get(login_url)

username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")

username_field.send_keys("thithithi")
password_field.send_keys("AgoAgoAgo")

password_field.send_keys(Keys.RETURN)
