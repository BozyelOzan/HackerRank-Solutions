#!env\Scripts\python.exe

def print_rangoli(size):
    alph = "abcdefghijklmnopqrstuvwxyz"
    line = []

    for i in range(size):
        a = "-".join(alph[i:size])
        line.append(a[::-1] + a[1:])
    
    w = len(line[0])

    for i in range(size-1, 0, -1):
        print(line[i].center(w, '-'))
        
    for i in range(size):
        print(line[i].center(w, '-'))
    pass

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)