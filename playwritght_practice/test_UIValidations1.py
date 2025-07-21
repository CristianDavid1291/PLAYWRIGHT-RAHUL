from playwright.sync_api import Page, expect
import time 

def test_UIValidation_dynamic(page:Page):
    # iphone X, Nokia Edge -> verify 2 items in cart
   
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button", name ="Add ").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button", name ="Add ").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_child_window(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as popup_info:
        page.locator(".blinkingText").click()
        child_page = popup_info.value
        text = child_page.locator(".red").text_content()
        # extract mentor@rahulshettyacademy.com from text
        email = text.split("at")[1].strip().split(" ")[0]
        print(email)
        

        
