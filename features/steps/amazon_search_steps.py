from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://wwww.amazon.com/')

@when('Search for table')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then('Verify search result is correct')
def verify_search_result(context):
    expected_result = '"table"'
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

@when('Click Orders')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify sign in page opened')
def verify_search_result(context):
    expected_sign_in_header = 'Sign in'
    actual_sign_in_header = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    assert expected_sign_in_header == actual_sign_in_header, f'Error, expected {expected_sign_in_header} did not match actual {actual_sign_in_header}'

    expected_email_input_field = context.driver.find_element(By.CSS_SELECTOR, '#ap_email')
    actual_email_input_field = context.driver.find_element(By.CSS_SELECTOR, '#ap_email')
    assert expected_email_input_field == actual_email_input_field, f'Error, expected {expected_email_input_field} did not match actual {actual_email_input_field}'

