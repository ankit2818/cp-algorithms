def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)
    while len(queue):
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return visited


if __name__ == "__main__":
    graph = {
        '0': ['1', '2'],
        '1': ['0', '3', '4'],
        '2': ['0'],
        '3': ['1'],
        '4': ['2', '3']
    }
    visited = bfs(graph, '0')
    print(visited)