"""
MicroAether Multi-Agent System (Phase 2)
Simple agent orchestration with blackboard.
"""

from typing import Any, Dict, List
from .agent import MicroAgent, agents

class MicroOrchestrator:
    __slots__ = ('blackboard',)

    def __init__(self):
        self.blackboard: Dict[str, Any] = {}

    def post(self, key: str, value: Any):
        self.blackboard[key] = value

    def get(self, key: str) -> Any:
        return self.blackboard.get(key)

    def route(self, task: str, capability: str) -> str:
        for name, agent in agents.items():
            if agent.can(capability):
                return name
        return "default"

    def run_task(self, task: str, capability: str = "general") -> str:
        agent_name = self.route(task, capability)
        agent = agents.get(agent_name)
        if agent:
            return agent.act(task)
        return f"No agent found for capability: {capability}"
