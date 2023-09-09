def addEdge(adj, u, v):
    adj[u].append(v);
    adj[v].append(u);
def delEdge(adj, u, v):
    for i in range(len(adj[u])):
        if (adj[u][i] == v):
            adj[u].pop(i);
            break;
    for i in range(len(adj[v])):
        if (adj[v][i] == u):
            adj[v].pop(i);
            break;
def prGraph(adj, V):
    for v in range(V):
        print("Vertex " + str(v), end = ' ')
        for x in adj[v]:
            print("-> " + str(x), end = ' ')
        print()
    print()
#Driver COde
if __name__ =='__main__':
    V = 5;
    adj = [ [] for i in range(V) ]

    #Adding edge as shown in the example figure
    addEdge(adj, 0, 1);
    addEdge(adj, 0, 4);
    addEdge(adj, 1, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 1, 4);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 4);

    #Print adjacency matrix
    prGraph(adj, V);

    #Deleting Edge (1,4)
    #as shown in the example figure
    delEdge(adj, 1, 4);

    #Print adjacency matrix
    prGraph(adj, V);
