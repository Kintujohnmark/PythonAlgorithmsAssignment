import networkx as nx

graph = nx.DiGraph()


graph.add_edge('S', 'A', weight=3)
graph.add_edge('S', 'B', weight=1)
graph.add_edge('A', 'S', weight=3)
graph.add_edge('A', 'B', weight=2)
graph.add_edge('A', 'C', weight=2)
graph.add_edge('B', 'S', weight=1)
graph.add_edge('B', 'A', weight=2)
graph.add_edge('B', 'C', weight=3)
graph.add_edge('C', 'A', weight=2)
graph.add_edge('C', 'B', weight=3)
graph.add_edge('C', 'D', weight=4)
graph.add_edge('C', 'G', weight=4)
graph.add_edge('D', 'C', weight=4)
graph.add_edge('D', 'G', weight=1)
graph.add_edge('G', 'C', weight=4)
graph.add_edge('G', 'D', weight=1)


heuristics = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

for node in graph.nodes():
    print(f'Node: {node}, Heuristic: {heuristics[node]}')
    for neighbor in graph.neighbors(node):
        cost = graph.get_edge_data(node, neighbor)['weight']
        print(f'  Neighbor node: {neighbor}, Cost: {cost}')


