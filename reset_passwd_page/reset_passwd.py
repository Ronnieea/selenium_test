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
    passwd = credential['密碼']
    wrong_passwd = "1"

    # 設立密碼-正確版
    try:
        driver.get("http://127.0.0.1:5173/set-password")

        new_passwd_input = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div/input")
        confirm_passwd_input = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div/input")
        new_passwd_input.send_keys(passwd)
        confirm_passwd_input.send_keys(passwd)

        terms_checkbox = driver.find_element(
            By.XPATH, "//input[@id='icon' and @type='checkbox']")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        create_account_button = driver.find_element(
            By.XPATH, "//div[@class='justify-center items-center inline-flex cursor-pointer transition-all duration-100 w-full bg-blue-500 hover:bg-blue-700 h-12 px-3 py-4 rounded-md w-full']")
        create_account_button.click()

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                # modified
                (By.XPATH, "//div[@class='justify-center items-center inline-flex cursor-pointer transition-all duration-100 w-full bg-blue-500 hover:bg-blue-700 h-12 px-3 py-4 rounded-md']"))
        )
        print(f"用戶 {index + 1} 成功創建帳號！")

        # 設立密碼-錯誤版(無勾選同意)
        new_passwd_input.send_keys(passwd)
        confirm_passwd_input.send_keys(passwd)

        if terms_checkbox.is_selected():
            terms_checkbox.click()

        create_account_button.click()

        error_message_element = webdriver(driver, 3).until(
            EC.presence_of_element_located(
                # 系統直接提示，如何取得錯誤提示?
                (By.XPATH, "//div[contains(@id, 'headlessui-portal-root')]"))
        )
        print(f"用戶 {index + 1} 無勾選同意，出現錯誤提示:", error_message_element.text)

    except Exception as e:
        print(f"用戶 {index + 1} 創建帳號發生錯誤：", str(e))

    # 設立密碼-錯誤版(密碼不一致)
    try:
        driver.get("http://127.0.0.1:5173/set-password")
        new_passwd_input = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div/input")
        confirm_passwd_input = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div/input")
        new_passwd_input.send_keys(passwd)
        confirm_passwd_input.send_keys(wrong_passwd)

        error_message_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                # modified
                (By.XPATH, "/html/body/div/div/main/div/div[3]/span"))
        )
        print(f"用戶 {index + 1} 獲取的錯誤提示:", error_message_element.text)
    except Exception as e:
        print(f"用戶 {index + 1} 沒有獲取錯誤提示，發生錯誤：", str(e))

    time.sleep(1)

driver.quit()
