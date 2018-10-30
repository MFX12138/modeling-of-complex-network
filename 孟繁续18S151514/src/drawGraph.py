# coding=utf-8
import networkx as nx
import numpy as np
import sys
import matplotlib.pyplot as plt
def drawgraph(Matrix):
    G = nx.Graph()
    lenth=len(Matrix)
    for i in range(lenth):
        for j in range(lenth):
            if Matrix[i][j] == 1:
                G.add_edge(i, j)
    del Matrix  
    return G
if __name__ == '__main__':
    from loadData import *
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    G=drawgraph(mat)
    nx.draw(G, node_size=20)
    plt.show()
