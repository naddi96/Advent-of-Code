def load(input):
    lista=[]
    with open(input,"r") as f:
        while True:
            x=f.readline()
            lista.append(x.replace("\n",""))
            
            if x=="":
                break
    return lista            


def parse(line,open_set,close_set,mapping,score_map):
    pile=[]
    for x in line:
        if x in open_set:
            pile.append(x)

        if x in close_set:
            popped=pile.pop()
            if mapping[x]!=popped:
                return score_map[x]
    return 0
def resolve1(inp):
    mapping={'}':'{',
             ']':'[',
             ')':'(',
             '>':'<'}
    open_set={"{","[","<","("}
    close_set={"}","]",">",")"}
    score_map={"}":1197,"]":57,">":25137,")":3}
    summ=0
    for line in inp:
        summ=summ+parse(line,open_set,close_set,mapping,score_map)
    
    return summ


def parse2(line,open_set,close_set,mapping,score_map):
    pile=[]
    for x in line:
        if x in open_set:
            pile.append(x)

        if x in close_set:
            popped=pile.pop()
            if mapping[x]!=popped:
                return 0
    score=0
    
    pile.reverse()
    for x in pile:
        score=(score*5)+score_map[x]
    return score

def resolve2(inp):
    mapping={'}':'{',
             ']':'[',
             ')':'(',
             '>':'<'}
    open_set={"{","[","<","("}
    close_set={"}","]",">",")"}
    score_map={"{":3,"[":2,"<":4,"(":1}
    
    li=[]
    for line in inp:
        x=parse2(line,open_set,close_set,mapping,score_map)
        if x!=0:
            li.append(x)
    li=sorted(li)
    return li[int(len(li)/2)]


if __name__=='__main__':
    inp=load('in.txt')
    inp=load('input.txt')

    x=resolve1(inp)
    print(x)

    x=resolve2(inp)
    print(x)