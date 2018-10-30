# coding=utf-8
# 计算核心数
import sys
import drawGraph
import matplotlib.pyplot as plt
import networkx as nx
def coreness(Matrix):
    Num = Matrix.__len__()
    Degreedis = []
    core=[0 for i in range(Num)]
    for i in range(0, Num):
        Degreedis.append(0)
    flag = 0
    key=1
    plt.figure(figsize=(60, 65))
    while flag <= Num:
        v = 0
        for line in Matrix:
            Degreedis[v] = sum(line)
            v += 1
        for j in range(Num):
            if Degreedis[j] <= flag and Degreedis[j]!=0:
                ax=plt.subplot(10,5,key)
                ax.set_title('Node%d has %d coreness'%((j + 1),flag))
                key+=1
                G=drawGraph.drawgraph(Matrix)
                nx.draw(G,node_size=2)
                core[j]=flag
                for k in range(Num):
                    Matrix[k][j] = 0
                    Matrix[j][k] = 0
        v = 0
        for line in Matrix:
            Degreedis[v] = sum(line)
            v += 1
        flag2 = 0
        for l in range(Num):
            if Degreedis[l] == flag and flag!=0:
                flag2 = 1
        if flag2 == 0:
            flag += 1
    plt.show()
    print(core)
    return core

if __name__ == '__main__':
    from loadData import *
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    coreness(mat)