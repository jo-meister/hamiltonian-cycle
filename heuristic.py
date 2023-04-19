import time


def hamiltonian_cycle(graph, n):
    cycle = [0]
    visited = set([0])

    while len(cycle) < n:
        neighbors = []
        for i, v in enumerate(graph[cycle[-1]]):
            if v == 1 and i not in visited:
                neighbors.append(i)
        neighbors.sort(key=lambda v: sum(graph[v]))
        for v in neighbors:
            cycle.append(v)
            visited.add(v)
            break
        else:
            return None

    if graph[cycle[-1]][cycle[0]] == 1:
        print("Hamiltonian cycle found:")
        cycle.append(cycle[0])
        print([v + 1 for v in cycle])
    else:
        print("No Hamiltonian cycle exists")


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

print('Heuristic hamiltonian cycle')
start = time.time()
hamiltonian_cycle(adj_matrix, n)
end = time.time()
print(f'Run time {end - start}')
