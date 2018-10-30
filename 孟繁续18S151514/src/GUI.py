from tkinter import *
from tkinter import messagebox
from loadData import *
from drawGraph import *
from Degree import *
from Distribution import *
from ASPL import *
from Clustering import *
from Coreness import *
from Attack import *

root = Tk()
root.title('welcome! ! !')
root.geometry('500x400+500+300')
v = IntVar()
def showMessage(title,*message):  
    messagebox.showinfo(title,message)
def loadData():
    if (str(var.get()) == '1'):
        name='name'
    if (str(var.get()) == '2'): 
        name='hometown'
    if (str(var.get()) == '3'):
        name='dialect'
    mat=loaddata(name)
    #showMessage('loadData','Successiful Load Data :'+name+'.xlsx')
    return mat
def drawG():
    nx.draw(drawgraph(loadData()), node_size=20)
    plt.show()
def degree():
    showdegree(loadData())
    nodeNum,edgeNum,averDegree=showother(loadData())         
    showMessage('information','nodeNum:',nodeNum,'edgeNum:',edgeNum,'averDegree:',averDegree)
def distrib():
    dis=distribution(loadData())
    showMessage('distribution',dis)
def ASPl():
    aspl=Aspl(loadData())
    showMessage('Average Shortest Path Longth',aspl)
def Clust():
    clust=clustering(loadData())
    showMessage('clustering',clust) 
def Core():
    core=coreness(loadData())
    showMessage('Coreness:',core)
def ATT():
    aspli,lgsubi=intentional_attack(loadData())
    asplr,lgsubr=random_attack(loadData())
    draw_attect(aspli,lgsubi,asplr,lgsubr)
group = LabelFrame(root, text='welcome!')  # 基于root 制定一个框架 .
group.pack(padx=50)
var = IntVar()
R1 = Radiobutton(root, text="name", variable=var, value=1 )
R1.pack(anchor=W)
R2 = Radiobutton(root, text="hometown", variable=var, value=2)
R2.pack(anchor=W)
R3 = Radiobutton(root, text="dialect", variable=var, value=3)
R3.pack(anchor=W)
loadDataButton = Button(root, text='LoadData', command=loadData)
loadDataButton.pack(pady=0)
drawGraphButton = Button(root, text='DrawGraph', command=drawG)
drawGraphButton.pack(pady=0)
showDegree = Button(root, text='DrawDegree', command=degree)
showDegree.pack(pady=0)
distrib = Button(root, text='Distribution', command=distrib)
distrib.pack(pady=0)
distrib = Button(root, text='AverageShortestPathLength', command=ASPl)
distrib.pack(pady=0)
distrib = Button(root, text='Clustering', command=Clust)
distrib.pack(pady=0)
distrib = Button(root, text='Coreness', command=Core)
distrib.pack(pady=0)
distrib = Button(root, text='Attack', command=ATT)
distrib.pack(pady=0)
mainloop()