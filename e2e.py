from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def test_scores_service(app_url):
    driver = webdriver.Chrome()
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
    app_url="http://127.0.0.1:5000"
    if test_scores_service(app_url) == True:
        os._exit(0)
    else:
        os._exit(-1)

main_function()