from collections import defaultdict, deque

def parse_input(file_name):
    graph = defaultdict(deque)
    with open(file_name, 'r') as f:
        for line in f:
            node, edges = line.strip().split(": ")
            graph[int(node)] = deque(map(int, edges.split()))
    return graph

def find_eulerian_cycle(graph):
    graph_copy = {u: deque(v) for u, v in graph.items()}
    start_node = next(iter(graph))
    cycle = []
    stack = [start_node]

    while stack:
        current = stack[-1]
        if graph_copy[current]:
            next_node = graph_copy[current].popleft()
            stack.append(next_node)
        else:
            cycle.append(stack.pop())
    return cycle[::-1]

if __name__ == "__main__":
    # 🔽 Change this to your actual input file name
    input_file = "dataset_30187_2.txt"

    # 🔽 Change this to your desired output file name
    output_file = "output.txt"

    graph = parse_input(input_file)
    cycle = find_eulerian_cycle(graph)

    with open(output_file, 'w') as f:
        f.write(" ".join(map(str, cycle)))

    print("Eulerian cycle written to", output_file)

