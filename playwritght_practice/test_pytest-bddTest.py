import pytest
from pytest_bdd import *
from pytest_bdd import parsers
from page_objects.login_page import LoginPage
from playwritght_practice.utils.base_api import APIUtils
from playwright.sync_api import expect

scenarios('features\\order_transaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_order(playwright, username, password, shared_data):
    user_data = {'username': username, 'password': password}
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_data)
    shared_data['order_id'] = order_id

@given('the user is on landing page')
def navigate_to_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data['login_page'] = login_page

@when(parsers.parse('the user logs in with {username} and {password}'))
def login_user(username, password, shared_data):
    user_data = {'username': username, 'password': password}
    dashboard_page = shared_data['login_page'].login(user_data)
    shared_data['dashboard_page'] = dashboard_page

@when('select the orderId')
def select_order_id(shared_data):
    order_page = shared_data['dashboard_page'].select_orders_nav_link()
    details_order_page = order_page.select_order(shared_data['order_id'])
    shared_data['details_order_page'] = details_order_page

@then('order success message should be shown in details page')
def verify_order_success_message(shared_data):
    details_order_page = shared_data['details_order_page']
    expect(details_order_page.get_message()).to_contain_text("Thank you for Shopping With Us")