"""
MicroAether Memory System
Lightweight persistent memory with search.
"""

import json
import os
import time
from typing import Any, Dict, List, Optional

class MicroMemory:
    __slots__ = ('path', 'data')

    def __init__(self, path: str = "micro_memory.json"):
        self.path = path
        self.data: Dict[str, Dict] = {}
        if os.path.exists(path):
            with open(path, "r") as f:
                self.data = json.load(f)

    def store(self, key: str, value: Any, tags: Optional[List[str]] = None):
        self.data[key] = {
            "value": value,
            "timestamp": time.time(),
            "tags": tags or []
        }
        self._save()

    def recall(self, key: str) -> Any:
        return self.data.get(key, {}).get("value")

    def search(self, query: str) -> List[Dict]:
        results = []
        q = query.lower()
        for key, entry in self.data.items():
            if q in key.lower() or q in str(entry.get("value", "")).lower():
                results.append({"key": key, **entry})
        return results

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

# Global instance
memory = MicroMemory()
