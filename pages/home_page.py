from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    def navigate(self, url):
        self.driver.get(url)

    def click_signup_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()

    def verify_logged_in_as(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a"))).text
    
    def click_delete_account_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/div/div/div/div[2]/div/ul/li[5]/a"))).click()

    