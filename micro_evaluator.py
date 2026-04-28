"""
MicroAether Evaluator (Phase 2)
Simple scoring system for outputs and performance.
"""

from typing import Any, Dict

class MicroEvaluator:
    __slots__ = ('scores',)

    def __init__(self):
        self.scores: Dict[str, float] = {}

    def evaluate(self, output: Any, criteria: Dict[str, float]) -> float:
        score = sum(criteria.values()) / max(len(criteria), 1)
        key = str(output)[:30]
        self.scores[key] = score
        return score

    def get_average(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)
