from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# initiate webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

email = "test@example.com"
password = "Password123!"
verification_code = "123456"  # temperated

try:
    # qrcode點名(改成手動手機測試)
    # driver.get("http://127.0.0.1:5173/")

    # email_input = driver.find_element(
    #     By.XPATH, "//input[@type='text' and @placeholder='輸入您的電子郵件']")
    # password_input = driver.find_element(
    #     By.XPATH, "//input[@type='password' and @placeholder='輸入您的密碼']")
    # email_input.send_keys(email)
    # password_input.send_keys(password)

    # login_button = driver.find_element(
    #     By.XPATH, "//div[@class='justify-center items-center inline-flex cursor-pointer transition-all duration-100 w-full bg-blue-500 hover:bg-blue-700 h-12 px-3 py-4 rounded-md']")
    # login_button.click()

    # # 進入課程
    # course_button = driver.find_element(
    #     By.XPATH, "/html/body/div/div/div[1]/main/div[4]/div[2]/div/ul/li[1]/div")
    # course_button.click()

    # # 進入點名系統
    # roll_call_button = driver.find_element(
    #     By.XPATH, "/html/body/div/div/div[1]/div/div/ul[1]/li[4]/a")
    # roll_call_button.click()

    # qrcode_button = driver.find_element(
    #     By.XPATH, "/html/body/div/div/div[1]/main/div[1]/div[2]")
    # qrcode_button.click()

    # 驗證碼輸入點名
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

    # 進入課程
    course_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[4]/div[2]/div/ul/li[1]/div")
    course_button.click()

    # 進入點名系統
    roll_call_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/ul[1]/li[4]/a")
    roll_call_button.click()

    qrcode_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[1]/div[2]")
    qrcode_button.click()

    # 切換到驗證碼輸入
    verification_button = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/button[2]")
    verification_button.click()

    # 輸入驗證碼
    verification_input = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/input")
    verification_input.send_keys(verification_code)

    # 送出
    send = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[3]")
    send.click()

except Exception as e:
    print(str(e))

driver.quit()
