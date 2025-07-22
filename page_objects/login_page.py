from locators import LoginLocators
from .dashboard_page import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page
    
    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")
    
    def login(self, user_data):
        LoginLocators.get_email_input(self.page).fill(user_data['username'])
        LoginLocators.get_password_input(self.page).fill(user_data['password'])
        LoginLocators.get_login_button(self.page).click()
        return DashboardPage(self.page)
