
from types import resolve_bases


def load(file):
    x=[]
    y=[]
    folds=[]
    with open(file,"r") as f:
        while True:
            line=f.readline().replace("\n","")
            if line =="":
                break
            points=line.split(",")
            x.append(int(points[0]))
            y.append(int(points[1]))
            #print(points)
        while True:
            line=f.readline().replace("\n","")
            if line =="":
                break
            fold=line.split(" ")[2]
            fold=fold.split("=")
            folds.append( (fold[0], int(fold[1])))
    x_max= max(x)
    y_max=max(y)
    for xy,k in folds:
        if xy=='x':
            x_max=max(x_max ,(k*2))
        if xy=='y':
            y_max=max(y_max,(k*2))
    matr=[]
    for i in range(y_max+1):
        li=[]
        for j in range(x_max+1):
            li.append(0)
        matr.append(li)
    
    for i in range(len(x)):
        matr[y[i]][x[i]]=1

    return matr,folds


def resolve1(matr,folds):
    len_x=len(matr[0])
    len_y=len(matr)

    #for x in matr:
    #   print(x)    
    
    for ord,ax in folds:
       
        if ord=="x":
            for i in range(len_y):
                for sc,dc in zip(range(ax),reversed(range(ax+1,len_x))):
                    matr[i][ax]=0
                    matr[i][sc]= max(matr[i][dc], matr[i][sc])
                    matr[i][dc]=0
            len_x=ax
        if ord=="y":
            for i in range(len_x):
                for sc,dc in zip(range(ax),reversed(range(ax+1,len_y))):
                    matr[ax][i]=0
                    matr[sc][i]= max(matr[dc][i],matr[sc][i])
                    matr[dc][i]=0
            len_y=ax
        break
        #print("aaaaaaaaaaaaa\n")
        #for x in matr:
         #   print(x)
        
   
    summ=0
    for x in matr:
        summ=sum(x)+summ
    #print(summ)
    return summ



def resolve2(matr,folds):
    len_x=len(matr[0])
    len_y=len(matr)
    for ord,ax in folds:
        

        if ord=="x":
            for i in range(len_y):
                for sc,dc in zip(range(ax),reversed(range(ax+1,len_x))):
                    
                    matr[i][ax]=0
                    matr[i][sc]= max(matr[i][dc], matr[i][sc])
                    matr[i][dc]=0
            len_x=ax
        
        if ord=="y":

            for i in range(len_x):
                for sc,dc in zip(range(ax),reversed(range(ax+1,len_y))):
                    matr[ax][i]=0
                    matr[sc][i]= max(matr[dc][i],matr[sc][i])
                    matr[dc][i]=0
            len_y=ax
        

        

    for x in matr[:len_y]:
        k=""
        for c in x[:len_x]:
            if c==1:
                c="#"
            if c==0:
                c=" "
            k=k+c
        print(k)

    



if __name__=="__main__":
    matr,folds=load("in.txt")
    matr,folds=load("input.txt")
    summ=resolve1(matr,folds)
    print(summ)  
    resolve2(matr,folds)  