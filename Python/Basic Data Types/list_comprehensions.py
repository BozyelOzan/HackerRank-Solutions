#!env\Scripts\python.exe

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list_n = []
    
    list_x = list(range(x+1))
    list_y = list(range(y+1))
    list_z = list(range(z+1))
    
    for i in list_x:
        for j in list_y:
            for k in list_z:
                if i+j+k != n:
                    list_n.append([i,j,k])
    print(list_n)