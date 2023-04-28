# Joey Walker
import time
import sys


def hamiltonian_cycle(graph):
    n = len(graph)
    path = [0]
    visited = set([0])

    while len(path) < n:
        next = None
        min = n
        for i, v in enumerate(graph[path[-1]]):
            if v == 1 and i not in visited:
                # Get the number of edges of the current node.
                cur = sum(graph[i])
                if cur < min:
                    min = cur
                    next = i
        if next is None:
            break
        # Add the adjacent vertex with the least number of edges to the path.
        path.append(next)
        visited.add(next)

    # Verify the path is a hamiltonian cycle.
    if len(path) == n and verify_hamiltonian_cycle(graph, path):
        return path
    else:
        return None


def verify_hamiltonian_cycle(graph, path):
    n = len(graph)

    # Verify the path is a cycle.
    if graph[path[0]][path[n-1]] == 0:
        return False

    # Verify that there is an edge between each vertex.
    for i in range(n-1):
        if graph[path[i]][path[i+1]] == 0:
            return False

    return True


# Read from file.
file = open(sys.argv[1])
problem_name = file.readline()
num_nodes = file.readline()
lines = file.readlines()
file.close()

# Create graph.
n = int(num_nodes)
adj_matrix = [[0] * n for _ in range(n)]

# Parse input text
for line in lines:
    if line[0] == "$":
        break
    a, b, weight = list(map(int, line.split(' ')))
    adj_matrix[a-1][b-1] = weight
    adj_matrix[b-1][a-1] = weight

print('Heuristic hamiltonian cycle')
start = time.time()
cycle = hamiltonian_cycle(adj_matrix)
if cycle is not None:
    print("Hamiltonian cycle found:")
    print([v + 1 for v in cycle + [cycle[0]]])
else:
    print("No Hamiltonian cycle exists")
end = time.time()
print(f'Run time {end - start}')
