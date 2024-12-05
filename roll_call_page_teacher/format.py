from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

email = "41147002s@gmail.com"
password = "Password123!"

try:
    # 登入
    driver.get("http://127.0.0.1:5173/")

    email_input = driver.find_element(
        By.XPATH, "//input[@type='text' and @placeholder='輸入您的電子郵件']")
    password_input = driver.find_element(
        By.XPATH, "//input[@type='password' and @placeholder='輸入您的密碼']")
    email_input.send_keys(email)
    password_input.send_keys(password)

    login_button = driver.find_element(
        By.XPATH, "//div[@class='justify-center items-center inline-flex cursor-pointer transition-all duration-100 w-full bg-blue-500 hover:bg-blue-700 h-12 px-3 py-4 rounded-md']")
    login_button.click()

    # 進入課程
    course_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[4]/div[2]/div/ul/li[1]/div")
    course_button.click()

    # 進入點名系統
    roll_call_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/ul[1]/li[4]/a")
    roll_call_button.click()

    # 尚未有教師端頁面

except Exception as e:
    print("檢查點名系統教師端發生錯誤：", str(e))

driver.quit()
