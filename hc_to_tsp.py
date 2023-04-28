# Joey Walker
import sys
from itertools import permutations


def tsp(graph, target_distance):
    n = len(graph)

    # Generate all possible routes.
    routes = permutations(range(n))
    for route in routes:
        if distance(graph, route) <= target_distance:
            return list(route)
    return None


def distance(graph, route):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i+1]]
    distance += graph[route[-1]][route[0]]
    return distance


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
    adj_matrix[a-1][b-1] = 1
    adj_matrix[b-1][a-1] = 1

# Set distance between cities with no edge as 2.
for city_a in range(n):
    for city_b in range(n):
        if adj_matrix[city_a][city_b] == 0:
            adj_matrix[city_a][city_b] = 2
            adj_matrix[city_b][city_a] = 2

print('Hamiltonian Cycle to Traveling Salesman Decision Problem')
cycle = tsp(adj_matrix, n)
if cycle is not None:
    print(f'Route found of total distance {n}')
    print([v + 1 for v in cycle + [cycle[0]]])
else:
    print(f'No route of total distance {n} found')
