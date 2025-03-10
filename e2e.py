from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless
chrome_options.add_argument("--disable-gpu")  # Necessary for some headless systems
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues

def test_scores_service(app_url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(app_url)

    time.sleep(2)

    header = driver.find_element(By.TAG_NAME, 'h1')
    score = driver.find_element(By.XPATH, '//*[@id="score"]')
    try:       
        assert header.text == "The score is:", "Test Failed!"
        assert 1<int(score.text)<100, "Test Failed!"
        print("Test Passed!")
        driver.quit()
        return True
    except AssertionError:
        print("Test Failed!")
        driver.quit()
        return False


def main_function():
    app_url="http://127.0.0.1:8777"
    if test_scores_service(app_url) == True:
        os._exit(0)
    else:
        os._exit(-1)

main_function()