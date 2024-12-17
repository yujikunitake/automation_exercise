from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

from utils.webdriver_setup import WebDriverSetup

from data.user_data import USER_DATA


@pytest.fixture
def driver():
    driver = WebDriverSetup("chrome").start_driver()
    yield driver
    driver.quit()

def test_register_user(driver: webdriver.Chrome):
    URL = "https://www.automationexercise.com/"
    home_page = HomePage(driver)

    """
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    """
    home_page.navigate(URL)


    """
    # 3. Verify that home page is visible successfully
    """
    assert "Automation Exercise" in driver.title, "Home page didn't load correctly."


    """
    # 4. Click on 'Signup / Login' button
    """
    home_page.click_signup_button()


    """
    # 5. Verify 'New User Signup!' is visible
    """
    login_page = LoginPage(driver)

    signup_h2 = login_page.verify_signup_h2()
    assert signup_h2 == "New User Signup!", "'New User Signup!' is not visible."


    """
    # 6. Enter name and email address
    """
    login_page.input_signup_name(USER_DATA['name'])
    login_page.input_signup_email(USER_DATA['email'])


    """
    # 7. Click 'Signup' button
    """
    login_page.submit_signup()


    """
    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    """
    signup_page = SignupPage(driver)

    enter_account_info = signup_page.enter_account_info_h2()
    assert enter_account_info == "ENTER ACCOUNT INFORMATION", "'ENTER ACCOUNT INFORMATION' is not visible."


    """
    # 9. Fill details: Title, Name, Email, Password, Date of birth
    """
    # Title
    title_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, f"id_gender{USER_DATA['title']}"))).click()

    # Name
    actions = ActionChains(driver)

    name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
    name_input.click()
    actions.key_down(Keys.CONTROL).key_down('A').key_up(Keys.CONTROL).key_up('A').perform()
    name_input.send_keys(USER_DATA["name"])

    # Password
    password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
    password_input.click()
    password_input.send_keys(USER_DATA["password"])

    # Date of Birth
    day, month, year = USER_DATA["birth_date"].split("/")

    day_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "days")))
    select_from_day = Select(day_select)
    select_from_day.select_by_value(day.lstrip("0"))

    month_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "months")))
    select_from_month = Select(month_select)
    select_from_month.select_by_value(month.lstrip("0"))

    year_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "years")))
    select_from_year = Select(year_select)
    select_from_year.select_by_value(year)

    """
    # 10. Select checkbox 'Sign up for our newsletter!'
    """
    newsletter_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "newsletter"))).click()

    """
    # 11. Select checkbox 'Receive special offers from our partners!'
    """
    receivbe_offers_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "optin"))).click()

    """
    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    """
    name_parts = USER_DATA["name"].split()

    # First name
    first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "first_name"))).send_keys(name_parts[0])

    # Last name
    last_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "last_name"))).send_keys(name_parts[-1])

    # Company
    company = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "company"))).send_keys(USER_DATA["company"])

    # Address
    address1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "address1"))).send_keys(USER_DATA["address1"])

    # Address2
    address2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "address2"))).send_keys(USER_DATA["address2"])

    # Country
    country = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "country")))
    select_from_country = Select(country)
    select_from_country.select_by_value(USER_DATA["country"])

    # State
    state = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "state"))).send_keys(USER_DATA["state"])

    # City
    city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "city"))).send_keys(USER_DATA["city"])

    # Zipcode
    zipcode = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "zipcode"))).send_keys(USER_DATA["zipcode"])

    # Mobile Number
    mobile_number = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "mobile_number"))).send_keys(USER_DATA["phone"])

    """
    # 13. Click 'Create Account button'
    """
    create_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='create-account']"))).click()

    """
    # 14. Verify that 'ACCOUNT CREATED!' is visible
    """
    account_created = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[data-qa='account-created']"))).text
    assert account_created == "ACCOUNT CREATED!", "'ACCOUNT CREATED' is not visible."

    """
    # 15. Click 'Continue' button
    """
    continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']"))).click()

    """
    # 16. Verify that 'Logged in as username' is visible
    """
    logged_in_as = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a"))).text
    assert logged_in_as == f"Logged in as {USER_DATA['name']}", f"'Logged in as {USER_DATA['name']}' is not visible."

    """
    # 17. Click 'Delete Account' button
    """
    delete_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/div/div/div/div[2]/div/ul/li[5]/a"))).click()

    """
    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    """
    # ACCOUNT DELETED!
    account_deleted = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[data-qa='account-deleted']"))).text
    assert account_deleted == "ACCOUNT DELETED!", "'ACCOUNT DELETED!' is not visible"

    # Continue
    continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']"))).click()
