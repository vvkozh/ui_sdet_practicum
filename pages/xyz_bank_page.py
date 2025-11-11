import allure

from locators.xyz_bank_locator import XYZBankLocator
from pages.base_page import BasePage

class XYZBankPage(BasePage):
    @allure.step('Открыть вкладку Add customer')
    def open_tab_add_customer(self):
        self.click_on_element(XYZBankLocator.TAB_ADD_CUSTOMER)

    @allure.step('Заполнить имя')
    def send_first_name(self, first_name):
        self.send_text_to_input(XYZBankLocator.FIELD_FIRST_NAME, first_name)
        return first_name

    @allure.step('Заполнить фамилию')
    def send_last_name(self, last_name):
        self.send_text_to_input(XYZBankLocator.FIELD_LAST_NAME, last_name)
        return last_name

    @allure.step('Заполнить post code')
    def send_post_code(self, post_code):
        self.send_text_to_input(XYZBankLocator.FIELD_POST_CODE, post_code)
        return post_code

    @allure.step('Нажать на кнопку Add Customer')
    def click_but_add_customer(self):
        self.click_on_element(XYZBankLocator.BUT_ADD_CUSTOMER)

    @allure.step('Получить текст уведомления о добавлении пользователи')
    def text_in_alert(self):
        text_alert = self.get_alert_notification()
        self.close_alert()
        return text_alert

    @allure.step('Открыть вкладку Customers')
    def click_tab_customers(self):
        self.click_on_element(XYZBankLocator.TAB_CUSTOMERS)

    @allure.step('Нажать на сортировку по имени')
    def click_sort_name(self):
        self.click_on_element(XYZBankLocator.SORT_NAME)

    @allure.step('Получить все имена')
    def get_name_customers(self):
        self.wait_for_element(XYZBankLocator.TABL_USERS)
        elements = self.find_element(XYZBankLocator.TABL_USERS)
        names = []
        for i in range(1, len(elements) + 1):
             first_name = self.get_text_on_element(XYZBankLocator.data_customer_locator(i, 1))
             names.append(first_name)
        return names

    @allure.step('Поиск добавленного пользователя')
    def find_new_customer(self, first_name, last_name, post_code):
        try:
            self.find_element(XYZBankLocator.all_data_customer_locator(first_name, last_name, post_code))
            return True
        except:
            return False

    @allure.step('Удалить пользователя')
    def delete_customer(self, first_name):
        self.click_on_element(XYZBankLocator.but_delete_locator(first_name))
