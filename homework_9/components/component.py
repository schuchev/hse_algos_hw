def find_connected_components(graph):
    
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)
    
    isolated_nodes = set(graph.keys()) - visited
    for node in isolated_nodes:
        components.append({node})
    
    return components
