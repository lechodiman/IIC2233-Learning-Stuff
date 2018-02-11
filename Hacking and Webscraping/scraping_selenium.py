from selenium import webdriver

driver = webdriver.Firefox()
driver.set_page_load_timeout(30)
driver.get('https://www.facebook.com')
driver.find_element_by_id('email').send_keys('Selenium Webdriver')
driver.find_element_by_name('pass').send_keys('Python')
driver.find_element_by_id('loginbutton').click()
