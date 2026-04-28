"""
MicroAether Interactive REPL (Phase 3)
Safe, simple Read-Eval-Print Loop.
"""

from typing import Any
import ast

class MicroREPL:
    __slots__ = ('history', 'globals')

    def __init__(self):
        self.history: list = []
        self.globals: dict = {}

    def execute(self, code: str) -> Any:
        try:
            # Safe evaluation using ast.literal_eval for expressions
            result = ast.literal_eval(code)
            self.history.append((code, result))
            return result
        except Exception as e:
            error = f"Error: {e}"
            self.history.append((code, error))
            return error

    def run_interactive(self):
        print("MicroREPL v0.1 (type 'exit' to quit)")
        while True:
            try:
                code = input(">>> ")
                if code.lower() in ['exit', 'quit']:
                    break
                result = self.execute(code)
                print(result)
            except KeyboardInterrupt:
                break
        print("Goodbye!")
