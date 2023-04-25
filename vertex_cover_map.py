import time


def hamiltonian_cycle(graph):
    # Initialize variables.
    n = len(graph)
    stack = [(i, [i]) for i in range(n)]

    # Traverse graph using DFS.
    while stack:
        (node, path) = stack.pop()
        # Check if path is Hamiltonian cycle.
        if len(path) == n and graph[path[-1]][path[0]] == 1:
            return path
        # Add unvisited neighbors to stack.
        for neighbor in range(n):
            if neighbor not in path and graph[node][neighbor] == 1:
                stack.append((neighbor, path + [neighbor]))
    # If no Hamiltonian cycle is found, return None
    return None


# Read from file.
file = open("datafiles/vertex_cover2.dat")
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
k = 1
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

with open('graph.txt', 'w') as f:
    for i in range(len(adj_matrix)):
        f.write(f'{i}\n')
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                f.write(f'{i} {j} \n')

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
