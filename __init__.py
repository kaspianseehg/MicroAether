"""
MicroAether v0.1
The efficient, minimal version of AETHER.

Core philosophy (inspired by Karpathy's MicroGPT):
"The core algorithm should be small. Everything else is just efficiency."
"""

from .core.micro_aether import BalancedTernary, MicroVM, MicroImprove, memory
from .memory import MicroMemory
from .cli import MicroCLI, cli
from .agent import MicroAgent, register_agent, get_agent
from .micro_agents import MicroOrchestrator
from .micro_improve import MicroImprove as ImproveLoop
from .micro_repl import MicroREPL
from .micro_harness import MicroHarness
from .micro_tools import MicroTools, tools
from .utils import timer, cached, log

__version__ = "0.1.0"
__all__ = [
    "BalancedTernary", "MicroVM", "MicroImprove", "memory",
    "MicroMemory", "MicroCLI", "cli",
    "MicroAgent", "register_agent", "get_agent",
    "MicroOrchestrator", "ImproveLoop",
    "MicroREPL", "MicroHarness", "MicroTools", "tools",
    "timer", "cached", "log"
]
