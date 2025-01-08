from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    """
    Page object for interacting with the Urban Routes page.
    """

    def __init__(self, driver):
        self.driver = driver

    def set_address(self, departure, destination):
        """
        Set the departure and destination address fields on the page.
        :param departure: The departure address
        :param destination: The destination address
        """
        # Find the departure and destination address fields by their ID
        departure_field = self.driver.find_element(By.ID, "departureField")
        destination_field = self.driver.find_element(By.ID, "destinationField")

        # Clear any existing input and set the new values
        departure_field.clear()
        departure_field.send_keys(departure)
        destination_field.clear()
        destination_field.send_keys(destination)

    def select_supportive_plan(self, plan_name):
        """
        Select a supportive plan from the dropdown menu by plan name.
        :param plan_name: Name of the supportive plan to select
        """
        # Find the supportive plan dropdown by ID
        plan_dropdown = self.driver.find_element(By.ID, "supportivePlanDropdown")
        plan_dropdown.click()

        # Find the plan option using XPath based on the plan name and select it
        plan_option = self.driver.find_element(By.XPATH, f"//option[text()='{plan_name}']")
        plan_option.click()

    def fill_phone_number(self, phone_number):
        """
        Fill in the phone number input field.
        :param phone_number: Phone number to input
        """
        phone_field = self.driver.find_element(By.ID, "phoneNumber")
        phone_field.clear()
        phone_field.send_keys(phone_number)

    def add_credit_card(self, card_number, exp_date, cvv):
        """
        Add a credit card information in the respective fields.
        :param card_number: The credit card number
        :param exp_date: The expiration date of the card
        :param cvv: The CVV of the card
        """
        card_number_field = self.driver.find_element(By.ID, "cardNumber")
        exp_date_field = self.driver.find_element(By.ID, "expDate")
        cvv_field = self.driver.find_element(By.ID, "cvv")

        card_number_field.clear()
        card_number_field.send_keys(card_number)

        exp_date_field.clear()
        exp_date_field.send_keys(exp_date)

        cvv_field.clear()
        cvv_field.send_keys(cvv)

    def write_comment_for_driver(self, comment):
        """
        Write a comment for the driver in the designated input field.
        :param comment: The comment to write
        """
        comment_field = self.driver.find_element(By.ID, "commentForDriver")
        comment_field.clear()
        comment_field.send_keys(comment)

    def order_blanket_and_handkerchiefs(self):
        """
        Order blanket and handkerchiefs from the shopping options.
        """
        blanket_checkbox = self.driver.find_element(By.ID, "blanketOption")
        handkerchief_checkbox = self.driver.find_element(By.ID, "handkerchiefOption")

        if not blanket_checkbox.is_selected():
            blanket_checkbox.click()

        if not handkerchief_checkbox.is_selected():
            handkerchief_checkbox.click()

    def order_ice_creams(self):
        """
        Order ice creams from the shopping options.
        """
        ice_cream_checkbox = self.driver.find_element(By.ID, "iceCreamOption")
        if not ice_cream_checkbox.is_selected():
            ice_cream_checkbox.click()

    def order_taxi_with_supportive_plan(self):
        """
        Order a taxi with a supportive plan.
        """
        taxi_button = self.driver.find_element(By.ID, "taxiButton")
        taxi_button.click()

