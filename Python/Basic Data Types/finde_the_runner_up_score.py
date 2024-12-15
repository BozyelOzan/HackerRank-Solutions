#!env\Scripts\python.exe

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr, reverse=True)
    
    max_num = arr[0]
    score = []
    
    for i in range(n):
        if max_num != arr[i]:
            score.append(arr[i])
            break
    print(score[0])