def load(input):
    lista=[]
    with open(input,"r") as f:
        while True:

            x=f.readline()
            if x=="":
                break
            li=[]
            for c in x.replace("\n",""):
                li.append(int(c))
            lista.append(li)
            

    return lista    



def get_vicinato(i,j,num_col,num_row):
    position=[[0,1],[0,-1],[1,0],[-1,0], [1,1],[-1,-1],[1,-1],[-1,1]]
    vicini=[]
    for x in position:
        if not((i+ x[0]< 0 or i+x[0]>num_row) or (j+x[1]<0 or j+x[1]>num_col)):
            vicini.append([i+x[0],j+x[1]]) 
    return vicini

def resolve1(inp):
    num_col=len(inp[0])-1
    num_row=len(inp)-1
    flash=0
    for step in range(100):

        for i,row in enumerate(inp):
            for j,el in enumerate(row):
                inp[i][j]=inp[i][j]+1
                #vicini=get_vicinato(i,j,num_col,num_row)
                #if inp[i][j] > 9:
        cond=True
        while cond:
            cond=False
            for i,row in enumerate(inp):
                for j,el in enumerate(row):
                    if el>9:
                        vicini=get_vicinato(i,j,num_col,num_row)
                        flash=flash+1
                        inp[i][j]=0
                        for vic in vicini:
                            if inp[vic[0]][vic[1]]!=0:
                                inp[vic[0]][vic[1]]=inp[vic[0]][vic[1]]+1
                            if inp[vic[0]][vic[1]]>9:
                                cond=True
                            
    
    return flash


def resolve2(inp):
    num_col=len(inp[0])-1
    num_row=len(inp)-1
    flash=0
    step=0
    while True:
        for i,row in enumerate(inp):
            for j,el in enumerate(row):
                inp[i][j]=inp[i][j]+1
        cond=True
        while cond:
            cond=False
            for i,row in enumerate(inp):
                for j,el in enumerate(row):
                    if el>9:
                        vicini=get_vicinato(i,j,num_col,num_row)
                        flash=flash+1
                        inp[i][j]=0
                        for vic in vicini:
                            if inp[vic[0]][vic[1]]!=0:
                                inp[vic[0]][vic[1]]=inp[vic[0]][vic[1]]+1
                            if inp[vic[0]][vic[1]]>9:
                                cond=True
                            
        cond=False
        for i,row in enumerate(inp):
                for j,el in enumerate(row):
                    if inp[i][j]!=0:
                        cond=True
        step=step+1
        
        if not cond:
            return step
        
                 




if __name__=="__main__":
    inp=load("in.txt")
    inp=load("input.txt")
    

    #x=resolve1(inp)
    #print(x)
    x=resolve2(inp)
    print(x)