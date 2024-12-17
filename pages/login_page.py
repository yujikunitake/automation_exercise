from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def verify_signup_h2(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='signup-form'] h2"))).text
    
    def input_signup_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-qa='signup-name']"))).send_keys(name)

    def input_signup_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-qa='signup-email']"))).send_keys(email)

    def submit_signup(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='signup-button']"))).click()
