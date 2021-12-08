



def load(input):
    with  open(input,"r") as f:
        stri=[]
        while True:
            line = f.readline()
            if line !='':
                stri.append(int(line.replace('\n',""),10))
            if not line:
                break
        return stri


def resolve1(values):
    l=len(values)
    count=0
    for x in range(l):
        if x+1 <l:

            if values[x+1] >= values[x]:
                #print(values[x+1])
                count=count+1
    return count            

def resolve2(values):
    l=len(values)
    count=0
    last=-1
    x=0
    while True:


        if (x>=l-2):
            break
        winA=values[x]+values[x+1]+values[x+2]
        if last<winA and last!=-1:
            count=count+1
        if (x>=l-3):
            break
        winB=values[x+1]+values[x+2]+values[x+3]
        if winA<winB:
            count=count+1
        if (x>=l-4):
            break
        winC=values[x+2]+values[x+3]+values[x+4]
        if winB<winC:
            count=count+1
        if (x>=l-5):
            break
        winD=values[x+3]+values[x+4]+values[x+5]
        if winC<winD:
            count=count+1
        last=winD
        x=x+4
        
        
        #print(winA,winB,winC,winD,winE,winF,winG,winH)
        




        


    return count
if __name__=="__main__":
    values=load("input.txt")
    #values=load("in.txt")
    #c=resolve1(values)
    c=resolve2(values)
    print(c)