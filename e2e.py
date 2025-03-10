from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def test_scores_service(app_url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(app_url)

    time.sleep(2)

    header = driver.find_element(By.TAG_NAME, 'h1')
    score = driver.find_element(By.XPATH, '//*[@id="score"]')
    try:       
        assert header.text == "The score is:", "Test Failed!"
        assert 1<int(score.text)<1000, "Test Failed!"
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