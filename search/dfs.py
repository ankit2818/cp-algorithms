def dfs(graph, start, visited = []):
    if start in visited:
        return
    visited.append(start)
    for node in graph[start]:
        dfs(graph, node, visited)
    return visited


if __name__ == "__main__":
    graph = {
        '0': ['1', '2'],
        '1': ['0', '3', '4'],
        '2': ['0'],
        '3': ['1'],
        '4': ['2', '3']
    }
    visited = dfs(graph, '0')
    print(visited)