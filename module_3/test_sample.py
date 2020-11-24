from selenium import webdriver
import time 

link = "http://selenium1py.pythonanywhere.com/ru/"

search_first_button_locator = 'login_link'
enter_email_locator = 'id_login-username'
user_email = 'denis.troyan92@gmail.com'
enter_password_locator = 'id_login-password'
user_password = 'uVw6R2uqCyjQYeq'
second_button_locator = 'login_submit'

def login_authorize():

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(link)

        step1 = browser.find_element_by_id(search_first_button_locator)
        step1.click()
        
        # Act
        step2 = browser.find_element_by_id(enter_email_locator)
        step2.send_keys(user_email)

        step3 = browser.find_element_by_id(enter_password_locator)
        step3.send_keys(user_password)

        step4 = browser.find_element_by_name(second_button_locator)
        step4.click()

        # Assert
        page_messsage = browser.find_element_by_xpath('//div[@class="alertinner wicon"]')
        authorize_result = page_messsage.text
        assert 'Рады видеть вас снова' in authorize_result


    finally:
          browser.quit()

login_authorize()
