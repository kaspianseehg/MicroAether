"""
MicroAether Agent System
Lightweight agent with basic capabilities.
"""

from typing import Any, Callable, Dict, List
from dataclasses import dataclass

@dataclass
class MicroAgent:
    __slots__ = ('name', 'role', 'capabilities', 'state')

    name: str
    role: str
    capabilities: List[str]
    state: Dict[str, Any]

    def can(self, capability: str) -> bool:
        return capability in self.capabilities

    def act(self, task: str) -> str:
        return f"[{self.name}] Executed: {task}"

# Simple registry
agents: Dict[str, MicroAgent] = {}

def register_agent(agent: MicroAgent):
    agents[agent.name] = agent

def get_agent(name: str) -> MicroAgent:
    return agents.get(name)
