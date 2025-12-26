from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


# ======================================
# LambdaTest Driver Factory (Selenium 4)
# ======================================
def get_lambdatest_driver(test_name):
    options = ChromeOptions()
    options.browser_version = "143.0"
    options.platform_name = "Windows 10"

    lt_options = {
        "username": "gowthamipg8888",
        "accessKey": "KFIGD3VUgMMQlkEMKqdowcIOwd0zlwMwrIHaMfNRH0CNVfN3vZ",
        "video": True,
        "network": True,
        "timezone": "Kolkata",
        "build": "SeleniumAutomationBuild",
        "project": "SeleniumAutomationProject",
        "name": test_name,
        "w3c": True,
        "plugin": "python-python"
    }

    options.set_capability("LT:Options", lt_options)

    driver = webdriver.Remote(
        command_executor="https://hub.lambdatest.com/wd/hub",
        options=options
    )
    return driver


# ==============================
# Scenario 1: Simple Form Demo
# (ASSERTS KEPT — NOT CHANGED)
# ==============================
def simple_form_demo():
    driver = get_lambdatest_driver("Simple Form Demo")
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")

        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Simple Form Demo"))
        ).click()

        assert "simple-form-demo" in driver.current_url, "URL validation failed!"

        message = "Welcome to LambdaTest"
        wait.until(
            EC.presence_of_element_located((By.ID, "user-message"))
        ).send_keys(message)

        driver.find_element(By.ID, "showInput").click()

        displayed_text = wait.until(
            EC.presence_of_element_located((By.ID, "message"))
        ).text

        assert displayed_text == message, (
            f"Expected '{message}', but got '{displayed_text}'"
        )

        print("✅ Simple Form Demo Passed")

    finally:
        driver.quit()


# ======================================
# Scenario 2: Drag & Drop Slider
# (Print current value, stop at 95)
# ======================================
def drag_and_drop_slider():
    driver = get_lambdatest_driver("Drag And Drop Slider")
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")

        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Drag & Drop Sliders"))
        ).click()

        slider = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='15']"))
        )

        actions = ActionChains(driver)

        while True:
            output = driver.find_element(By.ID, "rangeSuccess")
            current_value = int(output.text)
            print("Current Slider Value:", current_value)

            if current_value >= 95:
                print("✅ Slider reached 95, closing browser")
                break

            actions.click_and_hold(slider).move_by_offset(215, 0).release().perform()
            time.sleep(0.2)

    finally:
        driver.quit()


# ======================================
# Scenario 3: Input Form Submit
# ======================================
def input_form_submit_test():
    driver = get_lambdatest_driver("Input Form Submit")
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Input Form Submit']"))
        ).click()

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))
        ).click()

        name_field = driver.find_element(By.ID, "name")
        print("Name field validation message:",
              name_field.get_attribute("validationMessage"))

        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "inputEmail4").send_keys("john@example.com")
        driver.find_element(By.ID, "inputPassword4").send_keys("Test@123")
        driver.find_element(By.ID, "company").send_keys("Example Inc")
        driver.find_element(By.ID, "websitename").send_keys("www.example.com")
        driver.find_element(By.ID, "inputCity").send_keys("New York")
        driver.find_element(By.ID, "inputAddress1").send_keys("123 Main St")
        driver.find_element(By.ID, "inputAddress2").send_keys("Suite 101")
        driver.find_element(By.ID, "inputState").send_keys("NY")
        driver.find_element(By.ID, "inputZip").send_keys("10001")

        Select(
            driver.find_element(By.NAME, "country")
        ).select_by_visible_text("United States")

        driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

        success_msg = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='success-msg hidden']"))
        )
        print("Success Message:", success_msg.text)

    finally:
        driver.quit()


# ==============================
# Execute All Scenarios
# ==============================
if __name__ == "__main__":
    #simple_form_demo()
    #drag_and_drop_slider()
    input_form_submit_test()
