from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

online_sbis = 'https://fix-online.sbis.ru/'
current_auth_url = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
current_page_contact_url = 'https://fix-online.sbis.ru/page/dialogs'
my_login = 'Annushka'
my_password = 'Annushka123!'
massage = 'Приветули'
driver = webdriver.Chrome()

try:
    driver.get(online_sbis)
    driver.maximize_window()
    assert driver.current_url == current_auth_url, \
        f'Неверный адрес страницы авторизации. Ожидали "{current_auth_url}", а получили "{driver.current_url}"'

    # Вводим логин
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    time.sleep(5)
    login.send_keys(my_login, Keys.ENTER)
    time.sleep(1)
    assert login.is_displayed(), 'Поле ввода логина не отображается'
    assert login.get_attribute('value') == my_login

    # Вводим пароль и авторизуемся
    time.sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    assert password.is_displayed(), 'Поле ввода пароля не отображается'
    password.send_keys(my_password, Keys.ENTER)

    # Переходим на вкладку "Контакты"
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@data-qa="NavigationPanels-Accordion__title"][text()="Контакты"]').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]').click()
    time.sleep(2)
    assert driver.current_url == current_page_contact_url, \
        f'Неверный адрес страницы. Ожидали "{current_page_contact_url}", а получили "{driver.current_url}"'

    # Поиск и клик иконки ПЛЮС
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus').click()

    # В поисковую строку вводим имя адресата и выбираем адресата из списка
    time.sleep(2)
    find_person = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content .controls-Search__nativeField_caretEmpty')
    time.sleep(2)
    find_person.send_keys('Кошкин', Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[title="Кошкин Кот"]').click()

    # Отправляем сообщение
    time.sleep(2)
    add_text_massage = driver.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field')
    time.sleep(2)
    add_text_massage.send_keys(massage, Keys.CONTROL + Keys.ENTER)

    # Ищем сообщение из списка
    time.sleep(2)
    check_massage = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-expander p')[0]
    time.sleep(2)
    assert check_massage.text == massage, f"Сообщение найдено неверно. Ожидали: {massage}, получили: {check_massage}"

    # Удаляем сообщение
    action_chains = ActionChains(driver)
    time.sleep(2)
    action_chains.move_to_element(check_massage)
    time.sleep(2)
    action_chains.context_click(check_massage)
    action_chains.perform()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[text()="Удалить"]').click()

    # Проверяем, что среди сообщений нет нашего massage
    time.sleep(2)
    check_delete_massage = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-expander p')
    try:
        for i in check_delete_massage:
            assert i.text != massage, 'Сообщение не удалено.'
    finally:
        print('Всё ок')


finally:
    driver.quit()
