
from playwright.sync_api import Playwright, expect
from utils import APIUtils, Base
from page_objects import LoginPage, DashboardPage, OrdersPage
import pytest


def test_e2e_web_api(playwright:Playwright, user_data):
  

    #create order id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_data)

    #login
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login(user_data)
    order_page = dashboard_page.select_orders_nav_link()
    details_order_page = order_page.select_order(order_id)

   
    # Example assertion: check if order details are visible
    expect(details_order_page.get_message()).to_contain_text("Thank you for Shopping With Us")
