



def load(file):
    with open(file,"r") as f:
        matr=[]
        while True:
            line=f.readline().replace("\n","")
            if line=="":
                break
            li=[]
            for x in line:
                li.append(int(x))
            
            matr.append(li)
        return matr


def get_weight(matr,pos):
    return matr[pos[0]][pos[1]]

def get_neightbours(pos, num_col,num_row):
    position=[[0,1],[0,-1],[1,0],[-1,0]]
    vicini=[]
    i=pos[0]
    j=pos[1]
    for x in position:
        if not((i+ x[0]< 0 or i+x[0]>num_row) or (j+x[1]<0 or j+x[1]>num_col)):
            vicini.append([i+x[0],j+x[1]]) 
    return vicini

def get_min(q):
    min_=float('inf')
    el=[]
    for x in q.keys():
        if q[x]<min_:
            min_=q[x]
            el=x
    el = el.split("-")
    return [int(el[0]),int(el[1])]        


def conv(pos):
    return str(pos[0])+"-"+str(pos[1])

def resolve1(matr):
    start=[0,0]
    y_len=len(matr)-1
    x_len=len(matr[0])-1
    end=[y_len,x_len]
    priority_q={}
    priority_q[conv(start)]=matr[start[0]][start[1]]
    
    visited={}
    for x in range(y_len+1):
        for y in range(x_len+1):
            visited[conv([x,y])]=float("inf")
    
  
    visited[conv(start)]=0

    while len(priority_q) !=0:
        el=get_min(priority_q)
        priority_q.pop(conv(el))
        neightbours=get_neightbours(el,x_len,y_len)
        el_i,el_j=el[0],el[1]

        
        for x in neightbours:
            i,j=x[0],x[1]
            
            k=matr[i][j]+ visited[ conv(el) ]
            if visited[conv(x)] > k:    
                visited[conv(x)]=k
                priority_q[conv(x)]=k                

    return visited[conv([y_len,x_len])]


import heapdict

def resolve_q(matr):
    start=[0,0]
    y_len=len(matr)-1
    priority_q = heapdict.heapdict()
    x_len=len(matr[0])-1
    end=[y_len,x_len]
    

    priority_q[conv(start)]=matr[start[0]][start[1]]
    
    visited={}
    for x in range(y_len+1):
        for y in range(x_len+1):
            visited[conv([x,y])]=float("inf")
    
  
    visited[conv(start)]=0

    while len(priority_q) !=0:
        
        el=priority_q.popitem()[0].split("-")
        el=[int(el[0]),int(el[1])]
        neightbours=get_neightbours(el,x_len,y_len)
        
        for x in neightbours:
            i,j=x[0],x[1]
            
            k=matr[i][j]+ visited[ conv(el) ]
            if visited[conv(x)] > k:    
                visited[conv(x)]=k
                priority_q[conv(x)]=k                

    return visited[conv([y_len,x_len])]


    
def resolve2(matr):
    y_len=len(matr)
    x_len=len(matr[0])
    y_len_new=y_len*5 - y_len
    x_len_new=x_len*5 -x_len
    for y in range(y_len):
        for x in range(x_len_new):
            el=(matr[y][x]) % 9
            matr[y].append(el+1)
    x_len_new=x_len*5
    for y in range(y_len_new):
        li=[]
        for x in range(x_len_new):
            el=(matr[y][x]) % 9
            li.append(el+1)
        matr.append(li)


    return resolve_q(matr)



if __name__=="__main__":
    x=load('in.txt')
    x=load('input.txt')
    
    #s=resolve1(x)
    s=resolve2(x)
    print(s)
   