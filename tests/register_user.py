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
from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage

from utils.name_split import name_split
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
    assert login_page.verify_signup_h2() == "New User Signup!", "'New User Signup!' is not visible."


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
    assert signup_page.verify_enter_account_info() == "ENTER ACCOUNT INFORMATION", "'ENTER ACCOUNT INFORMATION' is not visible."


    """
    # 9. Fill details: Title, Name, Email, Password, Date of birth
    """
    # Title
    signup_page.select_radio_title(USER_DATA['title'])

    # Password
    signup_page.input_password(USER_DATA['password'])

    # Date of Birth
    signup_page.select_birth_day(USER_DATA['birth_day'])
    signup_page.select_birth_month(USER_DATA['birth_month'])
    signup_page.select_birth_year(USER_DATA['birth_year'])


    """
    # 10. Select checkbox 'Sign up for our newsletter!'
    """
    signup_page.select_checkbox_newsletter()


    """
    # 11. Select checkbox 'Receive special offers from our partners!'
    """
    signup_page.select_checkbox_offers()


    """
    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    """
    first_name, last_name = name_split(USER_DATA['name'])

    # First name
    signup_page.input_first_name(first_name)

    # Last name
    signup_page.input_last_name(last_name)

    # Company
    signup_page.input_company(USER_DATA['company'])

    # Address1
    signup_page.input_address1(USER_DATA['address1'])

    # Address2
    signup_page.input_address2(USER_DATA['address2'])

    # Country
    signup_page.select_country(USER_DATA['country'])

    # State
    signup_page.input_state(USER_DATA['state'])

    # City
    signup_page.input_city(USER_DATA['city'])

    # Zipcode
    signup_page.input_zipcode(USER_DATA['zipcode'])

    # Mobile Number
    signup_page.input_mobile_number(USER_DATA['mobile_number'])


    """
    # 13. Click 'Create Account button'
    """
    signup_page.submit()


    """
    # 14. Verify that 'ACCOUNT CREATED!' is visible
    """
    account_created_page = AccountCreatedPage(driver)
    assert account_created_page.verify_account_created() == "ACCOUNT CREATED!", "'ACCOUNT CREATED' is not visible."


    """
    # 15. Click 'Continue' button
    """
    account_created_page.click_continue_button()


    """
    # 16. Verify that 'Logged in as username' is visible
    """
    assert home_page.verify_logged_in_as() == f"Logged in as {USER_DATA['name']}", f"'Logged in as {USER_DATA['name']}' is not visible."


    """
    # 17. Click 'Delete Account' button
    """
    home_page.click_delete_account_button()


    """
    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    """
    delete_account_page = DeleteAccountPage(driver)
    # ACCOUNT DELETED!
    assert delete_account_page.verify_account_deleted() == "ACCOUNT DELETED!", "'ACCOUNT DELETED!' is not visible"

    # Continue
    delete_account_page.click_continue_button()
