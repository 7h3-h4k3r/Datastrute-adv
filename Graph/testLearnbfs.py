from collections import deque

# Graph as dictionary (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start, target):
    visited = set()          # Track visited nodes
    queue = deque([[start]]) # Queue holds paths, not just nodes
    while queue:
        path = queue.popleft()  
        print(path)   # Remove first path
        node = path[-1]            # Last node in path
        
        if node == target:         # Found target
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)   
    return None  # No path found

# Example usage
result = bfs(graph, 'A', 'F')
print("Shortest path:", result)
