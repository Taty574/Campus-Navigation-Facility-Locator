from data_structures.graph import Graph

def build_campus_graph():
    g = Graph()
    g.add_edge("Gate A", "Central building", 1)
    g.add_edge("Central building", "Chapel A", 2)
    g.add_edge("Chapel A", "B", 5)
    g.add_edge("B", "Law building", 3)
    g.add_edge("Law building", "SBS", 2)
    g.add_edge("Law building", "STC", 3)
    g.add_edge("STC", "B", 2)
    g.add_edge("STC", "STMB", 3)
    g.add_edge("B", "Main auditorium", 4)
    g.add_edge("B", "Lib", 3)
    g.add_edge("Lib", "Medical centre", 4)
    g.add_edge("Lib", "Oval building", 3)
    g.add_edge("Oval building", "MSB", 2)
    g.add_edge("MSB", "Forge", 4)
    return g