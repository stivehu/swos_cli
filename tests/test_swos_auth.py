# test_swos_auth.py

import os
import pytest
from controllers.swos_controller import SwOSController
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@pytest.fixture
def swos_controller():
    # Load real data from environment variables
    ip_address = os.getenv("SWOS_IP")
    username = os.getenv("SWOS_USERNAME")
    password = os.getenv("SWOS_PASSWORD")

    # Initialize the SwOSController class
    return SwOSController(ip_address, username, password)


def test_authentication(swos_controller):
    # Test if authentication is successful
    assert swos_controller.authenticate() == True, "Authentication failed"


def test_show_ports(swos_controller):
    # Test if port information can be retrieved
    try:
        swos_controller.show_ports()
        assert True  # Test passes if no exceptions occur
    except Exception as e:
        pytest.fail(f"Failed to fetch ports: {e}")
