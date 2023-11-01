import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from kualitee_POM import LoginPage


@given('I launch Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()


@when('I open Kualitee homepage')
def open_login_page(context):
    login_page = LoginPage(context.driver)
    login_page.open_page()
    context.driver.implicitly_wait(10)


@when('Enter username and password')
def enter_credentials(context):
    login_page = LoginPage(context.driver)
    login_page.enter_username()
    login_page.enter_password()


@when('click on login button')
def click_login_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()


@when('click on setting button')
def click_settings_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_settings()


@when('click on role button')
def click_role_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_roles()


@then('Manage Roles page will be open and checked')
def check_manage_role_text(context):
    login_page = LoginPage(context.driver)
    element = login_page.verify_manage_role_text()
    exp = "Manage Roles"
    assert exp == element


@then('click create role button')
def click_create_role_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_create_role()


@then('Create new role page will be open and checked')
def check_create_new_role_text(context):
    login_page = LoginPage(context.driver)
    element = login_page.verify_create_new_role_text()
    exp = "Create New Role"
    assert exp == element


@then(u'click save button')
def click_save_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_save()


@then(u'Check required fields message is prompted or not')
def check_required_field_visibility(context):
    login_page = LoginPage(context.driver)
    element = login_page.verify_required_text().text
    exp = "Name is required"
    assert exp == element


@then(u'click checkbox')
def click_checkbox(context):
    login_page = LoginPage(context.driver)
    time.sleep(5)
    login_page.click_checkbox()
    time.sleep(10)  # used for first check and then uncheck
    login_page.click_checkbox()
    time.sleep(10)


@then('click cancel button')
def click_cancel_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_cancel()


@then(u'enter roleName "{role}" and Description "{description}"')
def enter_role_description(context, role, description):
    login_page = LoginPage(context.driver)
    time.sleep(4)
    login_page.enter_role_name(role)
    iframe = context.driver.find_element(By.ID, "description_ifr")
    context.driver.switch_to.frame(iframe)
    element_in_iframe = context.driver.find_element(By.TAG_NAME, "p")
    element_in_iframe.send_keys(description)
    context.driver.switch_to.default_content()


@then(u'verify edit role page is landed')
def verify_landed_on_edit_page(context):
    login_page = LoginPage(context.driver)
    element = login_page.verify_edit_role_text()
    exp = "Edit Role"
    assert exp == element


@then(u'click domain project dropdown')
def click_domain_project_dropdown(context):
    login_page = LoginPage(context.driver)
    login_page.click_dropdown()


@then(u'click table headers and observe change in data')
def click_domain_project_dropdown(context):
    login_page = LoginPage(context.driver)
    login_page.click_role_and_user_header()


@then(u'click search and enter "{word}" and observe change')
def click_domain_project_dropdown(context, word):
    login_page = LoginPage(context.driver)
    login_page.enter_search_input(word)
