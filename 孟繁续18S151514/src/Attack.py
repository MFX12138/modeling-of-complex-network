# coding=utf-8
#网络的鲁棒性和脆弱性
from ASPL import *
import copy
import sys
from Degree import degree
import matplotlib.pyplot as plt
import random
#最大联通子图
def largestSubgraph(Matrix):
    mat=floyd(Matrix)
    Num = mat.__len__()    # 节点个数
    subgraph=[[k] for k in range(Num)]
    Max=[]
    for i in range(Num):
        for j in range(Num):
            if mat[i][j]!=0 and mat[i][j]!='INF':
                subgraph[i].append(j)
        if len(subgraph[i])>len(Max):
            Max=subgraph[i]
    return Max
#蓄意攻击
def intentional_attack(Matrix):
    mati=copy.deepcopy(Matrix)
    Num=mati.__len__()
    lgsubi=[]
    aspli=[]
    #intentional_attack
    for n in range(Num):
        Degree=degree(mati)
        k=Degree.index(max(Degree))
        for i in range(Num):
            for j in range(Num):
                mati[i][k]=0
                mati[k][j]=0
        Max=largestSubgraph(mati)
        aspli.append(Aspl(mati))
        lgsubi.append(len(Max))
    return aspli,lgsubi  
#随机攻击
def random_attack(Matrix):
    matr=copy.deepcopy(Matrix)
    Num=matr.__len__()
    lgsubr=[]
    asplr=[]
    #random_attect
    A=[i for i in range(Num)]
    random.shuffle(A)
    for n in range(Num):
        k=A[n]
        for i in range(Num):
            for j in range(Num):
                matr[i][k]=0
                matr[k][j]=0
        Max=largestSubgraph(matr)
        asplr.append(Aspl(matr))
        lgsubr.append(len(Max)) 
    return asplr,lgsubr
#绘制攻击时参数变化
def draw_attect(aspli,lgsubi,asplr,lgsubr):
    #攻击时最大连通子图大小变化
    x =range(len(asplr))
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Attack!!!')
    # 设置X轴标签
    plt.xlabel('Number')
    # 设置Y轴标签
    plt.ylabel('Maximum Connected Subgraph')
    # 画散点图
    ax1.scatter(x, lgsubi, s=12, c='r', marker='o')
    ax1.scatter(x, lgsubr, s=10, c='b', marker='o')
    # 设置图标
    label = ["intentional", "random"]
    plt.legend(label, loc=0, ncol=2)
    
    #攻击时平均最短路径长度变化
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.set_title('Attack!!!')
    plt.xlabel('Number')
    plt.ylabel('Average Shortest Path Longth')
    ax2.scatter(x, aspli, s=12, c='r', marker='o')
    ax2.scatter(x, asplr, s=10, c='b', marker='o')
    label = ["intentional", "random"]
    plt.legend(label, loc=0, ncol=2)

    # 显示所画的图
    plt.show() 
if __name__ == '__main__':
    from loadData import *
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    aspli,lgsubi=intentional_attack(mat)
    mat=loaddata(fileName)
    asplr,lgsubr=random_attack(mat)
    draw_attect(aspli,lgsubi,asplr,lgsubr)