# MicroAether v0.1

**The most efficient, minimal version of AETHER possible.**

Inspired by Karpathy's MicroGPT philosophy:

> *"The core algorithm should be small. Everything else is just efficiency."*

---

## Features

- **Ternary Core** — `BalancedTernary` with `__slots__` for memory efficiency
- **Lightweight Self-Improvement** — `MicroImprove` with early stopping
- **Multi-Agent Orchestration** — Simple blackboard + capability routing
- **Goal Decomposition** — Hierarchical goal breaking
- **Knowledge Base** — Searchable persistent memory
- **Interactive REPL** — Safe execution environment
- **Testing Harness** — Run and evaluate tests
- **Tool Registry** — Lightweight function calling
- **Zero Heavy Dependencies** — Pure Python

---

## Quick Start

```bash
cd MicroAether
python -m core.micro_aether demo
```

Or import as a package:

```python
from MicroAether import BalancedTernary, MicroImprove, memory

a = BalancedTernary("102")
print(int(a))  # 8

improver = MicroImprove()
result = improver.run(object())
print(result)
```

---

## Project Structure

```
MicroAether/
├── core/
│   └── micro_aether.py      # Main single-file core
├── memory.py
├── cli.py
├── agent.py
├── utils.py
├── micro_improve.py
├── micro_agents.py
├── micro_goals.py
├── micro_knowledge.py
├── micro_evaluator.py
├── micro_repl.py
├── micro_harness.py
├── micro_tools.py
├── __init__.py
└── README.md
```

**Total:** ~13 files, under 15KB — Extremely lean.

---

## Philosophy

This project follows the **MicroGPT mindset**:

- Keep the **core small**
- Use **`__slots__`** everywhere possible
- Prefer **pure Python** over heavy libraries
- Add complexity **only when it gives clear value**
- Maintain **readability** and **efficiency**

---

## License

Experimental / Research Use

---

*Built with love for minimal, efficient AI systems.*
