graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def DFS(src, graph):
    stack = []
    visited = []
    stack.append(src)
    
    # loop through stack while it's become empty
    while len(stack) != 0:
        node = stack.pop()
        # print the node
        print(node, end=' ')
        # loop through each children of the node
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                stack.append(child)

DFS('5', graph)