import allure
from pages.xyz_bank_page import XYZBankPage
from helpers import helpers

class TestDeleteCustomer:
    @allure.epic('Операции с пользователями')
    @allure.feature('Удаление пользователя')
    @allure.title('Тест удаления пользователя с длиной имени ближайшей к среднему')
    def test_delete_customer(self, driver):
        # arrange
        delete_customer = XYZBankPage(driver)

        # act
        delete_customer.click_tab_customers()
        customers_name = delete_customer.get_name_customers()
        avg_name = helpers.find_customer_avg_name(customers_name)
        delete_customer.delete_customer(avg_name)
        actual_customers_name = delete_customer.get_name_customers()

        # assert
        assert avg_name in actual_customers_name, f'Пользователь с именем {avg_name} не удален'
