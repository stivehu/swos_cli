import argparse

class ArgumentParser:
    """
    Handles command-line argument parsing for the SwOS CLI.
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="MikroTik SwOS CLI")

        # Add possible arguments
        self.parser.add_argument("ip", help="SwOS device IP address")
        self.parser.add_argument("--username", help="Username for SwOS", required=False)
        self.parser.add_argument("--password", help="Password for SwOS", required=False)
        self.parser.add_argument("--command", help="Command to execute and exit", required=False)

    def parse_args(self):
        """
        Parse and return the arguments from the command line.
        """
        return self.parser.parse_args()
