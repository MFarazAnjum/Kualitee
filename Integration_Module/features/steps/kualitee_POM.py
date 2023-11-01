import configparser
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

config = configparser.ConfigParser()


class LoginPage:
    with open('Integration_Module/features/steps/config.ini', 'r') as f:
        config_string = '[DEFAULT]\n' + f.read()
    config.read_string(config_string)

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "email_id")
        self.password_textbox = (By.ID, "password")
        self.role_name_textbox = (By.NAME, "role_name")
        self.role_description_textbox = (By.XPATH, '//*[@id="tinymce"]')
        self.login_button = (By.CLASS_NAME, 'submit-btn')
        self.cancel_button = (By.XPATH, '//*[@value="Cancel"]')
        self.checkbox = (By.NAME, "can_delete")
        self.setting_button = (By.XPATH, '//span[@id = "tour`-side-combine-btn"]//a[@title = "Settings"]')
        self.role_button = (By.XPATH, '//*[text() = "Roles"]')
        self.manage_role_text = (By.XPATH, '//a[text() = "Manage Roles"]')
        self.create_role_button = (By.XPATH, '//a[text() = "Create New Role"]')
        self.create_new_role_text = (By.XPATH, '//a[text() = "Create New Role"]')
        self.edit_role_text = (By.XPATH, '//a[text() = "Edit Role"]')
        self.required_text = (By.XPATH, '//*[contains(text(), "required")]')
        self.domain_dropdown = (By.ID, "domain_projects")
        self.role_header = (By.XPATH, '//th[text() = "Role"]')
        self.user_header = (By.XPATH, '//th[text() = "Users"]')
        self.search_input = (By.XPATH, '//input[@type = "search"]')
        self.search_role_and_delete = (By.XPATH, '//td[text() = " edit clone 12 reg "]/..//a[@title = "Delete"]')

    def open_page(self):
        url = config.get('DEFAULT', 'URL')
        self.driver.get(url)

    def enter_username(self):
        username = config.get('DEFAULT', 'USERNAME')
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self):
        password = config.get('DEFAULT', 'PASSWORD')
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_role_name(self, role_name):
        self.driver.find_element(*self.role_name_textbox).send_keys(role_name)

    def enter_role_description(self, role_description):
        self.driver.find_element(*self.role_description_textbox).click()
        self.driver.find_element(*self.role_description_textbox).send_keys(role_description)

    def enter_search_input(self, search_word):
        self.driver.find_element(*self.search_input).send_keys(search_word)
        time.sleep(5)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_cancel(self):
        self.driver.find_element(*self.cancel_button).click()

    def click_settings(self):
        time.sleep(8)
        self.driver.find_element(*self.setting_button).click()

    def click_roles(self):
        self.driver.find_element(*self.role_button).click()

    def click_dropdown(self):
        self.driver.find_element(*self.domain_dropdown).click()
        self.driver.find_element(*self.domain_dropdown).send_keys(Keys.ENTER)

    def verify_manage_role_text(self):
        text = self.driver.find_element(*self.manage_role_text).text
        return text

    def click_create_role(self):
        self.driver.find_element(*self.create_role_button).click()

    def click_save(self):
        self.driver.find_element(*self.login_button).click()

    def click_role_and_user_header(self):
        self.driver.find_element(*self.role_header).click()
        time.sleep(2)
        self.driver.find_element(*self.role_header).click()
        time.sleep(2)
        self.driver.find_element(*self.user_header).click()
        time.sleep(2)
        self.driver.find_element(*self.user_header).click()

    def verify_create_new_role_text(self):
        text = self.driver.find_element(*self.create_new_role_text).text
        return text

    def verify_edit_role_text(self):
        text = self.driver.find_element(*self.edit_role_text).text
        return text

    def verify_required_text(self):
        wait = WebDriverWait(self.driver, 10)
        text = self.driver.find_element(*self.required_text)
        wait.until(ec.visibility_of(element=text))
        return text

    def click_checkbox(self):
        self.driver.find_element(*self.checkbox).click()
