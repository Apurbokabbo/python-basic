import requests
from helper import helper
baseUrl = "https://restful-booker.herokuapp.com"


class ApiRequests:

    def login(self, username, password):
        api_url = f"{baseUrl}/auth"
        payload = {
            "username": username,
            "password": password
        }
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            print("Stats Code: ", response.status_code)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Login Failed: {e}')
            return None


    def createBooking(self, headers):
        api_url = f"{baseUrl}/booking"
        payload = {
            "firstname": helper.generate_random_first_name(),
            "lastname": helper.generate_random_last_name(),
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            print("Stats Code: ", response.status_code)
            print("Create Booking Response: ", response.text)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f'Create Booking Failed: {e}')
            return None


    def getBooking(self, headers, booking_id):
        api_url = f"{baseUrl}/booking/{booking_id}"
        try:
            response = requests.get(api_url, headers=headers)
            print("Stats Code: ", response.status_code)
            print(f"Get Booking Response: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Get Booking Failed: {e}')
            return None

    def updateBooking(self, headers, booking_id):
        api_url = f"{baseUrl}/booking/{booking_id}"
        payload = {
            "firstname": "Tanzim",
            "lastname": "Emon",
            "totalprice": 1020,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        try:
            response = requests.put(api_url, headers=headers, json=payload)
            print("Stats Code: ", response.status_code)
            print(f"Update Booking Response: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Update Booking Failed: {e}')
            return None

    def deleteBooking(self, headers, booking_id):
        api_url = f"{baseUrl}/booking/{booking_id}"
        try:
            response = requests.delete(api_url, headers=headers)
            print("Stats Code: ", response.status_code)
            print(f"Delete Booking Response: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Delete Booking Failed: {e}')
            return None


if __name__ == "__main__":
    print("------ Start API Testing -------")
    api = ApiRequests()

    print("[Step 1] Authenticating...")
    login_response = api.login("admin", "password123")
    print(login_response)

    if login_response and 'token' in login_response:
        token = login_response['token']
        print(f'Token: {token}')

        auth_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }

        print("[Step 2] Create a New Booking...")
        create_response = api.createBooking(auth_headers)

        if create_response and 'bookingid' in create_response:
            booking_id = create_response['bookingid']
            print(f'Booking ID: {booking_id}')

            print("[Step 3] Fetch Booking details by Id...")
            api.getBooking(auth_headers, booking_id)

            print(f"[Step 4] Update Booking for Id: {booking_id}")
            print("Headers: ", auth_headers)
            api.updateBooking(auth_headers, booking_id)

            print("[Step 5] Delete Booking...")
            api.deleteBooking(auth_headers, booking_id)

            print("[Step 6] Verify After Delete the Booking...")
            api.getBooking(auth_headers, booking_id)
        else:
            print("Failed to Create Booking")

    else:
        print("Failed to Authenticate")