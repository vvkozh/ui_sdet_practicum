from selenium.webdriver.common.by import By

class XYZBankLocator:
    TAB_ADD_CUSTOMER = (By.XPATH, '//button[@ng-click="addCust()"]')
    FIELD_FIRST_NAME = (By.XPATH, '//input[@ng-model="fName"]')
    FIELD_LAST_NAME = (By.XPATH, '//input[@ng-model="lName"]')
    FIELD_POST_CODE = (By.XPATH, '//input[@ng-model="postCd"]')
    BUT_ADD_CUSTOMER = (By.XPATH, '//button[@class="btn btn-default"]')
    TAB_CUSTOMERS = (By.XPATH, '//button[@ng-click="showCust()"]')
    SORT_NAME = (By.XPATH, '//a[contains(text(), "First Name")]')
    TABL_USERS = (By.CSS_SELECTOR, 'tr[ng-repeat*="cust in Customers"]')
    NAME_LOCATOR = (By.XPATH, '//tr[@class="ng-scope"][1]/child::td[1]')

    @staticmethod
    def data_customer_locator(tabl_line, number_column):
        return By.XPATH, f'//tr[@class="ng-scope"][{tabl_line}]/child::td[{number_column}]'

    @staticmethod
    def but_delete_locator(first_name):
        return By.XPATH, f'//td[contains(text(), "{first_name}")]/../td/button[contains(text(), "Delete")]'

    @staticmethod
    def all_data_customer_locator(first_name, last_name, post_code):
        return By.XPATH, f'//td[contains(text(), "{first_name}")]//following-sibling::td[contains(text(), "{last_name}")]/following-sibling::td[contains(text(), "{post_code}")]/parent::tr'

