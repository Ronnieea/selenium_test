from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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

    # 展開功能欄
    function_bar = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/div[1]")
    function_bar.click()

    # 功能欄檢查
    def check_link(xpath, description):
        try:
            link_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            link_element.click()
            print(f"{description} 連結可點擊")
        except Exception:
            print(f"{description} 連結不存在或無法點擊")

    def check_afterlink(xpath, description):
        try:
            link_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            if link_element.text == description:
                print(f"{description} 連結後的頁面存在")
            else:
                print(f"{description} 連結後的頁面不存在")
        except Exception as e:
            print(f"{description} 連結後的頁面不存在")

    # 1. 檢查首頁連結
    check_link("/html/body/div/div/div[1]/div/div/ul[1]/li[1]", "首頁")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "嗨，使用者!")
    driver.back()

    # 2. 檢查個人AI聊天室連結
    check_link("/html/body/div/div/div[1]/div/div/ul[1]/li[2]", "個人AI聊天室")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "AI聊天室")
    driver.back()

    # 3. 檢查課程清單連結
    check_link("/html/body/div/div/div[1]/div/div/ul[1]/li[3]", "課程清單")
    i = 1
    while True:
        time.sleep(2)
        try:
            course_element = driver.find_element(
                By.XPATH, f"/html/body/div/div/div[1]/div/div/ul[1]/ul/li[{
                    i}]/a/div")

            course_name = course_element.text
            check_link(f"/html/body/div/div/div[1]/div/div/ul[1]/ul/li[{
                i}]/a/div", course_name)
            check_afterlink("/html/body/div/div/div[1]/main/h1", course_name)
            if i == 1:
                course = driver.find_element(
                    By.XPATH, "/html/body/div/div/div[1]/div/div/ul[1]/li[3]")
                course.click()
            i += 1
        except NoSuchElementException:
            break

    # 4. 檢查設定連結
    check_link("/html/body/div/div/div[1]/div/div/ul[2]/li[1]", "設定")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "設定")
    driver.back()

    # 5. 檢查常見問題連結
    check_link("/html/body/div/div/div[1]/div/div/ul[2]/li[2]", "常見問題")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "常見問題")
    driver.back()

    # 6. 檢查隱私權及使用條款連結
    check_link("/html/body/div/div/div[1]/div/div/ul[2]/li[3]", "隱私權及使用條款")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "隱私權及使用條款")
    driver.back()

    # 7. 檢查登出鈕連結
    function_bar = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/div[1]")
    function_bar.click()

    check_link("/html/body/div/div/div[1]/div/div/div[2]/a", "登出按鈕")
    check_afterlink("/html/body/div/div/div[1]/div[1]/p[1]", "歡迎回來")
    driver.back()

    # 8. 檢查分組聊天系統連結
    check_link("/html/body/div/div/div[1]/div/div/div[2]/a", "分組系統")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "分組系統")
    driver.back()

    # 9. 檢查點名系統連結
    check_link("/html/body/div/div/div[1]/div/div/ul[1]/li[4]", "點名系統")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "點名系統")
    driver.back()

except Exception as e:
    print("檢查教師端功能欄發生錯誤：", str(e))

driver.quit()
