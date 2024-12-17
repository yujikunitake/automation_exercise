from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeleteAccountPage():
    def __init__(self, driver):
        self.driver = driver

    def verify_account_deleted(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-deleted']"))).text

    def click_continue_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']"))).click()
