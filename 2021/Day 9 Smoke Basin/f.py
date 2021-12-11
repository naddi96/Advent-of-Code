
def load(input):
    with  open(input,"r") as f:
        matr=[]
        while True:
            line = f.readline()
            
            if line !='':
                line=line.replace('\n',"")
                row= [int(x) for x in line]
                matr.append(row)
            if not line:
                break
        return matr


def get_neibough(i,j,num_col,num_row):
    position=[[0,1],[0,-1],[1,0],[-1,0]]
    vicini=[]
    for x in position:
        if not((i+ x[0]< 0 or i+x[0]>num_row) or (j+x[1]<0 or j+x[1]>num_col)):
            vicini.append([i+x[0],j+x[1]]) 
    return vicini
            

def visit_basis(matr,start_index,num_col,num_rows,visitati):
    i=start_index[0]
    j=start_index[1]
    if [i,j] in visitati:
        return
    if matr[i][j]==9:
        return
    vicini=get_neibough(i,j,num_col,num_rows)
    visitati.append([i,j])
    for x in vicini:
        visit_basis(matr,x,num_col,num_rows,visitati)
    return visitati






def resolve1(inp):
    num_col=len(inp[0])-1
    num_row=len(inp)-1
    mins=[]
    sum=0
    for i,row in enumerate(inp):
        for j,el in enumerate(row):
            indexs=get_neibough(i,j,num_col,num_row)
            count=0
            for index in indexs:
                if el < inp[index[0]][index[1]]:
                    count=count+1
                if count==len(indexs):
                    mins.append([i,j])
                    sum=sum+el
    return sum+ len(mins),mins





def resolve2(inp,mins):
    num_rows=len(inp)-1
    num_col=len(inp[0])-1
    basis=[]
    for point in mins:
        x=visit_basis(inp,point,num_col,num_rows,[])
        basis.append(len(x))
    max1=max(basis)
    basis.remove(max1)
    max2=max(basis)
    basis.remove(max2)
    max3=max(basis)
    print(max1*max2*max3)
    return max1*max2*max3

    
if __name__=='__main__':
    #inp=load('in.txt')
    inp=load('input.txt')
    _,mins=resolve1(inp)
    resolve2(inp,mins)