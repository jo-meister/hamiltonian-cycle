# Hamiltonian Cycle Problem
Determine if there is a path in a graph that visits each vertex once and returns to the vertex it started at.


# Running Project Files

Brute force solution: python3 brute_force.py

Heuristic solution: python3 heuristic.py

The input file on which to run the algorithm can be adjusted by editing the file to open in the .py files. Example input files are stored in the datafiles folder.


# Example Input Files

### hamcycle_jcwalker10.dat
This file contains a graph that presents a challenge for the heuristic solution. It visits the only connections to the starting vertex first and second so it can never get back to the beginning. Graphs where there are groups of vertices with few connections among them and other groups of vertices that are strongly connected will cause problems for this heuristic solution. The brute force solution has no issue with this graph because it only has 7 vertices.
*   Heuristic certificate - No Hamiltonian cycle exists
*   Brute force certificate - Hamiltonian cycle exists: [1, 2, 4, 6, 7, 5, 3, 1]

### big.dat
This file contains a graph that presents a challenge for the brute force solution. It is intractable for the brute force solution because there are to many possible paths through the graph to create a cycle. The heuristic algorithm is able to find the solution in aroun 1.3 seconds each time.
*   Heuristic certificate - Hamiltonian cycle exists: [1, 2, ..., 1000, 1]
*   Brute force certificate - 
    

# Vertex Cover to Hamiltonian Cycle Mapping
Find a set of vertices of size k that includes at least one endpoint of every edge of a graph

Reduction from Vertec Cover steps
1. Create components: For every edge in the minimum vertex cover problem, create a component. Connect components that represent u and u' of an edge. The number of chains will be equal to the number of vertices.
2. Create selectors: Add k nodes to the new graph that are connected to each unconnected u and u'.
3. Solve Hamiltonian Cycle problem: Start from the selector vertex s1, enter the chain corresponding to the vertex u1 in the cover. Move to the selector vertex s2 and the corresponding u2. Continue until at chain uk. Connect uk to s1. If the Hamiltonian Cycle exists, then the graph has a vertex cover of size k.



# Hamiltonian Cycle to Traveling Salesman Problem Mapping
Find the shortest route that visits each vertex (city) once and ends at the starting vertex.

Reduction from Hamiltonian Cycle steps
1. Construct the graph: Set the edge weight (distance) between connected vertices (cities) as 1 and all other distances as 2.
2. Solve the TSP: If the solution has a total distance traveld equal to the number of vertices in the graph, then there exists a Hamiltonian Cycle.