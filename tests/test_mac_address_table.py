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


def test_show_mac_address_table_all(swos_controller):
    """
    Test the 'show mac address-table all' command with live data.
    """
    # Test if MAC address table can be retrieved and displayed correctly
    swos_controller.mac_address_table_controller.show_mac_address_table("all")


def test_show_mac_address_table_count(swos_controller):
    """
    Test the 'show mac address-table count' command with live data.
    """
    swos_controller.mac_address_table_controller.show_mac_address_table("count")
