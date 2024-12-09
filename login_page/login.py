from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def get_credentials(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


credentials = get_credentials('data.json')

# initiate webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


for index, credential in enumerate(credentials):
    email = credential['gmail']
    password = credential['密碼']

    try:
        driver.get("https://swe.verypro.wtf/")

        email_input = driver.find_element(
            By.XPATH, "//input[@type='text' and @placeholder='輸入您的電子郵件']")
        password_input = driver.find_element(
            By.XPATH, "//input[@type='password' and @placeholder='輸入您的密碼']")
        email_input.send_keys(email)
        password_input.send_keys(password)

        remember_me_checkbox = driver.find_element(
            By.XPATH, "//input[@id='icon' and @type='checkbox']")
        if not remember_me_checkbox.is_selected():
            remember_me_checkbox.click()

        login_button = driver.find_element(
            By.XPATH, "//div[@class='justify-center items-center inline-flex cursor-pointer transition-all duration-100 w-full bg-blue-500 hover:bg-blue-700 h-12 px-3 py-4 rounded-md']")
        login_button.click()

        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                # need to modify
                (By.XPATH, "//main[@class='wrap flex-auto m-4 space-y-2']//h1[@class='text-4xl font-bold']"))
        )

        print(f"用戶 {index + 1} 成功登入！")

        # test for remember me checkbox
        driver.get("http://127.0.0.1:5173/")
        time.sleep(2)
        email_input = driver.find_element(
            By.XPATH, "//input[@type='text' and @placeholder='輸入您的電子郵件']")
        password = driver.find_element(
            By.XPATH, "//input[@type='password' and @placeholder='輸入您的密碼']")

        if email_input.get_attribute('value') == email and password_input.get_attribute('value') == password:
            print(f"用戶 {index + 1} 記住我功能測試成功！")
        else:
            print(f"用戶 {index + 1} 記住我功能測試失敗！")

    except Exception as e:
        try:
            error_message_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(@id, 'headlessui-portal-root')]"))
            )
            error_message_text = error_message_element.text
            print(f"用戶 {index + 1} 獲取到的錯誤提示：", error_message_text)

        except Exception as e:
            print(f"用戶 {index + 1} 發生錯誤：", str(e))

    time.sleep(1)

driver.quit()
