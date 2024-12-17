from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

URL = "https://www.automationexercise.com/"
NAME = "Clifford Lee Burton"
EMAIL = "pullingtheeth@metallica.com"
TITLE = "1"
PASSWORD = "Roberto23Agustín10Miguel1964SantiagoSamuelTrujilloVeracruz!"
BIRTH_DATE = "10/02/1962"
COMPANY = "Metallica"
ADDRESS1 = "Metal Land"
ADDRESS2 = "666"
COUNTRY = "United States"
STATE = "California"
CITY = "Castro Valley"
ZIPCODE = "94541"
PHONE = "+1 (951) 239-0523"

"""
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
"""
driver = webdriver.Chrome()
driver.get(URL)


"""
# 3. Verify that home page is visible successfully
"""
title = "Automation Exercise"
actual_title = driver.title

if title == actual_title:
    print("Page sucessfuly loaded!")
else:
    print(f"The actual page title is {actual_title}, expected {title}.")


"""
# 4. Click on 'Signup / Login' button
"""
signup_login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()


"""
# 5. Verify 'New User Signup!' is visible
"""
signup_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='signup-form'] h2"))).text

if signup_form == "New User Signup!":
    print("'New User Signup!' is visible.")
else:
    print("'New User Signup!' is not visible.")


"""
# 6. Enter name and email address
"""
name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-qa='signup-name']"))).send_keys(NAME)

email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-qa='signup-email']"))).send_keys(EMAIL)


"""
# 7. Click 'Signup' button
"""
signup_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='signup-button']"))).click()


"""
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
"""
enter_account_information = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='login-form'] h2 b"))).text

if enter_account_information == "ENTER ACCOUNT INFORMATION":
    print("ENTER ACCOUNT INFORMATION is visible.")
else:
    print("ENTER ACCOUNT INFORMATION is not visible.")


"""
# 9. Fill details: Title, Name, Email, Password, Date of birth
"""
# Title
title_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, f"id_gender{TITLE}"))).click()

# Name
actions = ActionChains(driver)

name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
name_input.click()
actions.key_down(Keys.CONTROL).key_down('A').key_up(Keys.CONTROL).key_up('A').perform()
name_input.send_keys(NAME)

# Password
password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
password_input.click()
password_input.send_keys(PASSWORD)

# Date of Birth
day, month, year = BIRTH_DATE.split("/")

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
name_parts = NAME.split()

# First name
first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "first_name"))).send_keys(name_parts[0])

# Last name
last_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "last_name"))).send_keys(name_parts[-1])

# Company
company = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "company"))).send_keys(COMPANY)

# Address
address1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "address1"))).send_keys(ADDRESS1)

# Address2
address2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "address2"))).send_keys(ADDRESS2)

# Country
country = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "country")))
select_from_country = Select(country)
select_from_country.select_by_value(COUNTRY)

# State
state = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "state"))).send_keys(STATE)

# City
city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "city"))).send_keys(CITY)

# Zipcode
zipcode = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "zipcode"))).send_keys(ZIPCODE)

# Mobile Number
mobile_number = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "mobile_number"))).send_keys(PHONE)

"""
# 13. Click 'Create Account button'
"""
create_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='create-account']"))).click()

"""
# 14. Verify that 'ACCOUNT CREATED!' is visible
"""
account_created = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[data-qa='account-created']"))).text

if account_created == "ACCOUNT CREATED!":
    print("'ACCOUNT CREATED!' is visible.")
else:
    print("'ACCOUNT CREATED!' is not visible.")

"""
# 15. Click 'Continue' button
"""
continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']"))).click()

"""
# 16. Verify that 'Logged in as username' is visible
"""
logged_in_as = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a"))).text

if logged_in_as  == f"Logged in as {NAME}":
    print(f"'Logged in as username' is visible.")
else:
    print(f"'Logged in as username' is not visible.")

"""
# 17. Click 'Delete Account' button
"""
delete_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/div/div/div/div[2]/div/ul/li[5]/a"))).click()

"""
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
"""
# ACCOUNT DELETED!
account_deleted = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[data-qa='account-deleted']"))).text

if account_deleted == "ACCOUNT DELETED!":
    print("'ACCOUNT DELETED!' is visible")
else:
    print("'ACCOUNT DELETED!' is visible")

# Continue
continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='continue-button']"))).click()
