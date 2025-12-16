def detect_cycle_and_toposort(graph):

    visited = set()
    rec_stack = set()
    topo_order = []
    parent = {}

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                parent[neighbor] = node
                result = dfs(neighbor)
                if result:  
                    return result
            elif neighbor in rec_stack:
                cycle = [neighbor]
                current = node
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor)
                cycle.reverse()
                return cycle
        rec_stack.remove(node)
        topo_order.append(node)
        return None

    for node in graph:
        if node not in visited:
            result = dfs(node)
            if result:
                return True, result 

    topo_order.reverse()
    return False, topo_order
