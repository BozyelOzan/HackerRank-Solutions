#!env\Scripts\python.exe

if __name__ == '__main__':
    N = int(input())
    naked_list = []

    for _ in range(N):
        inp = input().split()
        command = inp[0]
        values = inp[1:]

        if command == "print":
            print(f"{naked_list}")
        else:
            new_com = "naked_list." + command + "(" + ",".join(values) + ")"
            exec(new_com)
    
