from selenium import webdriver
from selenium.webdriver.common.by import By
import time


sbis_url = 'https://sbis.ru/'
tensor_url = 'https://tensor.ru/'
driver = webdriver.Chrome()

try:
    driver.get(sbis_url)
    driver.maximize_window()
    assert driver.current_url == sbis_url, f'Неверно открыт сайт. Ожидали: {sbis_url}, получили: {driver.current_url}.'

    contact_button = driver.find_element(By.XPATH, '//*[text()="Контакты"]')
    find_class = 'sbisru-Header__menu-link sbisru-Header__menu-link--hover'
    assert contact_button.text == 'Контакты', f'Неверное именование элемента. Ожидали: Контакты, получили: {contact_button.text}.'
    assert contact_button.get_attribute('class') == find_class, f'Обращение было к неверному классу. Ожидали: "{find_class}", получили: "{contact_button.get_attribute("class")}".'
    assert contact_button.is_displayed(), 'Кнопка не отображается'
    contact_button.click()

    tensor_logo = driver.find_element(By.CSS_SELECTOR, '.sbis_ru-container .sbisru-Contacts__logo-tensor')
    assert tensor_logo.is_displayed(), 'Логотип не отображается'
    tensor_logo.click()

    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_url, f'Неверно открыт сайт. Ожидали: {tensor_url}, получили: {driver.current_url}.'

    strength_in_people_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert strength_in_people_block.text == 'Сила в людях', f'Неверное именование элемента. Ожидали: "Сила в людях", получили: "{strength_in_people_block.text}".'
    assert strength_in_people_block.is_displayed(), 'Блок "Сила в людях" не отображается'
    about_button = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-link')
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", about_button)
    time.sleep(1)
    about_button.click()
    time.sleep(2)
    assert driver.current_url == 'https://tensor.ru/about', f'Неверно открыт сайт. Ожидали: https://tensor.ru/about, получили: {driver.current_url}.'

finally:
    driver.quit()

