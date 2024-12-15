#!env\Scripts\python.exe

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    n_tuple = tuple(integer_list)
    print(hash(n_tuple))
    