from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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

email = "41147002s@gapps.ntnu.edu.tw"
password = "RonnieeA23$10"
invalid_email = "41147002s@gamil.com"

try:
    driver.get("https://swe.verypro.wtf/")

    # 進入創建帳號頁面
    create_account_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div[1]/div[7]/div/a")
    create_account_button.click()

    # 創建帳號-錯誤版
    email_input = driver.find_element(
        By.XPATH, "//input[@type='text' and @placeholder='請輸入您的電子郵件']")
    email_input.send_keys(invalid_email)

    send_button = driver.find_element(
        By.XPATH, "/html/body/div/div/main/div/div[3]")
    send_button.click()
    time.sleep(2)

    try:
        error_message = driver.find_element(By.XPATH, "")  # path 待添加
        print("輸入錯誤的電子郵件地址，顯示錯誤提示：", error_message.text)
    except NoSuchElementException:
        print("輸入錯誤的電子郵件地址，但未顯示錯誤提示，測試失敗")


except Exception as e:
    print("創建帳號測試發生錯誤：", str(e))

finally:
    driver.quit()
