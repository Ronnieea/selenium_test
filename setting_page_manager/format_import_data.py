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

print("設定頁面(管理端)-匯入資料格式檢查")
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

    # 1. 檢查課程資料匯入欄位
    try:
        upload_course_csv_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/a/button"))
        )
        print("課程資料上傳按鈕存在")
    except NoSuchElementException:
        print("課程資料上傳按鈕不存在，測試失敗")

    try:
        remove_course_file_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div/a")
        print("課程資料移除檔案按鈕存在")
    except NoSuchElementException:
        print("課程資料移除檔案按鈕不存在，測試失敗")

    # 2. 檢查教職員資料匯入欄位
    try:
        upload_staff_csv_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/a/button"))
        )
        print("教職員資料上傳按鈕存在")
    except NoSuchElementException:
        print("教職員資料上傳按鈕不存在，測試失敗")

    try:
        remove_staff_file_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/a")
        print("教職員資料移除檔案按鈕存在")
    except NoSuchElementException:
        print("教職員資料移除檔案按鈕不存在，測試失敗")

    # 3. 檢查新增用戶欄位
    try:
        add_user_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[4]/div[2]/div/div/div")
        print("個別新增用戶按鈕存在")
    except NoSuchElementException:
        print("個別新增用戶按鈕不存在，測試失敗")

    # 4. 檢查學校電子郵件網域欄位
    try:
        modify_email_domain_input = driver.find_element(
            By.XPATH, "//input[@type='text' and @placeholder='@example.edu']")
        print("修改電子郵件網域輸入框存在")
    except NoSuchElementException:
        print("修改電子郵件網域輸入框不存在，測試失敗")

    try:
        modify_email_domain_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div")
        print("修改電子郵件網域按鈕存在")
    except NoSuchElementException:
        print("修改電子郵件網域按鈕不存在，測試失敗")

    # 5. 新增課程欄位
    try:
        add_course_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[5]/div[2]/div/div/div")
        print("個別新增課程按鈕存在")
    except NoSuchElementException:
        print("個別新增課程按鈕不存在，測試失敗")

except Exception as e:
    print("設定頁面(管理端)測試發生錯誤：", str(e))

finally:
    driver.quit()
