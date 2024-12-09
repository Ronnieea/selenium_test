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

print("更改語系測試")

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

    # 展開語言選擇
    list = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/button")
    list.click()

    # 切換英文
    english = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/ul/li[2]")
    english.click()

    title = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/main/h1")
    if title.text == "Setting":
        print("語系切換成功，介面已改成英文")
    else:
        print("語系切換失敗，介面未改成英文")

    # 再切換回中文
    list = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/button")
    list.click()
    chinese = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/ul/li[1]")
    chinese.click()
    if title.text == "設定":
        print("語系切換成功，介面已改成中文")
    else:
        print("語系切換失敗，介面未改成中文")

except Exception as e:
    print("設定(管理端)更改語系發生錯誤：", str(e))

finally:
    driver.quit()
