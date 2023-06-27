from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import names
from time import sleep

url = "https://www.guidetogwinnett.com/georgia/lilburn/sports-recreation/team-mongoose-bjj"

for _ in range(400):
    name = names.get_full_name()
    strip_name = name.lower().replace(" ", "_")
    driver = webdriver.Firefox()
    driver.get(url)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="vote-4109-156"]'))
    )
    element.click()
    alert = Alert(driver)
    alert.send_keys(f"{strip_name}@gmail.com")
    alert.accept()
    sleep(2)
    driver.close()
