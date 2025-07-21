from playwright.sync_api import Page, expect

# def test_playwright_basics(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://rahulshettyacademy.com")

def test_playwright_shortcut(page: Page):
    page.goto("https://rahulshettyacademy.com")

def test_core_locators(page: Page):
    #page.pause()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learninghhhhh")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
   

    
   
