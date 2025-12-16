import heapq

def dijkstra(graph, start):
   
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()
    heap = [(0, start)] 

    while heap:
        current_dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

    return distances
