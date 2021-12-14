def load (file):
    stri=""
    with open(file,"r") as f:
        stri=f.readline().replace("\n","")
        f.readline()
        dic={}
        while True:
            line=f.readline().replace("\n","")
            if line=="":
                break
            line=line.split(" -> ")
            dic[line[0]]=line[1]
            

        return stri,dic
   


def resolve1(stri,dic):
    stri_len=len(stri)
    new_stre=""
    i=0
    for x in range(40):
        
        if new_stre!="":
            stri_len=len(new_stre)
            stri=new_stre
            new_stre=""
        i=0
        while i < stri_len-1:
            rule=stri[i]+stri[i+1]
            if new_stre=="":
                d=stri[i]
            else:
                d="" 
            new_stre= new_stre +d +dic[rule]+stri[i+1] 
            i=i+1
        
        print(len(new_stre))
    

    dic={}
    y=""
    for x in new_stre:
        y=x
        if x in dic:
            dic[x]=dic[x]+1
        else:
             dic[x]=1
    max_=0
    min_=dic[y]

    print(dic)
    for x in dic.keys():
            max_=max(dic[x],max_ )
            min_=min(dic[x],min_)
    return max_ - min_




def resolve2(stri,dic):

    dic_count={}
    c={}
    f={}

    

    for x in dic.keys():
        dic_count[dic[x]]=0
        f[dic[x]]=0
        dic[x]=(dic[x]+x[1],x[0] +dic[x] )
        c[x]=0

    len_=len(stri)-1
    for i in range(len_):
        key=stri[i]+stri[i+1]
        c[key]+=1
        f[stri[i]]+=1
    
    f[stri[len_]]+=1
    
    for x in range(0,40):
        a= {k:0 for k in dic.keys()}
        for d in c.keys():
            a1,a2=dic[d]
            a[a1]+=c[d]
            a[a2]+=c[d]
            f[a1[0]]+=c[d]
            c[d]=0
        c=a
    
    max_=0
    min_=float('inf')
    for x in f.keys():
            max_=max(f[x],max_ )
            min_=min(f[x],min_)
    return max_ - min_
            



if __name__=="__main__":
    stri,dic=load("in.txt")
    stri,dic=load("input.txt")

    #x=resolve1(stri,dic)
    x=resolve2(stri,dic)
    print(x)