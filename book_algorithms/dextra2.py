graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3
graph['d'] = {}
graph['d']['fin'] = 1
graph['fin'] = {}

infinity = float('inf')

# costs = {}
# parents = {}
# for i, x in enumerate(graph.keys()):
#     for j, y in enumerate(graph[x].keys()):
#         if y in graph.keys():
#             # parents[y] = x
#             costs[y] = graph[x][y]
#     costs['fin'] = infinity

costs = {'a': 5, 'b': 2, 'c': infinity, 'd': infinity, 'fin': infinity}
parents = {'a': 'start', 'b': 'start'}

# print(costs)
# print(parents)
processed = []


def find_lower_cost_node():
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lower_cost_node()
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lower_cost_node()

print(costs)
print(parents)
