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

try:

    driver.get("https://swe.verypro.wtf/")

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

    def check_element(xpath, description):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            print(f"{description} 存在且顯示正常")
            return element
        except NoSuchElementException:
            print(f"{description} 不存在或顯示異常")
            return None

    # 檢查登入按鈕
    check_link("/html/body/div/div/div[1]/div[1]/div[5]", "登入")

    # 檢查忘記密碼連結
    check_link("/html/body/div/div/div[1]/div/div[4]/div/a", "忘記密碼")
    check_afterlink("/html/body/div/div/main/div/p[1]", "忘記密碼？")
    driver.back()

    # 檢查還沒創建帳號?連結
    check_link("/html/body/div/div/div[1]/div[1]/div[7]/div/a", "還沒創建帳號?註冊")
    check_afterlink("/html/body/div/div/main/div/p[1]", "創建帳號")
    driver.back()

    # 檢查常見問題按鈕
    check_link("/html/body/div/div/nav/div/div/a[2]/button", "常見問題")
    check_afterlink("/html/body/div/div/div[1]/main/h1", "常見問題")
    driver.back()

    # 檢查網頁名稱和logo
    check_element("/html/body/div/div/nav/div/div/a[1]/span", "網頁名稱")
    check_element(
        "//img[@alt='logo' and @src='/assets/logo-DoNYWvJZ.png']", "logo")

    # 檢查歡迎文字和吉祥物
    welcome = check_element("/html/body/div/div/div[1]/div[1]/p[1]", "歡迎文字")
    if welcome.text == "歡迎回來":
        print("歡迎文字正確")
    else:
        print("歡迎文字不正確")

    check_element(
        "//img[@src='/assets/login-placeholder-CNdZqKmF.png']", "吉祥物")

    # 檢查電子郵件地址和密碼輸入
    email_input = check_element(
        "//input[@type='text' and @placeholder='輸入您的電子郵件']", "電子郵件地址輸入框")
    if email_input:
        email_input.send_keys("test@example.com")
        print("電子郵件地址輸入框可輸入")

    password_input = check_element(
        "//input[@type='password' and @placeholder='輸入您的密碼']", "密碼輸入框")
    if password_input:
        password_input.send_keys("Password123!")
        print("密碼輸入框可輸入")

    # # 檢查記住我
    # remember_me_checkbox = check_element(
    #     "//input[@id='icon' and @type='checkbox']", "記住我")
    # if remember_me_checkbox:
    #     remember_me_checkbox.click()
    #     if remember_me_checkbox.is_selected():
    #         print("記住我勾選欄可勾選且成功勾選")
    #     else:
    #         print("記住我勾選欄未能成功勾選")

    # 檢查網站資訊
    check_element("/html/body/div/div/div[2]", "網站資訊")

except Exception as e:
    print("檢查登入頁面格式發生錯誤：", str(e))
