from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """
        Set up the test environment by initializing WebDriver and UrbanRoutesPage.
        """
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (optional)
        chrome_options.add_argument("--no-sandbox")  # Optional, for environments like Docker
        chrome_options.add_argument("--disable-dev-shm-usage")  # Optional

        # Add Chrome capabilities for logging through the chrome_options
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Initialize the WebDriver service and the ChromeDriver instance with options
        service = Service(executable_path='/path/to/chromedriver')  # Specify if chromedriver isn't in PATH

        # Now create the driver using options and service
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Initialize your page object here if needed
        # cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        """
        Tear down the test environment by quitting the WebDriver instance.
        """
        if cls.driver:
            cls.driver.quit()
