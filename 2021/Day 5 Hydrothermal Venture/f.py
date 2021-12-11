import numpy as np


def load_input():
    f=open("input.txt","r")
    #read lines of file
    x1=[]
    y1=[]
    y2=[]
    x2=[]
    while True:
      
    
        # Get next line from file
        line = f.readline()
        points=line.replace("\n","").split(" -> ")
        if len(points)>1:
            point1=points[0].split(",")
            point2=points[1].split(",")
            x1.append(int(point1[0]))
            y1.append(int(point1[1]))
            x2.append(int(point2[0]))
            y2.append(int(point2[1]))
        if not line:
            break
    return x1,y1,x2,y2

def resolve1(x1,y1,x2,y2):
    matrix_dim =max([max(x1),max(y1),max(x2),max(y2)])
    
    matrix = np.zeros((matrix_dim+1,matrix_dim+1))
    for i in range(len(x1)):
        if(x1[i]==x2[i]):
            y_min=min(y1[i],y2[i])
            y_max=max(y1[i],y2[i])
            while y_min<=y_max:
                matrix[y_min][x1[i]]+=1
                y_min=y_min+1
        
        if(y1[i]==y2[i]):
            x_min=min(x1[i],x2[i])
            x_max=max(x1[i],x2[i])
            while x_min<=x_max:
                matrix[y1[i]][x_min]+=1
                x_min=x_min+1

    count=0
    for i in range(matrix_dim):
        for j in range(matrix_dim):
           
            if matrix[i][j]>=2:
                count=count+1
    print(matrix)
    print(count)
                

def resolve2(x1,y1,x2,y2):
    matrix_dim =max([max(x1),max(y1),max(x2),max(y2)])
    matrix = np.zeros((matrix_dim+1,matrix_dim+1))
    for i in range(len(x1)):
        if (y1[i] != y2[i] and x1[i] != x2[i]):
            if (y1[i]> y2[i] and x1[i]> x2[i]) or (y2[i]> y1[i] and x2[i]> x1[i]):
                y_min=min(y1[i],y2[i])
                y_max=max(y1[i],y2[i])
                x_min=min(x1[i],x2[i])
                x_max=max(x1[i],x2[i])
                while x_min<=x_max:
                    matrix[y_min][x_min]+=1
                    y_min=y_min+1
                    x_min=x_min+1
            
            if(x1[i]> x2[i] and y1[i]< y2[i]) or (x2[i]> x1[i] and y2[i]< y1[i]):
                y_min=min(y1[i],y2[i])
                y_max=max(y1[i],y2[i])
                x_min=min(x1[i],x2[i])
                x_max=max(x1[i],x2[i])
                
                while y_min<=y_max :
                    matrix[y_min][x_max]+=1
                    y_min=y_min+1
                    x_max=x_max-1
        else:
            
            if(x1[i]==x2[i]):
                y_min=min(y1[i],y2[i])
                y_max=max(y1[i],y2[i])
                while y_min<=y_max:
                    matrix[y_min][x1[i]]+=1
                    y_min=y_min+1
            
            if(y1[i]==y2[i]):
                x_min=min(x1[i],x2[i])
                x_max=max(x1[i],x2[i])
                while x_min<=x_max:
                    matrix[y1[i]][x_min]+=1
                    x_min=x_min+1

            


    count=0
    for i in range(matrix_dim+1):
        for j in range(matrix_dim+1):
           
            if matrix[i][j]>=2:
                count=count+1
    print(matrix)
    print(count)


if __name__ == "__main__":
    x1,y1,x2,y2=load_input()
    resolve2(x1,y1,x2,y2)