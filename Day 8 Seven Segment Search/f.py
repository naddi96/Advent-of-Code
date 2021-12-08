
def loadinput(filename):
    with open(filename) as f:
        stri=[]
        while True:
            line = f.readline()
            stri.append(line.replace('\n',""))

            if not line:
                break
        
        return stri[:-1]

def return_mappping(input):
    input=input.split(" ")
    digits=input[:10]
    out=input[11:]
 
    digit_dict={}
    out_set=[ ]
    for x in out:
        x=sorted(x)
        out_set.append(''.join(x))
    one=""
    fore=""
    digits_sets=[]
    for x in digits:
        l=len(x)
        x=sorted(x)
        x=''.join(x)
        
        if l==2:
            digit_dict[x]=1
            one=set(x)
        if l==4:
            digit_dict[x]=4
            fore=set(x)
        if l==3:
            digit_dict[x]=7 
        if l==7:
            
            digit_dict[x]=8
        if l != 2 and l != 4  and l != 3 and l != 7:
            digits_sets.append(x)
        
    for x in digits_sets:
        num=set(x)

        set1=num^fore
        
        if len(set1)==2 and len(x)==6:
            digit_dict[x]=9

        if len(set1 )==5 and len(x)==5:
            digit_dict[x]=2

        if len(set1)==3 and len(x)==5:
            digit_dict[x]=5

        if len(num-one )==3 and len(x)==5:
            digit_dict[x]=3
        if len(set1)==4 and len(x)==6:
            if len(num ^ one)==6:
                digit_dict[x]=6
            else:
                digit_dict[x]=0
    return digit_dict,out_set

def resolve1(input):
    counts=[0,0,0,0,0,0,0,0,0,0]
    for line in input:
        mapp,num=return_mappping(line)
        for x in num:
            counts[mapp[x]]=counts[mapp[x]]+1
    return counts

def resolve2(input):
    sum=0
    for line in input:
        mapp,num=return_mappping(line)
        app=''
        for x in num:
            app=app+str(mapp[x])
        sum=sum+int(app)
    return sum


if __name__ == '__main__':
    input=loadinput("input.txt")
    #input=loadinput("in.txt")
    x=resolve1(input)
    print(x[1]+x[4]+x[7]+x[8])
    print(resolve2(input))

 
    