"""
MicroAether CLI
Clean command line interface.
"""

import sys
from typing import Callable, Dict

class MicroCLI:
    __slots__ = ('commands',)

    def __init__(self):
        self.commands: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        self.commands[name] = func

    def run(self, args: list = None):
        if args is None:
            args = sys.argv[1:]

        if not args:
            self._show_help()
            return

        cmd = args[0]
        if cmd in self.commands:
            self.commands[cmd](args[1:])
        else:
            print(f"Unknown command: {cmd}")
            self._show_help()

    def _show_help(self):
        print("MicroAether v0.1")
        print("Commands:", ", ".join(self.commands.keys()))

# Global CLI instance
cli = MicroCLI()
