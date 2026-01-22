# iterated_graph_systems/__init__.py

from .igs import (
    Edge_Iterated_Graph_Systems,
    draw_IGS,
    draw_bond_percolation,
    substitute_edge,
    count_new_vertices_in_rule,
)

__all__ = [
    "Edge_Iterated_Graph_Systems",
    "draw_IGS",
    "draw_bond_percolation",
    "substitute_edge",
    "count_new_vertices_in_rule",
]

# 可选：如果你想在包里暴露版本号（装了以后才准）
try:
    from importlib.metadata import version as _version
    __version__ = _version("iterated-graph-systems")
except Exception:
    __version__ = "0.0.0"
