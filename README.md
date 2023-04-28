# Algorithms

brute_force.py: A brute force algorithm for solving the hamiltonian cycle problem.
>   Run: python3 brute_force.py datafiles/hamcycle_jcwalker10.dat

heuristic.py: A heuristic algorithm for solving the hamiltonian cycle problem.
>   Run: python3 heuristic.py datafiles/big.dat

vertexcover_to_hc.py: A mapping from a vertex cover problem's input to the hamiltonian cycle brute force algorithm.
>   Run python3 vertexcover_to_hc.py datafiles/vertex_cover.dat

hc_to_tsp.py: A mapping from a hamiltonian cycle problem's input to a traveling salesman decision problem algorithm.
>   Run: python3 hc_to_tsp.py datafiles/hamcycle_jcwalker10.dat

datafiles: A directory for storing input example input graphs.
>   Each .dat file contains an input graph. Specify the input file to use as the command line argument.

mappedfiles: A directory containing the generated mappings.
*   hc_to_tsp_map.dat: a mapping from hamiltonian cycle to tsp
*   vertexcover_to_hc_map.dat: a mapping from vertex cover to hamiltonian cycle


# Hamiltonian Cycle Problem
Determine if there is a path in a graph that visits each vertex once and returns to the vertex it started at. The problem is NP Complete because it is both NP and NP-hard. It is NP because no polynomial time solution has been found for it and it is verifiable in polynomial time. In my brute force and heuristic algorithms I provide a 'verify_hamiltonian_cycle' function that returns true in O(N) time if the given path is a hamiltonian cycle in the graph. Therefore the problem is verifiable in polynomial time. The hamiltonian cycle problem is NP-hard because any problem in NP can theoretically be reduced to it. I provide a reduction from the vertex cover problem to the hamiltonian cycle.

### Brute Force Approach
This algorithm takes in a graph as input and returns a Hamiltonian Cycle if one exists. It checks if every single path through the graph contains a Hamiltonian Cycle. There are N! possible paths in a graph and it takes N time to verify if each one is a Hamiltonian Cycle. So the complexity of this algorithm is O(N*N!) where N is the number of vertices in the graph.

### Heuristic Approach
This algorithm takes in a graph as input and usually returns a Hamiltonian Cycle if one exists. There are special cases like the graph in hamcycle_jcwalker10.dat that trick this algorithm into not finding a cycle at all. These special cases only occur when graphs contain high deviations in the number of edges from each vertex. The algorithm works by repeatedly adding the adjacent vertex of the current vertex that has the least number of edges. This loop takes N steps. Each step finds the number of edges of each adjacent vertex which takes N^2 time for an adjacency matrix representation of the graph. So the complexity of this algorithm is O(N^3) where N is the number of vertices in the graph.


# Example Input Files

### hamcycle_jcwalker10.dat
This file contains a graph that presents a challenge for the heuristic solution. It visits the only connections to the starting vertex first and second so it can never get back to the beginning. Graphs where there are groups of vertices with few connections among them and other groups of vertices that are strongly connected will cause problems for this heuristic solution. The brute force solution has no issue with this graph because it only has 7 vertices.
*   Heuristic certificate - No Hamiltonian cycle exists
*   Brute force certificate - Hamiltonian cycle found: [1, 2, 4, 6, 7, 5, 3, 1]
*   HC to TSP certificate - Route found of total distance 7: [1, 2, 4, 6, 7, 5, 3, 1]

### big.dat
This file contains a graph that presents a challenge for the brute force solution. It is intractable for the brute force solution because there are too many possible paths through the graph to create a cycle. The heuristic algorithm is able to find the solution in less than two minutes.
*   Heuristic certificate - Hamiltonian cycle found: [1, 2, 3998, 4, 3999, 5, 4000, 6, 7, …, 3996, 3997, 3, 1]
*   Brute force certificate - None after 20 minutes

### vertex_cover.dat
This file was sent from Eleri Floyd who has the vertex cover problem. It causes her heuristic algorithm to produce a less than optimal result, but her brute force algorithm is able to find a vertex cover of size 3.
*   Vertex Cover to HC certificate - A vertex cover of size 3 exists


# Vertex Cover to Hamiltonian Cycle Mapping
Find a set of vertices of size k that includes at least one endpoint of every edge of a graph
*   The vertexcover_to_hc.py program will create a new dat file containing the graph of the mapped input.

Reduction from Vertex Cover steps
1. Create components: For every edge in the minimum vertex cover problem, create a component. Connect components that represent u and u' of an edge. The number of chains will be equal to the number of vertices.
2. Create selectors: Add k vertices to the new graph that are connected to each unconnected u and u'.
3. Solve Hamiltonian Cycle problem: Start from the selector vertex s1, enter the chain corresponding to the vertex u1 in the cover. Move to the selector vertex s2 and the corresponding u2. Continue until at chain uk. Connect uk to s1. If the Hamiltonian Cycle exists, then the graph has a vertex cover of size k.


# Hamiltonian Cycle to Traveling Salesman Problem Mapping
Find if a route exists that visits each vertex (city) once, ends at the starting vertex, and has a total distance traveled less than or equal to n.
*   The hc_to_tsp.py program will create a new dat file containing the graph of the mapped input.

Reduction from Hamiltonian Cycle steps
1. Construct the graph: Set the edge weight (distance) between connected vertices (cities) as 1 and all other distances as 2.
2. Solve the TSP: If the solution has a total distance traveled equal to the number of vertices in the graph, then there exists a Hamiltonian Cycle.