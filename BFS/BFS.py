graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def BFS(src, graph):
    queue = []
    visited = []
    queue.append(src)
    
    # loop through queue while it's become empty
    while len(queue) != 0:
        node = queue.pop(0)
        # print the node
        print(node, end=' ')
        # loop through each children of the node
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                queue.append(child)

BFS('5', graph)
