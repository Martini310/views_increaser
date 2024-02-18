from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()

while True:
    website_random_URL = 'https://billwise-martini310.koyeb.app/auth/login'

    driver.get(website_random_URL)
    time.sleep(5)
    height = int(driver.execute_script("return document.documentElement.scrollHeight"))

    while True:
        driver.execute_script('window.scrollBy(0,10)')
        time.sleep(0.10)
        totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        
        if totalScrolledHeight == height:
            driver.switch_to.window(driver.window_handles[0])
            break
    print('***Web Page Visited***')