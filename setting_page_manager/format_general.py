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

email = "test@example.com"
password = "Password123!"


# 設定頁面格式檢查
print("設定頁面(管理端)-一般格式檢查")
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

    # 1. 檢查設定文字
    try:
        settings_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/main/h1")
                                           ))
        print("設定文字存在")

    except NoSuchElementException:
        print("設定文字不存在，測試失敗")

    # 2. 檢查個人資料欄位
    try:
        upload_photo_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/button")
                                           ))
        print("上傳照片按鈕存在")
    except NoSuchElementException:
        print("上傳照片按鈕不存在，測試失敗")

    try:
        remove_photo_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/a")
        print("移除照片按鈕存在")
    except NoSuchElementException:
        print("移除照片按鈕不存在，測試失敗")

    # 3. 檢查語系與更改主題欄位
    try:
        language_dropdown = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/button")
        print("語系下拉選單存在")
    except NoSuchElementException:
        print("語系下拉選單不存在，測試失敗")

    if language_dropdown:
        language_dropdown.click()
        try:
            chinese = driver.find_element(
                By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/ul/li[1]")
            print("繁體中文存在")
        except Exception as e:
            print("繁體中文不存在，測試失敗")

        try:
            english = driver.find_element(
                By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/ul/li[2]")
            print("英文存在")
        except Exception as e:
            print("英文不存在，測試失敗")

    try:
        theme_dropdown = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/button")
        print("更改主題下拉選單存在")
    except NoSuchElementException:
        print("更改主題下拉選單不存在，測試失敗")

    if theme_dropdown:
        theme_dropdown.click()
        try:
            auto = driver.find_element(
                By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/ul/li[1]")
            print("自動主題存在")
        except Exception as e:
            print("自動主題不存在，測試失敗")

        try:
            light = driver.find_element(
                By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/ul/li[2]")
            print("淺色主題存在")
        except Exception as e:
            print("淺色主題不存在，測試失敗")

        try:
            light = driver.find_element(
                By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/ul/li[3]")
            print("深色主題存在")
        except Exception as e:
            print("深色主題不存在，測試失敗")

    # 4. 檢查輸入舊密碼/更改密碼/確認新密碼輸入框
    try:
        old_password_input = driver.find_element(
            By.XPATH, "//input[@id='passwordInput' and @type='password' and @placeholder='請輸入舊密碼']")
        print("舊密碼輸入框存在")
    except NoSuchElementException:
        print("舊密碼輸入框不存在，測試失敗")

    try:
        new_password_input = driver.find_element(
            By.XPATH, "//input[@id='passwordInput' and @type='password' and @placeholder='請輸入新密碼']")
        print("新密碼輸入框存在")
    except NoSuchElementException:
        print("新密碼輸入框不存在，測試失敗")

    try:
        confirm_password_input = driver.find_element(
            By.XPATH, "//input[@id='passwordInput' and @type='password' and @placeholder='請再次輸入新密碼']")
        print("確認新密碼輸入框存在")
    except NoSuchElementException:
        print("確認新密碼輸入框不存在，測試失敗")

    # 5. 檢查修改密碼按鈕
    try:
        save_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div")
        print("修改密碼按鈕存在")
    except NoSuchElementException:
        print("修改密碼按鈕不存在，測試失敗")

    # 6. 檢查匯入資料按鍵
    try:
        import_data_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[1]/div/button[2]")
        print("匯入資料按鈕存在")
    except Exception as e:
        print("匯入資料按鈕不存在")


except Exception as e:
    print("設定頁面(管理端)格式檢查發生錯誤：", str(e))

finally:
    driver.quit()
