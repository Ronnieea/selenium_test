from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

email = "test@example.com"
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

    # 檢查日曆
    calendar_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[1]/div[1]/div/div[2]"))
    )

    if calendar_element:
        print("日曆存在且顯示正常")
    else:
        print("日曆不存在或顯示異常")

    # 檢查每節課堂顯示
    class_elements = driver.find_elements(
        By.CSS_SELECTOR, "div.w-full.p-4.rounded-lg.border.items-center")
    if len(class_elements) > 0:
        for i, class_element in enumerate(class_elements, start=1):
            class_name = class_element.text
            print(f"第 {i} 節課顯示正常：{class_name}")
    else:
        print("未找到任何課堂信息，顯示異常")

    # 檢查qrcode點名按鈕
    qrcode_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[1]/main/div[1]/div[2]"))
    )

    if qrcode_button:
        print("QR Code 點名按鈕存在且可點擊")
    else:
        print("QR Code 點名按鈕不存在或無法點擊")

except Exception as e:
    print("檢查點名系統學生端發生錯誤：", str(e))

driver.quit()
