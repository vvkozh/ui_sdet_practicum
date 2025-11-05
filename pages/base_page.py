import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимость элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельность элемента")
    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_clickable_element(locator, timeout)
        element.click()

    @allure.step('Ввод текста в поле')
    def send_text_to_input(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст уведомления')
    def get_alert_notification(self):
        alert = Alert(self.driver)
        alert_notification = alert.text
        return alert_notification

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        element = self.driver.find_elements(*locator)
        return element

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Закрыть уведомление')
    def close_alert(self):
        alert = Alert(self.driver)
        alert.accept()



