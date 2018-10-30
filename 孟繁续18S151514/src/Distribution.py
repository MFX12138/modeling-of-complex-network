# coding=utf-8
import numpy as np
import sys
import matplotlib.pyplot as plt
from Degree import *
def distribution(Matrix):
    Num = Matrix.__len__()  # 节点个数
    deg=degree(Matrix)
    print('The 10 students whose know more student:',np.argsort(deg)[:Num-11:-1])
    Distribution=[0 for i in range(max(deg)+1)]
    for i in range(Num):
        Distribution[deg[i]]+=1
    temp=list(range(max(deg)+1))
    rects = plt.bar(left=(temp), height=(Distribution), width=1, align="center", yerr=0.000001)
    fig1 = plt.figure(1)
    plt.title('The distribution of these nodes')
    plt.xlabel('Degree')
    plt.ylabel('Distribution')
    plt.show()
    return Distribution
if __name__=='__main__':
    from loadData import *
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    distribution(mat)