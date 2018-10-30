# -*- coding: utf-8 -*-
import xlrd
import sys
def loaddata(fileName):
    Name='../data/'+fileName+'.xlsx'
    aa = []
    bb = []
    data = xlrd.open_workbook(Name)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    for i in range(1, nrows):
        rowValues = table.row_values(i)  # 某一行数据
        for item in rowValues:
            a = item
            if a != 'm' and a != 'y' and a != 'n':
                continue
            elif a== 'y':
                bb.append(1)
            elif a == 'm' or a=='n':
                bb.append(0)
        aa.append(bb)
        bb = []
    return aa
if __name__ == '__main__':
    fileName=sys.argv[1]
    mat=loaddata(fileName)
    print('Successiful Load Data :'+fileName+'.xlsx')