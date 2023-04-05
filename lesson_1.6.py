import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://suninjuly.github.io/registration2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.XPATH, "//div/label[text()='First name*']/../input")
    first_name.send_keys('Ivan')
    last_name = browser.find_element(By.XPATH, "//div/label[text()='Last name*']/../input")
    last_name.send_keys('Petrov')
    email = browser.find_element(By.XPATH, "//div/label[text()='Email*']/../input")
    email.send_keys('ivan_petrov@email.div')
    try:
        phone = browser.find_element(By.XPATH, "//div/label[text()='Phone:']/../input")
        phone.send_keys('35353464634')
    except NoSuchElementException:
        print('No Phone field')
    try:
        address = browser.find_element(By.XPATH, "//div/label[text()='Address:']/../input")
        address.send_keys('Star City')
    except NoSuchElementException:
        print('No address field')
    submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
