from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import json

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

email = "test@example.com"
password = "Password123!"

print("更改主題測試")

try:
    # 登入
    driver.get("https://swe.verypro.wtf/")

    email_input = driver.find_element(
        By.XPATH, "//input[@type='text' and @placeholder='輸入您的電子郵件']")
    password_input = driver.find_element(
        By.XPATH, "//input[@type='password' and @placeholder='輸入您的密碼']")
    email_input.send_keys(email)
    password_input.send_keys(password)

    login_button = driver.find_element(
        By.XPATH, "//div[@class='justify-center items-center inline-flex cursor-pointer transition-all duration-100 w-full bg-blue-500 hover:bg-blue-700 h-12 px-3 py-4 rounded-md']")
    login_button.click()

    # 進入設定頁面
    setting_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/ul[2]/li[1]")
    setting_button.click()

    # 切換身分至使用者(暫時)
    user = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[1]/div/div")
    user.click()

    # 展開主題選擇
    list = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/button")
    list.click()

    # 切換淺色模式
    light = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/ul/li[2]")
    light.click()
    # 測試方法待補

    # 再切換深色模式
    list = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/button")
    list.click()
    dark = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/ul/li[3]")
    dark.click()
    # 測試方法待補

except Exception as e:
    print("設定(教師端/學生端)更改主題發生錯誤：", str(e))

finally:
    driver.quit()
