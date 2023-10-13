# Function to et edges of graph
def graph(input_string):
    edges = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string)):
            if input_string[i] != input_string[j]:
                edges.append((i, j))
    return edges


# Get user IP
input_string = input()

edges = graph(input_string)
print(edges)
