import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage
from time import sleep


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """
        Setup method to initialize the WebDriver and check server status.
        """
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # For environments like Docker
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Add Chrome capabilities for logging
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Set up the WebDriver service
        service = Service(executable_path='/path/to/chromedriver')  # Specify your chromedriver path

        # Initialize the WebDriver with the given options and service
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.get("https://cnt-b49eab23-48f6-4d85-9c8b-618a174940b6.containerhub.tripleten-services.com")
        cls.page = UrbanRoutesPage(cls.driver)

        print("WebDriver initialized. Starting tests.")

        if helpers.is_url_reachable():
            print("Server is reachable. Proceeding with tests.")
        else:
            print("Server is not reachable. Please check the server.")
            cls.teardown_class()
            raise Exception("Server not reachable.")

    @classmethod
    def teardown_class(cls):
        """
        Teardown method to quit the WebDriver.
        """
        try:
            # Ensure resources are released even if test fails
            print("Ending the tests and releasing resources.")
        finally:
            cls.driver.quit()
            print("WebDriver quit. Resources released.")

    def test_set_route(self):
        self.page.set_address("123 Urban Ave")
        assert self.page.is_address_set(), "Address was not set correctly"
        print("Test: Address set successfully.")

    def test_select_plan(self):
        self.page.select_supportive_plan()
        assert self.page.is_plan_selected(), "Supportive plan was not selected"
        print("Test: Supportive plan selected.")

    def test_fill_phone_number(self):
        self.page.fill_phone_number("1234567890", helpers)
        assert self.page.is_phone_number_filled(), "Phone number was not entered correctly"
        print("Test: Phone number filled and SMS code entered.")

    def test_fill_card(self):
        self.page.add_credit_card("123")
        assert self.page.is_card_linked(), "Credit card was not linked"
        print("Test: Credit card linked successfully.")

    def test_comment_for_driver(self):
        self.page.comment_for_driver("Please drive carefully.")
        assert self.page.is_driver_comment_added(), "Driver comment was not added"
        print("Test: Driver comment added.")

    def test_order_blanket_and_handkerchiefs(self):
        self.page.order_blanket_and_handkerchiefs()
        assert self.page.are_blanket_and_handkerchiefs_ordered(), "Blanket and handkerchiefs were not ordered"
        print("Test: Blanket and handkerchiefs ordered.")

    def test_order_2_ice_creams(self):
        self.page.order_ice_cream(2)
        assert self.page.are_ice_creams_ordered(2), "Ice creams were not ordered properly"
        print("Test: Two ice creams ordered.")

    def test_car_search_model_appears(self):
        self.page.order_taxi(helpers, comment="Need a child seat.")
        assert self.page.is_car_search_model_visible(), "Car search model did not appear"
        print("Test: Taxi ordered successfully.")
