import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"D:/Selenium"

driver = webdriver.Chrome()
driver.get(
    "https://the-internet.herokuapp.com/add_remove_elements/")

# btn = driver.find_element(By.TAG_NAME, "button")

# dev tools -> right click item -> copy -> full xpath
# btn = driver.find_element_by_tag_name("button")
# for x in range(5):

driver.implicitly_wait(10)
btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
btn.click()
btn2 = driver.find_element(By.ID, "njdwd")

# css Selector
# ----- find tags like button or h or p and then reference by list -> button[]
# and enter your filtration -> button[filter_criteria='']
# currency_element = driver.find_element(By.CSS_SELECTOR, "button[data-tooltip-text='Choose your currency']")
# another example: we can use *= for substring filtering, beginning or ending with also possible...
# currency = driver.find_element(By.CSS_SELECTOR, 'a[data-modal-header-and-so-on*="selected_currency=USD"]')
#1111111111111111111111111112222222222222222222222222222222
#molfjefwef
# rgrg