# Some practice using the networkx library and matplotlib
# Python3 v 3.6.9

# Because life is too short to use standard Python3 dictionaries
import networkx as nx
# To print out an image of the graph
import matplotlib.pyplot as plot

if __name__ == "__main__":
    g = nx.Graph()
    nodes = ["a","b","c","d","e","f"]
    edges = [("a","b"),
            ("a","f"),
            ("e","f"),
            ("a","c"),
            ("a","e"),
            ("d","e"),
            ("d","c")]
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    nx.draw_networkx(g)

    # saves an image of the graph
    plot.savefig("simple_path.png")

    # clear figure
    plot.clf()
    h = nx.Graph()

    # Perform a depth first search of the network
    # Psuedo:
        # DFS(Graph, source_node):
            # mark source_node as visited
            # for all neighbours of source_node in Graph:
                # if neighbour is not visited:
                    # DFS(Graph, neighbour)
    # Time-complexity = O(V+E)
    dfs = list(nx.dfs_edges(g, source="a", depth_limit=None))

    # Perform a breadth first search of the network
    # Psuedo:
        # BFS(Graph, source_node):
            # Q -> queue.
            # Q.enqueue(source_node)
            # mark source_node as visited.
            # while (Q is not empty)
                # vertex = Q.dequeue()
                # for all neighbours of vertex in Graph:
                    # if neighbour is not visited
                        # Q.enqueue(neighbour)
                        # mark neighbour as visited.
    # Time-complexity = O(V+E)
    bfs = list(nx.dfs_edges(g, source="a", depth_limit=None))
    print(dfs)
    print(bfs)
    h.add_edges_from(dfs)
    nx.draw_networkx(h)
    # saves an image of the dfs
    plot.savefig("dfs_path.png")

    #clear graph h for bfs path
    h.clear()
    # clear figure
    plot.clf()
    h.add_edges_from(bfs)
    nx.draw_networkx(h)

    # saves an image of the dfs
    plot.savefig("bfs_path.png")

    exit()
