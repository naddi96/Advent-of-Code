
import numpy as np

def loadinput(filename):
    with open(filename) as f:
        stri=f.read().strip()
        li=[int(x) for x in stri.split(',')]
        return li



def resolve1(inp):
    dim=max(inp)
    arr=np.zeros([dim])
    for k in range(dim):
        for x in inp:

            arr[k]=arr[k] + (max(k,x) -min(k,x))
            if k==2:
                print((max(k,x) -min(k,x)))
    
    index_min=0
    min_v=arr[0]
    for i,v in enumerate(arr):
        if v<=min_v:
            min_v=v
            index_min=i
    return arr,index_min,min_v
    '''
    sottoproblema 
    opt[j] soluzione ottima a cui stare fino alla j-esima elemento 

    opt[j]= min(       )
    '''

    pass

def resolve2(inp):
    dim=max(inp)
    arr=np.zeros([dim])
    for k in range(dim):
        for x in inp:
            arr[k]=arr[k] + sum(range(1,(max(k,x) -min(k,x)+1)))
            #if k==5:
             #   print(sum(range(1,(max(k,x) -min(k,x)+1))))

    index_min=0
    min_v=arr[0]
    for i,v in enumerate(arr):
        if v<=min_v:
            min_v=v
            index_min=i
    return arr,index_min,min_v
    pass


if __name__ == '__main__':
    inp=loadinput("input.txt")
    test=[16,1,2,0,4,2,7,1,2,14]
    #x=resolve1(inp)
    

    y=resolve2(inp)
    print(y)
    
