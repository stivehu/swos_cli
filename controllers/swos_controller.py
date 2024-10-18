import requests
from requests.auth import HTTPDigestAuth

class SwOSController:
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.base_url = f"http://{self.ip_address}"
        self.auth = HTTPDigestAuth(self.username, self.password)

        if self.authenticate():
            print("Authentication successful")
        else:
            print("Authentication failed")

    def authenticate(self):
        try:
            response = requests.get(f"{self.base_url}/fan.b", auth=self.auth)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.RequestException as e:
            print(f"Error during authentication: {e}")
            return False

    # Például itt kérdezhetjük le a portokat
    def show_ports(self):
        try:
            response = requests.get(f"{self.base_url}/ports", auth=self.auth)
            if response.status_code == 200:
                print(response.json())  # Vagy a megfelelő formátum szerint dolgozzuk fel
            else:
                print(f"Failed to retrieve ports: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching ports: {e}")
