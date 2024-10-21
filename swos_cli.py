import readline
from controllers.swos_controller import SwOSController

COMMANDS = [
    'show mac address-table all',
    'show mac address-table count',
    'show mac address-table vlan',
    'show mac address-table mac',
    'show mac address-table interface',
    'exit'
]

def completer(text, state):
    """
    Autocompletion logic for the CLI.
    """
    options = [cmd for cmd in COMMANDS if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def main():
    print("Welcome to MikroTik SwOS CLI")

    # Enable autocompletion
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)

    # Prompt for authentication details
    ip_address = input("Enter SwOS IP address: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Initialize the SwOS controller with DigestAuth
    controller = SwOSController(ip_address, username, password)

    while True:
        # Get command input from the user
        command = input(f"{username}@{ip_address}> ")

        if command == "exit":
            break
        elif command.startswith("show mac address-table"):
            # Extract mode (all, count, vlan, mac, interface) and any parameters
            command_parts = command.split()

            # Determine the mode and possible parameters
            if len(command_parts) == 4:
                mode = command_parts[-1]
                controller.mac_address_table_controller.show_mac_address_table(mode)
            elif len(command_parts) == 5:
                mode = command_parts[-2]
                param = command_parts[-1]

                # VLAN mode
                if mode == "vlan" and param.isdigit():
                    vlan = int(param)
                    controller.mac_address_table_controller.show_mac_address_table(mode="vlan", vlan=vlan)

                # MAC mode (accepts both colon and dash-separated formats)
                elif mode == "mac":
                    mac = param
                    controller.mac_address_table_controller.show_mac_address_table(mode="mac", mac=mac)

                # Interface mode
                elif mode == "interface":
                    interface = param
                    controller.mac_address_table_controller.show_mac_address_table(mode="interface", interface=interface)
                else:
                    print("Invalid parameters for show mac address-table")
            else:
                # Default mode is 'all'
                controller.mac_address_table_controller.show_mac_address_table(mode="all")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
