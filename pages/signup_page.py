from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SignupPage():
    def __init__(self, driver):
        self.driver = driver

    def verify_enter_account_info(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='login-form'] h2 b"))).text
    
    def select_radio_title(self, title_id_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, f"id_gender{title_id_number}"))).click()

    def input_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(password)

    def select_birth_day(self, birth_day):
        Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "days")))).select_by_value(birth_day)
    
    def select_birth_month(self, birth_month):
        Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "months")))).select_by_value(birth_month)

    def select_birth_year(self, birth_year):
        Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "years")))).select_by_value(birth_year)

    def select_checkbox_newsletter(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "newsletter"))).click()

    def select_checkbox_offers(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "optin0"))).click()

    def input_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "first_name"))).send_keys(first_name)

    def input_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "last_name"))).send_keys(last_name)

    def input_company(self, company):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "company"))).send_keys(company)

    def input_address1(self, address1):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "address1"))).send_keys(address1)

    def input_address2(self, address2):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "address2"))).send_keys(address2)

    def select_country(self, country):
        Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "country")))).select_by_value(country)

    def input_state(self, state):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "state"))).send_keys(state)

    def input_city(self, city):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "city"))).send_keys(city)

    def input_zipcode(self, zipcode):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "zipcode"))).send_keys(zipcode)

    def input_mobile_number(self, mobile_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "mobile_number"))).send_keys(mobile_number)

    def submit(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='create-account']"))).click()

    