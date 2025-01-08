import time
import json
from selenium.common.exceptions import WebDriverException


def retrieve_phone_code(driver) -> str:
    """Retrieve the phone confirmation code from WebDriver's performance logs.

    The phone confirmation code can only be obtained after the application has
    requested the code via an API call.
    """
    code = None
    for i in range(10):  # Retry a few times
        try:
            # Extract the performance log and search for relevant messages
            logs = [log["message"] for log in driver.get_log('performance')
                    if 'api/v1/number?number' in log.get("message", "")]

            # If there are matching logs, extract the confirmation code
            if logs:
                for log in reversed(logs):
                    try:
                        message_data = json.loads(log)["message"]
                        request_id = message_data["params"].get("requestId")
                        body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                        # Extract digits from response body
                        code = ''.join([x for x in body['body'] if x.isdigit()])

                        if code:
                            print(f"Code found: {code}")  # Debugging line
                            return code
                    except json.JSONDecodeError as e:
                        print(f"Failed to decode log: {e}")
                    except KeyError as e:
                        print(f"Missing expected key in log: {e}")

        except WebDriverException as e:
            print(f"WebDriver error: {e}")
            time.sleep(1)  # Wait before retrying

    if not code:
        raise Exception("No phone confirmation code found.\n"
                        "Make sure retrieve_phone_code is only called after the code is requested in the application.")
    return code


# Checks if Routes is up and running. Do not change
def is_url_reachable(url: str) -> bool:
    """Check if the URL can be reached. Pass the URL for Urban Routes as a parameter.
    If it can be reached, returns True. Otherwise, returns False."""

    import ssl
    import urllib.request

    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            if response.status == 200:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error while checking URL: {e}")

    return False
