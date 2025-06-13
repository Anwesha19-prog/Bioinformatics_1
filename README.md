**Eulerian Cycle Problem Solver (Python)**


**Problem Overview:**
In graph theory, an Eulerian cycle is a cycle in a directed graph that visits every edge exactly once and returns to the starting node. For a graph to have an Eulerian cycle:

Every node must have the same number of incoming and outgoing edges (i.e., in-degree = out-degree).

The graph must be strongly connected, meaning you can reach any node from any other node via a directed path.



**Why Is This Problem Important?**


Eulerian cycles appear in multiple real-world applications, such as:

Genome assembly (e.g., DNA reconstruction using de Bruijn graphs)

Network routing

Circuit design

Tour planning (e.g., the classic Königsberg bridge problem)

In bioinformatics, Eulerian cycles allow us to reconstruct a sequence (like DNA) from overlapping fragments (k-mers), making this a foundational problem in computational biology.

**Problem Statement:**
You are given the adjacency list of a directed graph that has an Eulerian cycle. Your task is to compute one possible Eulerian cycle in the graph and return the sequence of nodes in the order they are visited.

**Input Format**
A text file (input.txt) containing the adjacency list of a directed graph.

Each line has the format:
node: neighbor1 neighbor2 ...


Example: 


0: 3
1: 0
2: 1 6
3: 2
4: 2
5: 4
6: 5 8
7: 9
8: 7
9: 6



**Output Format**
A text file (output.txt) containing a space-separated list of nodes representing one Eulerian cycle.


6 8 7 9 6 5 4 2 1 0 3 2 6
