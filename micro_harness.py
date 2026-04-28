"""
MicroAether Harness (Phase 3)
Simple testing and execution harness.
"""

from typing import Any, Callable, Dict

class MicroHarness:
    __slots__ = ('results',)

    def __init__(self):
        self.results: Dict[str, Dict] = {}

    def run_test(self, name: str, func: Callable) -> Dict:
        try:
            result = func()
            self.results[name] = {"status": "pass", "result": result}
            return self.results[name]
        except Exception as e:
            self.results[name] = {"status": "fail", "error": str(e)}
            return self.results[name]

    def get_summary(self) -> Dict:
        total = len(self.results)
        passed = sum(1 for r in self.results.values() if r["status"] == "pass")
        return {
            "total": total,
            "passed": passed,
            "failed": total - passed,
            "success_rate": passed / total if total > 0 else 0
        }
