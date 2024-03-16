# web_scraper.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests


# 打开指定URL的网页，如果失败则重试3次，每次失败后等待3秒
def open_webpage_with_chrome(url):
    driver = None
    for _ in range(3):
        try:
            driver = webdriver.Remote(
                command_executor="http://chrome:4444/wd/hub",
                options=get_chrome_options()
            )
            driver.get(url)
            time.sleep(1)
            check_webpage_status(url)
            return driver.page_source
        except Exception as e:
            print(f"An error occurred: {e}, retrying in 3 seconds...")
            time.sleep(3)
        finally:
            if driver:
                driver.quit()
    raise Exception("Max retries exceeded.")


# 获取Chrome的选项配置
def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options


# 检查网页的状态，如果状态码不是200，则抛出异常
def check_webpage_status(url):
    response = requests.get(url, timeout=10)  # 设置超时时间为10秒
    if response.status_code != 200:
        raise Exception(f"Failed to open webpage: {url}")


# 从指定的API URL获取JSON数据
def get_json_from_api(api_url):
    response = requests.get(api_url, timeout=10)  # 设置超时时间为10秒
    response.raise_for_status()
    return response.json()


# 向指定的API URL发送JSON数据
def post_json_to_api(api_url, data):
    response = requests.post(api_url, json=data, timeout=10)  # 设置超时时间为10秒
    response.raise_for_status()
    return response.json()
