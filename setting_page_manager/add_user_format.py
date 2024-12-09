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

print("設定頁面(管理端)-匯入資料-新增用戶格式檢查")
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

    # 進入匯入資料頁面
    import_data_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[1]/div/button[2]")
    import_data_button.click()

    # 打開新增用戶頁面
    add_user_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[4]/div[2]/div/div/div")
    add_user_button.click()

    # 1. 檢查姓氏輸入框
    try:
        last_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @placeholder='請輸入姓氏']"))
        )
        print("姓氏輸入框存在")
    except Exception as e:
        print("姓氏輸入框不存在")

    # 2. 檢查名字輸入框
    try:
        first_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @placeholder='請輸入名字']"))
        )
        print("名字輸入框存在")
    except Exception as e:
        print("名字輸入框不存在")

    # 3. 檢查學號/教職員編號輸入框
    try:
        number = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @placeholder='請輸入教職員編號']"))
        )
        print("學號/教職員編號輸入框存在")
    except Exception as e:
        print("學號/教職員編號輸入框不存在")

    # 4. 檢查電子郵件地址輸入框
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @placeholder='example@example.com']"))
        )
        print("電子郵件地址輸入框存在")
    except Exception as e:
        print("電子郵件地址輸入框不存在")

    # 5. 檢查用戶組下拉選單
    try:
        users = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[1]/button"))
        )
        print("用戶組下拉選單存在")
    except Exception as e:
        print("用戶組下拉選單不存在")

    if users:
        users.click()
        try:
            manager = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[2]/ul/li[1]/li"))
            )
            print("管理員選項存在")
        except Exception as e:
            print("管理員選項不存在")

        try:
            manager = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[2]/ul/li[2]"))
            )
            print("教師選項存在")
        except Exception as e:
            print("教師選項不存在")

        try:
            manager = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[2]/ul/li[3]"))
            )
            print("學生選項存在")
        except Exception as e:
            print("學生選項不存在")

    # 檢查班級下拉選單
    try:
        class_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div/div/div/button"))
        )
        print("班級下拉選單存在")
    except Exception as e:
        print("班級下拉選單不存在")

    # 檢查新增用戶按鈕
    try:
        add_user = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div"))
        )
        print("新增用戶按鈕存在")
    except Exception as e:
        print("新增用戶按鈕不存在")

except Exception as e:
    print("設定頁面(管理端)-匯入資料-新增用戶格式檢查測試發生錯誤：", str(e))

finally:
    driver.quit()
