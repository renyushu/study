from selenium import webdriver


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def find_info():
    pass


driver = start_chrome()
