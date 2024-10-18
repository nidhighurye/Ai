import matplotlib.pyplot as plt
import networkx as nx


graph={'kudal':['sawantwadi','malvan','dodamarg','kankavli'],
       'kankavli':['sawantwadi','malvan','dodamarg','kudal'],
       'sawantwadi':['kudal','malvan','dodamarg','kankavli'],
       'malvan':['sawantwadi','kudal','dodamarg','kankavli'],
       'dodamarg':['sawantwadi','kudal','malvan','kankavli'],
    }

grp=nx.Graph(graph)
nx.draw(grp,with_labels="True",node_color="white",font_color="black")

visited=[]
Queue=[]

def bfs(node,visited,graph):
    visited.append(node)
    Queue.append(node)
    while True:
        m=Queue.pop(0)
        print(m)
        for i in graph[m]:
          if i not in visited:
               visited.append(i)
               Queue.append(i)
bfs("kudal",visited,graph)
