#!env\Scripts\python.exe

def merge_the_tools(string, k):
    sub_s = []

    for i in range(0,len(string),k):
        sub_s.append(string[i:i+k])

    for i in sub_s:
        same = []

        for j in i:
            if not j in same:
                same.append(j)
        print("".join(same))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)