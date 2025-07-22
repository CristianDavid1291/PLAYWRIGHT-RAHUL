
from playwright.sync_api import Page, Playwright
from utils.base_api import APIUtils
import time 

fake_payload = {"data": [],"message":"No Orders"}

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=12345")


def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.locator("#userEmail").fill("cristiandavid1291@gmail.com")
    page.locator("#userPassword").fill("Manizales2025++")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.locator("tr").filter(has_text="ADIDAS ORIGINAL").get_by_role("button", name="View").first.click()
    time.sleep(4)

def test_local_storage(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    api_utils = APIUtils()
    token = api_utils.get_token(playwright)

    #script to inject token into local storage
    page.add_init_script(f"window.localStorage.setItem('token', '{token}')")

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(4)
    
   
