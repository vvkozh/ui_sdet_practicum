import allure
from pages.xyz_bank_page import XYZBankPage

@allure.epic('Операции с пользователями')
@allure.feature('Сортировка пользователей')
@allure.title('Тест сортировки пользователей по имени')
def test_sort_name(driver):
    with allure.step('Подготовка теста'):
        sort_name = XYZBankPage(driver)

    with allure.step('Получение списка имен'):
        sort_name.click_tab_customers()
        customers_name = sort_name.get_name_customers()

    if customers_name == sorted(customers_name, reverse=True):
        with allure.step('Проверка сортировка по возрастанию A-Z'):
            sort_name.click_sort_name()
            sort_asc = sort_name.get_name_customers()
            assert sort_asc == sorted(customers_name), 'Имена не отсортированы по возрастанию A-Z'
        with allure.step('Проверка сортировка по убыванию Z-A'):
            sort_name.click_sort_name()
            sort_desc = sort_name.get_name_customers()
            assert sort_desc == sorted(customers_name, reverse=True), 'Имена не отсортированы по убыванию Z-A'
    else:
        with allure.step('Проверка сортировка по убыванию Z-A'):
            sort_name.click_sort_name()
            sort_desc = sort_name.get_name_customers()
            assert sort_desc == sorted(customers_name, reverse=True), 'Имена не отсортированы по убыванию Z-A'
        with allure.step('Проверка сортировка по возрастанию A-Z'):
            sort_name.click_sort_name()
            sort_asc = sort_name.get_name_customers()
            assert sort_asc == sorted(customers_name), 'Имена не отсортированы по возрастанию A-Z'