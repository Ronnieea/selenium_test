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


# 更改密碼 - 正確版
print("更改密碼測試: 正確版")
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

    # 進入設定頁面
    setting_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/ul[2]/li[1]/a/div/svg")
    setting_button.click()

    # 切換身分至使用者(暫時)
    user = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[1]/div/div")
    user.click()

    # 密碼輸入位置
    old_passwd_input = driver.find_element(
        By.XPATH, "//input[@id='passwordInput' and @placeholder='請輸入舊密碼' and @type='password']")
    new_passwd_input = driver.find_element(
        By.XPATH, "//input[@id='passwordInput' and @placeholder='請輸入新密碼' and @type='password']")
    confirm_passwd_input = driver.find_element(
        By.XPATH, "@id='passwordInput' and @placeholder='請再次輸入新密碼' and @type='password'")
    reset_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div")

    old_passwd_input.send_keys(password)
    new_passwd_input.send_keys(password + "&")
    confirm_passwd_input.send_keys(password + "&")
    reset_button.click()

    function_bar = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/div[1]")
    function_bar.click()  # 展開功能欄

    logout_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/div[2]/a")
    logout_button.click()  # 登出並重新登入

    email_input = driver.find_element(
        By.XPATH, "//input[@type='text' and @placeholder='輸入您的電子郵件']")
    password_input = driver.find_element(
        By.XPATH, "//input[@type='password' and @placeholder='輸入您的密碼']")
    email_input.send_keys(email)
    password_input.send_keys(password + "&")

    ogin_button = driver.find_element(
        By.XPATH, "//div[@class='justify-center items-center inline-flex cursor-pointer transition-all duration-100 w-full bg-blue-500 hover:bg-blue-700 h-12 px-3 py-4 rounded-md']")
    login_button.click()

    try:
        link_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div[1]/main/h1"))
        )
        if link_element.text == "嗨，使用者！":
            print("成功更改密碼並登入至首頁")
        else:
            print("更改密碼失敗，無法登入")
    except Exception as e:
        print("更改密碼失敗，無法登入")

except Exception as e:
    print("檢查設定(教師端/學生端)更改密碼發生錯誤：", str(e))

# 更改密碼 - 錯誤版
print("更改密碼測試: 錯誤版")

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

    # 進入設定頁面
    setting_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/div/div/ul[2]/li[1]/a/div/svg")
    setting_button.click()

    # 切換身分至使用者(暫時)
    user = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[1]/div/div")
    user.click()

    # 密碼輸入位置
    old_passwd_input = driver.find_element(
        By.XPATH, "//input[@id='passwordInput' and @placeholder='請輸入舊密碼' and @type='password']")
    new_passwd_input = driver.find_element(
        By.XPATH, "//input[@id='passwordInput' and @placeholder='請輸入新密碼' and @type='password']")
    confirm_passwd_input = driver.find_element(
        By.XPATH, "@id='passwordInput' and @placeholder='請再次輸入新密碼' and @type='password'")
    reset_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div")

    # 1.舊密碼與新密碼相同
    old_passwd_input.clear()
    new_passwd_input.clear()
    confirm_passwd_input.clear()
    old_passwd_input.send_keys(password)
    new_passwd_input.send_keys(password)
    confirm_passwd_input.send_keys(password)
    reset_button.click()
    time.sleep(2)

    # 檢查是否跳出更改密碼錯誤
    try:
        error_message = driver.find_element(
            # 補error message的位置
            By.XPATH, "//div[contains(@id, 'headlessui-portal-root')]")
        print("測試 1: 舊密碼與新密碼相同，錯誤提示: ", error_message.text)
    except NoSuchElementException:
        print("測試 1: 未找到錯誤提示，測試失敗")

    # 2. 新密碼與確認新密碼不同
    old_passwd_input.clear()
    new_passwd_input.clear()
    confirm_passwd_input.clear()
    old_passwd_input.send_keys(password)
    new_passwd_input.send_keys(password + "&")
    confirm_passwd_input.send_keys(password + "&E")
    reset_button.click()
    time.sleep(2)

    # 檢查是否跳出更改密碼錯誤
    try:
        error_message = driver.find_element(
            # 補error message的位置
            By.XPATH, "//div[contains(@id, 'headlessui-portal-root')]")
        print("測試 2: 新密碼與確認新密碼不同，錯誤提示：", error_message.text)
    except NoSuchElementException:
        print("測試 2: 未找到錯誤提示，測試失敗")

    # 3. 新密碼不滿足密碼格式
    old_passwd_input.clear()
    new_passwd_input.clear()
    confirm_passwd_input.clear()
    old_passwd_input.send_keys(password)
    new_passwd_input.send_keys("123")
    confirm_passwd_input.send_keys("123")
    reset_button.click()
    time.sleep(2)

    # 檢查是否跳出更改密碼錯誤
    try:
        error_message = driver.find_element(
            # 補error message的位置
            By.XPATH, "//div[contains(@id, 'headlessui-portal-root')]")
        print("測試 3: 新密碼不符合格式，錯誤提示：", error_message.text)
    except NoSuchElementException:
        print("測試 3: 未找到錯誤提示，測試失敗")

    # 4. 任一欄位沒填寫
    old_passwd_input.clear()
    new_passwd_input.clear()
    confirm_passwd_input.clear()
    new_passwd_input.send_keys("123")
    reset_button.click()
    time.sleep(2)

    # 檢查是否跳出更改密碼錯誤
    try:
        error_message = driver.find_element(
            # 補error message的位置
            By.XPATH, "//div[contains(@id, 'headlessui-portal-root')]")
        print("測試 4: 任一欄位未填寫，錯誤提示：", error_message.text)
    except NoSuchElementException:
        print("測試 4: 未找到錯誤提示，測試失敗")

except Exception as e:
    print("檢查設定(教師端/學生端)更改密碼發生錯誤：", str(e))

driver.quit()
