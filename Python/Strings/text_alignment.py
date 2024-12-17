#!env\Scripts\python.exe

if __name__ == "__main__":
    a = int(input())
    s = "H"

    for i in range(a):
        print((s*i).rjust(a-1)+s+(s*i).ljust(a-1))

    for i in range(a+1):
        print((s*a).center(a*2)+(s*a).center(a*6))

    for i in range((a+1)//2):
        print((s*a*5).center(a*6))    

    for i in range(a+1):
        print((s*a).center(a*2)+(s*a).center(a*6))    

    for i in range(a):
        print(((s*(a-i-1)).rjust(a)+s+(s*(a-i-1)).ljust(a)).rjust(a*6))