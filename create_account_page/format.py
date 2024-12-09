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

    # 進入創建帳號頁面
    create_account_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div[1]/div[7]/div/a")
    create_account_button.click()

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

    # 1. 檢查創建帳號與說明文字
    title = check_element("/html/body/div/div/main/div/p[1]", "創建帳號標題")
    if title.text == "創建帳號":
        print("標題內容正確")
    else:
        print("標題內容不正確")

    explain = check_element(
        "/html/body/div/div/main/div/p[2]/span[1]", "創建帳號說明文字-1")
    if explain.text == "請輸入學校機構的電子郵件帳號，":
        print("說明內容-1正確")
    else:
        print("說明內容-1不正確")
    explain = check_element(
        "/html/body/div/div/main/div/p[2]/span[3]", "創建帳號說明文字-2")
    if explain.text == "我們將會傳送一則郵件協助創建帳號。":
        print("說明內容-2正確")
    else:
        print("說明內容-2不正確")

    # 2. 檢查電子郵件地址輸入框是否可輸入
    email_input = check_element(
        "//input[@type='text' and @placeholder='請輸入您的電子郵件']", "電子郵件地址輸入框")
    if email_input:
        email_input.send_keys("test@example.com")
        print("電子郵件地址輸入框可輸入")

    # 3. 檢查傳送電子郵件按鈕
    check_link("/html/body/div/div/main/div/div[3]", "傳送電子郵件按鈕")

    # 4. 檢查已經有帳號了嗎？登入按鍵
    check_link("/html/body/div/div/main/div/div[5]/a", "已經有帳號了嗎？登入按鍵")
    check_afterlink("/html/body/div/div/div[1]/div[1]/p[1]", "歡迎回來")

except Exception as e:
    print("創建帳號頁面檢查發生錯誤：", str(e))

finally:
    # 關閉瀏覽器
    driver.quit()
