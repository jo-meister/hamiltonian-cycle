# Joey Walker
import time
import sys
from itertools import permutations


def hamiltonian_cycle(graph):
    n = len(graph)

    # Generate all possible paths.
    paths = permutations(range(n))

    # Check if each path is a Hamiltonian cycle.
    for path in paths:
        if verify_hamiltonian_cycle(graph, path):
            return list(path)
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


print('Brute force hamiltonian cycle')
start = time.time()
cycle = hamiltonian_cycle(adj_matrix)
if cycle is not None:
    print("Hamiltonian cycle found:")
    print([v + 1 for v in cycle + [cycle[0]]])
else:
    print("No Hamiltonian cycle exists")
end = time.time()
print(f'Run time {end - start}')
