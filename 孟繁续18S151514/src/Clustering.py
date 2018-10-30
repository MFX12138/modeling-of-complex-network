# coding=utf-8
#计算聚类系数
import sys
def clustering(Matrix):
    Num = Matrix.__len__()  # 节点个数
    EEE = [0 for i in range(Num)]
    CCC = [0 for i in range(Num)]
    for i in range(0, Num):
        neighbornum = 0
        neighbor = []
        for j in range(0, Num):
            if i != j and Matrix[i][j] == 1:
                neighbornum += 1
                neighbor.append(j)
        for linea in neighbor:
            for lineb in neighbor:
                if Matrix[linea][lineb] == 1:
                    EEE[i] += 1
        EEE[i] = EEE[i] / 2
        if (EEE[i] == 0):
            CCC[i] = 0
        else:
            CCC[i] = 2 * EEE[i] / (neighbornum * (neighbornum - 1))
    aver = sum(CCC) / Num
    print('clustering:',aver)
    return aver
if __name__ == '__main__':
    from loadData import *
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    clustering(mat)