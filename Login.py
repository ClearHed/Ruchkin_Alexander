from selenium import webdriver
import pytest
import BaseP
from selenium.webdriver.common.by import By

class LoginPage(BaseP):

    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    SUBMIT_BUTTON = (By.LINK_TEXT,"LOGIN")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_login_link_exist(self):
        return self.is_boolean(self.SUBMIT_BUTTON)

    def Llogin(self, username, password):
        self.ssend_keys(self.USERNAME, username)
        self.ssend_keys(self.PASSWORD, password)
        self.cclick(self.SUBMIT_BUTTON)