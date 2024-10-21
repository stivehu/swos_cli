import readline

class CLICompleter:
    """
    Handles command autocompletion for the CLI.
    """

    def __init__(self, commands):
        self.commands = commands

    def completer(self, text, state):
        """
        Autocompletion logic based on the given text.
        """
        options = [cmd for cmd in self.commands if cmd.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None

    def enable_autocompletion(self):
        """
        Enables the readline autocompletion with the current command list.
        """
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.completer)
