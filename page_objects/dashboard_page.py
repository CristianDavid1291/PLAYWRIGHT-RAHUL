from locators import DashboardLocators
from .orders_page import OrdersPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def select_orders_nav_link(self):
        DashboardLocators.get_orders_button(self.page).click()
        return OrdersPage(self.page)
