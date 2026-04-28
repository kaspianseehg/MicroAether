"""
MicroAether Tools (Phase 3 - Partial)
Only the most useful lightweight tools.
"""

from typing import Any, Callable, Dict

class MicroTools:
    __slots__ = ('tools',)

    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        self.tools[name] = func

    def call(self, name: str, *args, **kwargs) -> Any:
        if name in self.tools:
            return self.tools[name](*args, **kwargs)
        return f"Tool '{name}' not found"

    def list_tools(self) -> list:
        return list(self.tools.keys())

# Pre-register some basic tools
tools = MicroTools()
tools.register("add", lambda a, b: a + b)
tools.register("multiply", lambda a, b: a * b)
tools.register("upper", lambda s: str(s).upper())
