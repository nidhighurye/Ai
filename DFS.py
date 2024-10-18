import matplotlib.pyplot as plt
import networkx as nx

graph = {
    'kudal': ['malvan', 'sawantwadi', 'kankavli', 'belgav'],
    'sawantwadi': ['kudal', 'kankavli', 'belgav', 'malvan'],
    'malvan': ['kudal', 'kankavli', 'belgav', 'malvan'],
    'belgav': ['kudal', 'kankavli', 'sawantwadi', 'malvan'],
    'kankavli': ['kudal', 'belgav', 'sawantwadi', 'malvan'],
}

grp = nx.Graph(graph)
nx.draw(grp, with_labels=True, node_color="white", font_color="black")

visited = []

def dfs(node, visited, graph):
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(i, visited, graph)

# Call DFS before showing the plot
dfs("kudal", visited, graph)

# Now show the plot
plt.show()


