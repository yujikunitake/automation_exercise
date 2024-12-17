from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage():
    def __init__(self, driver):
        self.driver = driver

    def verify_enter_account_info(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='login-form'] h2 b"))).text
    
    def select_radio_title(self, title_id_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, f"id_gender{title_id_number}")))
