# coding=utf-8
import numpy as np
import sys
import matplotlib.pyplot as plt
def degree(Matrix):
    Degree=[]
    for line in Matrix:
        Degree.append(sum(line))
    return Degree
def showdegree(Matrix):
    Num = Matrix.__len__()  # 节点个数
    Degree=degree(Matrix)
    temp=list(range(Num))
    fig1 = plt.figure(2)
    rects = plt.bar(left=(temp), height=(Degree), width=1, align="center", yerr=0.000001)
    plt.title('The degree of these nodes')
    plt.xlabel('Number of nodes')
    plt.ylabel('Degree')
    plt.show()
def showother(Matrix):
    nodeNum=len(Matrix)
    edgeNum=(sum(degree(Matrix)))/2
    averDegree=sum(degree(Matrix))/nodeNum
    print('nodeNum:',nodeNum)
    print('edgeNum:',edgeNum)
    print('averDegree:',averDegree)
    return nodeNum,edgeNum,averDegree
if __name__=='__main__':
    from loadData import *
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    showdegree(mat)
    showother(mat)