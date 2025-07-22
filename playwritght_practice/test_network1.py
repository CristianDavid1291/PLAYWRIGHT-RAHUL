
from playwright.sync_api import Page
import time 

fake_payload = {"data": [],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fake_payload
    )


def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.locator("#userEmail").fill("cristiandavid1291@gmail.com")
    page.locator("#userPassword").fill("Manizales2025++")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)    
    time.sleep(2) 
