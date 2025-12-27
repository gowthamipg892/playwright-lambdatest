import pytest
import json
import urllib.parse
import re
from playwright.sync_api import sync_playwright, expect
from config import LT_OPTIONS, BROWSERS


def launch_browser(p, browser_cap):
    capabilities = {
        "browserName": browser_cap["browserName"],
        "LT:Options": LT_OPTIONS
    }
    caps = urllib.parse.quote(json.dumps(capabilities))
    ws_url = f"wss://cdp.lambdatest.com/playwright?capabilities={caps}"
    return p.chromium.connect(ws_url)


@pytest.mark.parametrize("browser_cap", BROWSERS)
def test_simple_form_demo(browser_cap):
    with sync_playwright() as p:
        browser = launch_browser(p, browser_cap)
        page = browser.new_page()

        page.goto("https://www.lambdatest.com/selenium-playground")
        page.locator("text=Simple Form Demo").click()
        expect(page).to_have_url(re.compile(".*simple-form-demo.*"))

        msg = "Welcome to LambdaTest"
        page.fill("#user-message", msg)
        page.click("#showInput")
        expect(page.locator("#message")).to_have_text(msg)

        browser.close()


'''@pytest.mark.parametrize("browser_cap", BROWSERS)
def test_drag_and_drop_slider(browser_cap):
    import time
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        # Launch LambdaTest browser (NOT local)
        browser = launch_browser(p, browser_cap)
        page = browser.new_page()

        try:
            page.goto("https://www.lambdatest.com/selenium-playground")
            page.set_viewport_size({"width": 1920, "height": 1080})

            # Click Drag & Drop Sliders
            page.locator("text=Drag & Drop Sliders").click()

            # Slider & output
            slider = page.locator("//input[@value='15']")
            output = page.locator("#rangeSuccess")

            # Get slider coordinates (same as ActionChains)
            box = slider.bounding_box()
            assert box is not None, "Slider bounding box not found"

            while True:
                current_value = int(output.inner_text())
                print("Current Slider Value:", current_value)

                if current_value >= 95:
                    print("✅ Slider reached 95")
                    break

                # Mouse drag (Playwright version of ActionChains)
                page.mouse.move(
                    box["x"] + box["width"] / 2,
                    box["y"] + box["height"] / 2
                )
                page.mouse.down()
                page.mouse.move(
                    box["x"] + box["width"] / 2 + 215,
                    box["y"] + box["height"] / 2,
                    steps=5
                )
                page.mouse.up()

                time.sleep(0.2)

        finally:
            browser.close()



@pytest.mark.parametrize("browser_cap", BROWSERS)
def test_input_form_submit(browser_cap):
    with sync_playwright() as p:
        browser = launch_browser(p, browser_cap)
        page = browser.new_page()

        page.goto("https://www.lambdatest.com/selenium-playground")
        page.locator("text=Input Form Submit").click()
        page.locator("button:has-text('Submit')").click()

        page.fill("#name", "John Doe")
        page.fill("#inputEmail4", "john@example.com")
        page.fill("#inputPassword4", "Test@123")
        page.fill("#company", "Example Inc")
        page.fill("#websitename", "www.example.com")
        page.fill("#inputCity", "New York")
        page.fill("#inputAddress1", "123 Main St")
        page.fill("#inputAddress2", "Suite 101")
        page.fill("#inputState", "NY")
        page.fill("#inputZip", "10001")
        page.select_option("select[name='country']", label="United States")

        page.click("button:has-text('Submit')")
        expect(page.locator("p.success-msg")).to_be_visible()

        browser.close()'''
