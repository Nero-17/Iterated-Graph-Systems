# Iterated Graph Systems

This repository implements **edge-based Iterated Graph Systems (IGS)** in the setting of finite graphs, together with simple visualisation tools and a bond percolation demo.

The core idea:

- Start from a single coloured edge.
- For each edge colour, specify a **rule graph** describing how an edge of that colour is replaced.
- Iteratively substitute each edge by its rule graph, identifying the endpoints of the rule with the endpoints of the edge.
- Optionally convert the resulting directed graph to an undirected one and run percolation experiments on top.

The library is intended for experimentation and visual exploration of iterated graph constructions.

---

## Installation

At the moment the package is distributed directly from GitHub:

```bash
pip install git+https://github.com/Nero-17/iterated-graph-systems.git
