"""
MicroAether Knowledge Base (Phase 2)
Simple key-value knowledge with search.
"""

from typing import Any, Dict, List
import time

class MicroKnowledge:
    __slots__ = ('store',)

    def __init__(self):
        self.store: Dict[str, Dict] = {}

    def remember(self, key: str, value: Any, confidence: float = 1.0):
        self.store[key] = {
            "value": value,
            "timestamp": time.time(),
            "confidence": confidence
        }

    def recall(self, key: str) -> Any:
        return self.store.get(key, {}).get("value")

    def search(self, query: str) -> List[Dict]:
        results = []
        q = query.lower()
        for key, entry in self.store.items():
            if q in key.lower() or q in str(entry.get("value", "")).lower():
                results.append({"key": key, **entry})
        return results
