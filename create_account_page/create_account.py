from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def get_credentials(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


credentials = get_credentials('data.json')

# initiate webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


for index, credential in enumerate(credentials):
    email = credential['gmail']

    try:
        driver.get("http://127.0.0.1:5173/")

        create_account_href = driver.find_element(
            By.XPATH, "//a[@href='/register']")

    except Exception as e:
        print(f"用戶 {index + 1} 發生錯誤:", str(e))
