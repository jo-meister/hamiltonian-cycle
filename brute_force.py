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
file = open("big.dat")
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
