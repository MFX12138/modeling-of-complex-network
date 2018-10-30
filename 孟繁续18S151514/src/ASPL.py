# coding=utf-8
#平均最短路径长度
import copy
import sys
#弗洛伊德算法求最小路径
def floyd(Matrix):
    mat = copy.deepcopy(Matrix)
    Num = mat.__len__()
    for m in range(Num):
        for n in range(Num):
            if mat[m][n]==0:
                mat[m][n]='INF'
    for m in range(0, Num):
        mat[m][m]=0

    for k in range(0,Num):
        for i in range(0, Num):
            for j in range(0, Num):
                if mat[i][k] != 'INF' and mat[k][j] != 'INF':
                    if mat[i][j]=='INF' or mat[i][j] >mat[i][k] +mat[k][j]:
                        mat[i][j] = mat[i][k] + mat[k][j]
    return mat
#平均最短路径长度
def Aspl(Matrix):
    mat=floyd(Matrix)
    Num = mat.__len__()
    sumlen=0
    for i in range(Num):
        for j in range(Num):
            if mat[i][j]!='INF':
                sumlen = sumlen + mat[i][j]
    ave=sumlen/(Num*(Num-1))
    return ave
if __name__ == '__main__':
    from loadData import *
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    ave=Aspl(mat)
    print("aver shorest path lengh:", ave)