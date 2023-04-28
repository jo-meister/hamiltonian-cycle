
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

# Parse input text
edges = []
for line in lines:
    if line[0] == "$":
        break
    a, b, weight = list(map(int, line.split(' ')))
    edges.append((a, b))

vertices = [0] * n
first = [0] * n
primes = [0] * n
n = len(edges)
k = 3
adj_matrix = [[0] * (n * 12 + k) for _ in range((n * 12) + k)]
for edge in range(n):
    if vertices[edges[edge][0]] == 0:
        vertices[edges[edge][0]] = 1
        first[edges[edge][0]] = 12*edge + k
        primes[edges[edge][0]] = 12*edge + k + 5
    else:
        adj_matrix[primes[edges[edge][0]]][12*edge+k] = 1
        adj_matrix[12*edge+k][primes[edges[edge][0]]] = 1
        primes[edges[edge][0]] = 12*edge + k + 5
    if vertices[edges[edge][1]] == 0:
        vertices[edges[edge][1]] = 1
        first[edges[edge][1]] = 12*edge + k + 6
        primes[edges[edge][1]] = 12*edge + k + 11
    else:
        adj_matrix[primes[edges[edge][1]]][12*edge+k+6] = 1
        adj_matrix[12*edge+k+6][primes[edges[edge][1]]] = 1
        primes[edges[edge][1]] = 12*edge + k + 11
    edge = 12 * edge
    adj_matrix[edge+k][edge+k+1] = 1
    adj_matrix[edge+k][edge+k+8] = 1
    adj_matrix[edge+k+1][edge+k] = 1
    adj_matrix[edge+k+1][edge+k+2] = 1
    adj_matrix[edge+k+2][edge+k+1] = 1
    adj_matrix[edge+k+2][edge+k+3] = 1
    adj_matrix[edge+k+2][edge+k+6] = 1
    adj_matrix[edge+k+3][edge+k+2] = 1
    adj_matrix[edge+k+3][edge+k+4] = 1
    adj_matrix[edge+k+3][edge+k+11] = 1
    adj_matrix[edge+k+4][edge+k+3] = 1
    adj_matrix[edge+k+4][edge+k+5] = 1
    adj_matrix[edge+k+5][edge+k+4] = 1
    adj_matrix[edge+k+5][edge+k+9] = 1
    adj_matrix[edge+k+6][edge+k+2] = 1
    adj_matrix[edge+k+6][edge+k+7] = 1
    adj_matrix[edge+k+7][edge+k+6] = 1
    adj_matrix[edge+k+7][edge+k+8] = 1
    adj_matrix[edge+k+8][edge+k+7] = 1
    adj_matrix[edge+k+8][edge+k] = 1
    adj_matrix[edge+k+8][edge+k+9] = 1
    adj_matrix[edge+k+9][edge+k+8] = 1
    adj_matrix[edge+k+9][edge+k+5] = 1
    adj_matrix[edge+k+9][edge+k+10] = 1
    adj_matrix[edge+k+10][edge+k+9] = 1
    adj_matrix[edge+k+10][edge+k+11] = 1
    adj_matrix[edge+k+11][edge+k+10] = 1
    adj_matrix[edge+k+11][edge+k+3] = 1

for selector in range(k):
    for v in first:
        adj_matrix[selector][v] = 1
        adj_matrix[v][selector] = 1
    for v_ in primes:
        adj_matrix[selector][v_] = 1
        adj_matrix[v_][selector] = 1

print('Vertex Cover to Hamiltonian Cycle')
cycle = hamiltonian_cycle(adj_matrix)
if cycle is not None:
    print(f'A vertex cover of size {k} exists')
else:
    print(f'There is no vertex cover of size {k}')