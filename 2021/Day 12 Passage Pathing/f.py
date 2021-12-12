



def load(file):
    graph={}
    with open(file,"r") as f:
        while True:
            line=f.readline().replace("\n","")
            if line =="":
                break
            pars=line.split('-')
            
            if not pars[0] in graph.keys():
                graph[pars[0]] = []
            graph[pars[0]].append(pars[1])

            if pars[0] != 'start':
                if not pars[1] in graph.keys():
                    graph[pars[1]] = []
                graph[pars[1]].append(pars[0])
    graph['end']=[]
    return graph



def resolve1(graph):
    paths=[['start']]
    j=0
    for path in paths:
        i=len(path)-1
        nod=path[i]
        if nod == "end":
            j=j+1
            continue
        for vic in graph[nod]:
            if not vic in path or vic.isupper():
                paths.append(path+[vic])
    #return j
    i=0
    for x in paths:
        if x[len(x)-1] == "end":
            i=i+1
            print(x)
    return i

def resolve2(graph):
    paths=[['start']]
    j=0
    for path in paths:
        
        i=len(path)-1
        nod=path[i]
        if nod == "end":
            j=j+1
            continue

        
        
        for vic in graph[nod]:
            if vic.isupper():
                
                paths.append(path+[vic])
            else:
                if vic=="end" :
                    
                    paths.append(path+[vic])
                else:
                    if (count_times(path) or not vic in path ) and vic != 'start':
                    
                        paths.append(path+[vic])
            
                

    #return j
    i=0
    for x in paths:
        if x[len(x)-1] == "end":
            i=i+1
            #print(x)
    return i


def count_times(lista):
    k=""
    se=set()
    for x in lista:
        if x.islower():
            if not x in se:
                se.add(x)
            else: 
                return False
    return True



if __name__=="__main__":

    x=load("in.txt")
    x=load("input.txt")


    import time

    start = time.time()
   

    res=resolve2(x)
    end = time.time()
    print(end - start)
    print(res)