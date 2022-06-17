graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['9'],
    '8': ['10']
}

def iterativeDDFS(src, target, graph, maxdeepth):
    for i in range(maxdeepth):
        if DFS(src, target, graph, i):
            return True
    return False

def DFS(src, target, graph, maxdeepth):
    if src == target:
        return True
    if maxdeepth <= 0:
        return False
    
    for node in graph[src]:
        if DFS(node, target, graph, maxdeepth - 1):
            return True
    return False

print(iterativeDDFS('5', '10', graph, 4))