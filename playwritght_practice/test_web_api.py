
from playwright.sync_api import Playwright, expect
from utils.base_api import APIUtils

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("cristiandavid1291@gmail.com")
    page.locator("#userPassword").fill("Manizales2025++")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    

    #orders history page -> order is present
    page.locator("tr").filter(has_text=order_id).get_by_role("button", name="View").click()
    # Example assertion: check if order details are visible
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")

    
