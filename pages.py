from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # You can adjust the timeout to suit your needs.

    # Locators
    FROM_FIELD = (By.ID, "from")
    To_FIELD = (By.ID, "to")
    PLAN_BUTTON = (By.ID, "")
    PHONE_FIELD = (By.ID, "phone")
    SMS_CODE_FIELD = (By.ID, "sms")
    CREDIT_CARD_MODAL = (By.CLASS_NAME, "card-input")
    LINK_BUTTON = (By.ID, "link-button")
    DRIVER_COMMENT_FIELD = (By.ID, "comment")
    BLANKET_CHECKBOX = (By.ID, "order-blanket")
    HANDKERCHIEF_CHECKBOX = (By.ID, "order-handkerchief")
    ICE_CREAM_BUTTON = (By.XPATH, "")
    CAR_SEARCH_MODAL = (By.ID, "car-search-modal")

    # Methods with explicit waits
    def set_address(self, address):
        field = self.wait.until(EC.presence_of_element_located(self.ADDRESS_FIELD))
        field.clear()
        field.send_keys(address)

    def select_supportive_plan(self):
        button = self.wait.until(EC.element_to_be_clickable(self.PLAN_BUTTON))
        if not button.is_selected():
            button.click()

    def fill_phone_number(self, phone_number, helpers):
        phone_field = self.wait.until(EC.presence_of_element_located(self.PHONE_FIELD))
        phone_field.send_keys(phone_number)
        sms_code = helpers.retrieve_phone_code()
        sms_code_field = self.driver.find_element(*self.SMS_CODE_FIELD)
        sms_code_field.send_keys(sms_code)

    def add_credit_card(self, cvv):
        card_field = self.wait.until(EC.presence_of_element_located(self.CREDIT_CARD_MODAL))
        card_field.send_keys(cvv)
        card_field.send_keys("\t")  # Simulate focus shift with TAB key
        link_button = self.wait.until(EC.element_to_be_clickable(self.LINK_BUTTON))
        link_button.click()

    def comment_for_driver(self, comment):
        field = self.wait.until(EC.presence_of_element_located(self.DRIVER_COMMENT_FIELD))
        field.send_keys(comment)

    def order_blanket_and_handkerchiefs(self):
        self.wait.until(EC.element_to_be_clickable(self.BLANKET_CHECKBOX)).click()
        self.wait.until(EC.element_to_be_clickable(self.HANDKERCHIEF_CHECKBOX)).click()

    def order_ice_cream(self, count=2):
        for _ in range(count):
            self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_BUTTON)).click()

    def order_taxi(self, helpers, comment=""):
        self.fill_phone_number(helpers.retrieve_phone_number(), helpers)
        self.comment_for_driver(comment)
        self.wait.until(EC.presence_of_element_located(self.CAR_SEARCH_MODAL))

    # Added assertions or checks for verification during tests
    def is_address_set(self):
        return bool(self.driver.find_element(*self.ADDRESS_FIELD).get_attribute("value"))

    def is_plan_selected(self):
        return self.driver.find_element(*self.PLAN_BUTTON).is_selected()

    def is_phone_number_filled(self):
        return bool(self.driver.find_element(*self.PHONE_FIELD).get_attribute("value"))

    def is_card_linked(self):
        return self.driver.find_element(*self.CREDIT_CARD_MODAL).get_attribute("value") != ""

    def is_driver_comment_added(self):
        return bool(self.driver.find_element(*self.DRIVER_COMMENT_FIELD).get_attribute("value"))

    def are_blanket_and_handkerchiefs_ordered(self):
        blanket = self.driver.find_element(*self.BLANKET_CHECKBOX).is_selected()
        handkerchief = self.driver.find_element(*self.HANDKERCHIEF_CHECKBOX).is_selected()
        return blanket and handkerchief

    def are_ice_creams_ordered(self, count):
        ice_creams = len(self.driver.find_elements(*self.ICE_CREAM_BUTTON))
        return ice_creams == count

    def is_car_search_model_visible(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()
