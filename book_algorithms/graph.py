from collections import deque

# Поиск в ширину графа.
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']

search_deque = deque()
search_deque += graph['you']

seller = None
processed = []

while search_deque:
    x = search_deque.popleft()
    if x == 'anuj':
        seller = x
    if x not in processed and not seller:
        if x in graph.keys():
            search_deque += graph[x]
            processed.append(x)

print(seller)
