


def load_input(input):
    f=open(input,"r")
    li=[]
    while True:
      
    
        # Get next line from file
        line = f.readline()
        line=line.replace("\n","")
        li.append(line)
        if not line:
            break
    return li[:-1]

def resolve1(input):
    dim_string=len(input[0])
    count_array=[[0,0] for x in range(dim_string)]
    print(count_array)

    for bin in input:
        for i in range(dim_string):
            j=int(i)
            index=int(bin[j])
            #print(count_array[i][index])
            count_array[j][index]=count_array[j][index]+1
    gamma=''
    eps=''
    for x in count_array:
        if x[0]>x[1]:
            gamma=gamma+"0"
            eps=eps+"1"
        else:
            gamma=gamma+"1"
            eps=eps+"0"
    return int(gamma,2)*int(eps,2)

def oxygen(input,i):
    app=input
    counts=[0,0]
    for x in app:
        index=int(x[i])
        counts[index]=counts[index]+1
    
    new_list=[]
    for x in app:
        bit=int(x[i])
        if counts[0]> counts[1]:
            if bit==0:
                new_list.append(x)
        else:
            if bit ==1:
                new_list.append(x)

    if len(new_list)==1:
        return int(new_list[0],2)
    return oxygen(new_list,i+1)
    




def CO2(input,i):
    app=input
    counts=[0,0]
    for x in app:
        index=int(x[i])
        counts[index]=counts[index]+1
    new_list=[]
    for x in app:
        bit=int(x[i])
        if counts[0]<=counts[1]:
            if bit==0:
                new_list.append(x)
        else:
            if bit ==1:
                new_list.append(x)
    
    if len(new_list)==1:
        return int(new_list[0],2)
    return CO2(new_list,i+1)
    




def resolve2(input):

    x=oxygen (input,0)
    y=CO2(input,0)
    print(x*y)


if __name__ == "__main__":
    input=load_input("inputtest.txt")
    input=load_input("input.txt")
    #gamma=resolve1(input)
    resolve2(input)
    #print(gamma)