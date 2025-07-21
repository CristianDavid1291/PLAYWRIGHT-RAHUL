from playwright.sync_api import Page, expect
import time

def test_UIChecks(page: Page):
    #hide/show place holder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alert boxes
    page.on("dialog", lambda dialog: dialog.accept())# event listener for dialog
    page.get_by_role("button", name="Confirm").click()
    
    #FrameHandling
    #page.pause() 
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="Courses" ,exact=True).click()
    expect(pageFrame.locator("body")).to_contain_text("Browse products")

    #Check price rice is equal 37
    #identify price column
    #identify rice row
    #extract price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).text_content() == "Price":
            price_index = index
            break
    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(price_index)).to_have_text("37")