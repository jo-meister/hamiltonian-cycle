import time


def hamiltonian_cycle(graph, path=[]):
    # Return the path if a hamiltonian cycle is found.
    if len(path) == len(graph) and graph[path[-1]][path[0]] == 1:
        return path

    # Visit each unvisited neighbor of the last node in the path
    last = path[-1] if path else None
    for node in range(len(graph)):
        if node not in path and (last is None or graph[last][node] == 1):
            cycle = hamiltonian_cycle(graph, path + [node])
            if cycle is not None:
                return cycle

    # If no Hamiltonian cycle is found, return None
    return None


# Read from file.
file = open("datafiles/hamcycle_jcwalker10.dat")
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
