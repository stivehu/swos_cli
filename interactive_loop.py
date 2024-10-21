from cli.completer import CLICompleter

class InteractiveCLI:
    """
    Handles the interactive command loop.
    """

    def __init__(self, controller, commands):
        self.controller = controller
        self.commands = commands

    def run(self, username, ip_address):
        """
        Run the interactive CLI loop.
        """
        cli_completer = CLICompleter(self.commands)
        cli_completer.enable_autocompletion()

        while True:
            command = input(f"{username}@{ip_address}> ")

            if command == "exit":
                break
            elif command.startswith("show mac address-table"):
                # Delegate command processing to the controller
                self.controller.mac_address_table_controller.show_mac_address_table(command)
            else:
                print("Unknown command")
