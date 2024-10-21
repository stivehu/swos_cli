from controllers.swos_controller import SwOSController
from completer import CLICompleter
from arg_parser import ArgumentParser

# Available commands
COMMANDS = [
    'show mac address-table all',
    'show mac address-table count',
    'show mac address-table vlan',
    'show mac address-table mac',
    'show mac address-table interface',
    'exit'
]

def main():
    # Parse command-line arguments
    arg_parser = ArgumentParser()
    args = arg_parser.parse_args()

    # Initialize the SwOS controller with the provided or prompted credentials
    ip_address = args.ip
    username = args.username if args.username else input("Enter username: ")
    password = args.password if args.password else input("Enter password: ")

    controller = SwOSController(ip_address, username, password)

    # If a command is passed, execute it and exit
    if args.command:
        execute_command(controller, args.command)
        return

    # Enable autocompletion
    cli_completer = CLICompleter(COMMANDS)
    cli_completer.enable_autocompletion()

    # Interactive CLI loop
    while True:
        command = input(f"{username}@{ip_address}> ")

        if command == "exit":
            break
        elif command.startswith("show mac address-table"):
            process_mac_command(controller, command)
        else:
            print("Unknown command")

def execute_command(controller, command):
    """
    Executes a single command and exits the program.
    """
    if command.startswith("show mac address-table"):
        process_mac_command(controller, command)
    else:
        print(f"Unknown command: {command}")

def process_mac_command(controller, command):
    """
    Processes the show mac address-table commands with modes like all, count, vlan, mac, and interface.
    """
    command_parts = command.split()

    if len(command_parts) == 4:
        mode = command_parts[-1]
        controller.mac_address_table_controller.show_mac_address_table(mode)
    elif len(command_parts) == 5:
        mode = command_parts[-2]
        param = command_parts[-1]

        if mode == "vlan" and param.isdigit():
            vlan = int(param)
            controller.mac_address_table_controller.show_mac_address_table(mode="vlan", vlan=vlan)
        elif mode == "mac":
            mac = param
            controller.mac_address_table_controller.show_mac_address_table(mode="mac", mac=mac)
        elif mode == "interface":
            interface = param
            controller.mac_address_table_controller.show_mac_address_table(mode="interface", interface=interface)
        else:
            print("Invalid parameters for show mac address-table")
    else:
        controller.mac_address_table_controller.show_mac_address_table(mode="all")

if __name__ == "__main__":
    main()
