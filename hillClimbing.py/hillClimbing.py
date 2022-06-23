from collections import defaultdict

graph = defaultdict(list)
graph[('A', 5)].append(('B', 2))
graph[('A', 5)].append(('C', 3))
graph[('B', 2)].append(('D', 2))
graph[('B', 2)].append(('E', 3))
graph[('C', 3)].append(('F', 2))
graph[('C', 3)].append(('G', 4))
graph[('D', 2)].append(('H', 1))
graph[('D', 2)].append(('I', 99))
graph[('F', 2)].append(('J', 99))
graph[('G', 4)].append(('K', 99))
graph[('G', 4)].append(('L', 3))


def MOV(node, graph):
    _list = []
    if len(graph[node]) == 0:
        return -1
    for tup in graph[node]:
        _list.append(tup)
    return _list

def SORT(_list: list):
    _list.sort(key= lambda x: x[1])

def HEU(node):
    return node[1]

def hillClimb(start, graph):
    path = []
    node = start
    new_nodes = MOV(node, graph)
    SORT(new_nodes)
    child = new_nodes[0]
    path.append(start)
    path.append(child)

    while HEU(child) <= HEU(node):
        node = child
        new_nodes = MOV(node, graph)
        if new_nodes == -1:
            return path
        SORT(new_nodes)
        child = new_nodes[0]
        path.append(child)

    return path

print(hillClimb(('A', 5), graph))
