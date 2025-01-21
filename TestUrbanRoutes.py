import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage
import helpers
from data import SERVER_URL


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """
        Setup method to initialize WebDriver and check server status.
        """
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()  # Adjust if using path
        cls.driver.get(SERVER_URL)  # Use the URL from data.py
        cls.page = UrbanRoutesPage(cls.driver)

        if helpers.is_server_working():
            print("Server is working. Proceeding with tests.")
        else:
            print("Server is not working. Please check the server.")
            cls.teardown_class()
            raise Exception("Server not reachable.")

    @classmethod
    def teardown_class(cls):
        """
        Teardown method to quit the WebDriver.
        """
        cls.driver.quit()
        print("WebDriver quit. Resources released.")

    def test_set_route(self):
        self.page.set_address("123 Urban Ave")
        print("Test: Address set successfully.")

    def test_select_plan(self):
        self.page.select_supportive_plan()
        print("Test: Supportive plan selected.")

    def test_fill_phone_number(self):
        self.page.fill_phone_number("1234567890", helpers)
        print("Test: Phone number filled and SMS code entered.")

    def test_fill_card(self):
        self.page.add_credit_card("123")
        print("Test: Credit card linked successfully.")

    def test_comment_for_driver(self):
        self.page.comment_for_driver("Please drive carefully.")
        print("Test: Driver comment added.")

    def test_order_blanket_and_handkerchiefs(self):
        self.page.order_blanket_and_handkerchiefs()
        print("Test: Blanket and handkerchiefs ordered.")

    def test_order_ice_cream(self):
        self.page.order_ice_cream(2)
        print("Test: Two ice creams ordered.")

    def test_car_search_model_appears(self):
        self.page.order_taxi(helpers, comment="Need a child seat.")
        print("Test: Taxi ordered successfully.")
