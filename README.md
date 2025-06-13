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
<img width="242" alt="image" src="https://github.com/user-attachments/assets/fbf5c915-d62d-4918-b6c5-64d68ba094fe" />

<img width="98" alt="image" src="https://github.com/user-attachments/assets/508a9371-8274-49cb-8af2-234b0ed0a15d" />


**Output Format**
A text file (output.txt) containing a space-separated list of nodes representing one Eulerian cycle.
<img width="209" alt="image" src="https://github.com/user-attachments/assets/fc301362-4c70-489e-9145-36f85891ce4f" />
