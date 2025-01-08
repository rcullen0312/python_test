import helpers  # Importing helpers to check the server


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """
        Runs before all tests to check if the server is working.
        """
        if helpers.is_server_working():  # Check server status using helpers.is_server_working
            print("Server is working. Proceeding with tests.")
        else:
            print("Server is not working. Please check the server and try again.")

    def test_set_route(self):
        # Add in S8
        print("Function created for set route")

    def test_select_plan(self):
        # Add in S8
        print("Function created for select plan")

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for fill phone number")

    def test_fill_card(self):
        # Add in S8
        print("Function created for fill card")

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for comment for driver")

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for order blanket and handkerchiefs")

    def test_order_2_ice_creams(self):
        # Add a loop to iterate twice
        print("Function created for order 2 ice creams")
        for i in range(2):
            # Add in S8
            print(f"Ordering ice cream {i + 1}")

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for car search model appears")
