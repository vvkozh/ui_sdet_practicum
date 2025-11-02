import allure
from pages.xyz_bank_page import XYZBankPage
from helpers import helpers

class TestSortName:
    @allure.epic('Операции с пользователями')
    @allure.feature('Сортировка пользователей')
    @allure.title('Тест сортировки пользователей по имени')
    def test_sort_name(self, driver):
        # arrange
        sort_name = XYZBankPage(driver)

        # act
        sort_name.click_tab_customers()
        before_sort_name = sort_name.get_name_customers()
        sort_name.click_sort_name()
        after_sort_name = sort_name.get_name_customers()
        expected_result = helpers.sorting_data(before_sort_name)

        # assert
        assert after_sort_name == expected_result, 'Имена отсортированы неправильно'
