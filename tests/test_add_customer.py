import allure
from data.data import ExpectedResult
from pages.xyz_bank_page import XYZBankPage
from helpers import generators
from helpers import helpers

class TestAddCustomer:
    @allure.epic('Операции с пользователями')
    @allure.feature('Добавление нового пользователя')
    @allure.title('Добавление пользователя с автогенерацией данных')
    def test_add_customer(self, driver):
        # arrange
        add_customer = XYZBankPage(driver)

        # act
        add_customer.open_tab_add_customer()
        post_code = generators.generate_post_code()
        customer_name = helpers.convert_post_code_in_name(post_code)
        add_customer.send_first_name(customer_name)
        add_customer.send_last_name(customer_name)
        add_customer.send_post_code(post_code)
        add_customer.click_but_add_customer()
        actual_text_alert = add_customer.text_in_alert()
        add_customer.click_tab_customers()
        search_result = add_customer.find_new_customer(customer_name, customer_name, post_code)

        # assert
        assert ExpectedResult.ALERT_TEXT_ADD_CUSTOMER in actual_text_alert, 'Нет в уведомлении информации о добавлении пользователя'
        assert search_result, 'Пользователь не найден'