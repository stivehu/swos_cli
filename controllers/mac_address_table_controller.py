import json
import requests
from requests.auth import HTTPDigestAuth
import re

class MacAddressTableController:
    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth

    def fix_invalid_json(self, data):
        """
        Convert invalid JSON format to valid JSON by replacing single quotes with double quotes,
        and ensuring both keys and values are wrapped in double quotes.
        """
        fixed_data = re.sub(r"\'", "\"", data)  # Replace single quotes with double quotes
        fixed_data = re.sub(r"(\w+):", r'"\1":', fixed_data)  # Wrap keys in double quotes
        fixed_data = re.sub(r'(?<=:)"?(\w+)"?(?=,|})', r'"\1"', fixed_data)  # Wrap values in double quotes
        return fixed_data

    def format_mac_address(self, mac):
        """
        Format MAC address to the standard form 00:18:ae:98:3c:21.
        """
        return ":".join(mac[i:i+2] for i in range(0, len(mac), 2))

    def get_mac_address_table(self):
        """
        Fetch MAC address table data from the '!dhost.b' file and convert it into valid JSON.
        """
        try:
            response = requests.get(f"{self.base_url}/!dhost.b", auth=self.auth)
            if response.status_code == 200:
                data = response.text
                fixed_data = self.fix_invalid_json(data)  # Fix the JSON structure
                return json.loads(fixed_data)
            else:
                print(f"Failed to retrieve MAC address table: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error fetching MAC address table: {e}")
            return None

    def show_mac_address_table(self, mode="all", vlan=None, mac=None,interface=None):
        """
        Display MAC address table based on the mode provided.
        Modes: 'all', 'count', 'interface', 'mac', 'vlan'.
        Filtering is supported for VLAN and MAC address.
        """
        mac_table = self.get_mac_address_table()
        if mac_table is None:
            return

        if mode == "all":
            for entry in mac_table:
                formatted_mac = self.format_mac_address(entry['adr'])
                print(f"MAC: {formatted_mac} | VLAN: {int(entry['vid'], 16)} | Port: {int(entry['prt'], 16)+1}")
        elif mode == "count":
            print(f"Total MAC Addresses: {len(mac_table)}")
        elif mode == "vlan":
            # Filter by VLAN
            if vlan is not None:
                for entry in mac_table:
                    if int(entry['vid'], 16) == vlan:
                        formatted_mac = self.format_mac_address(entry['adr'])
                        print(f"MAC: {formatted_mac} | VLAN: {vlan} | Port: {int(entry['prt'], 16)+1}")
        elif mode == "mac":
            # Filter by MAC address
            if mac is not None:
                # Normalize MAC by removing delimiters (colons and dashes)
                normalized_mac = re.sub(r'[:-]', '', mac).lower()
                for entry in mac_table:
                    entry_mac = entry['adr'].lower()
                    if entry_mac == normalized_mac:
                        formatted_mac = self.format_mac_address(entry['adr'])
                        print(f"MAC: {formatted_mac} | VLAN: {int(entry['vid'], 16)} | Port: {int(entry['prt'], 16)+1}")
        elif mode == "interface":
            # Filter by interface

            if interface is not None:
                for entry in mac_table:
                    if int(entry['prt'], 16)+1 == int(interface):
                        formatted_mac = self.format_mac_address(entry['adr'])
                        print(f"MAC: {formatted_mac} | VLAN: {int(entry['vid'], 16)} | Port: {int(entry['prt'], 16)+1}")
        else:
            print("Unknown mode")
