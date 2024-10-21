from requests.auth import HTTPDigestAuth
from controllers.mac_address_table_controller import MacAddressTableController

class SwOSController:
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.base_url = f"http://{self.ip_address}"
        self.auth = HTTPDigestAuth(self.username, self.password)

        # Initialize MacAddressTableController
        self.mac_address_table_controller = MacAddressTableController(self.base_url, self.auth)

    def authenticate(self):
        """
        Authenticate by attempting to retrieve the 'sys.b' file from the SwOS device.
        If the file can be fetched successfully, authentication is considered successful.
        """
        try:
            response = requests.get(f"{self.base_url}/sys.b", auth=self.auth)
            if response.status_code == 200 and response.text:
                return True
            return False
        except requests.RequestException as e:
            print(f"Error during authentication: {e}")
            return False
