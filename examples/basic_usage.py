# examples/basic_usage.py

import networkx as nx

from iterated_graph_systems import (
    Edge_Iterated_Graph_Systems,
    draw_IGS,
)


def main():
    # Define substitution rules (example)
    rules_graphs = {
        "blue": {
            "planting": ("start", "end"),
            "edge_list": [
                ("start", "A", "blue"),
                ("A", "B", "red"),
                ("B", "end", "blue"),
                ("start", "C", "red"),
                ("C", "end", "red"),
            ],
        },
        "red": {
            "planting": ("start", "end"),
            "edge_list": [
                ("B", "start", "red"),
                ("C", "B", "red"),
                ("C", "D", "red"),
                ("E", "D", "red"),
                ("end", "E", "blue"),
                ("start", "F", "blue"),
                ("G", "F", "blue"),
                ("H", "G", "blue"),
                ("H", "I", "blue"),
                ("I", "end", "red"),
            ],
        },
    }

    # Build an IGS with initial blue edge and 3 iterations
    G = Edge_Iterated_Graph_Systems(
        rules_graphs=rules_graphs,
        initial_colour="blue",
        iterations=3,
        direction="off",
        colour="on",
    )

    # Compute a layout externally
    layout = nx.spring_layout(G, scale=2)

    # Draw the resulting IGS
    draw_IGS(G, layout, direction="off", colour="on")


if __name__ == "__main__":
    main()
