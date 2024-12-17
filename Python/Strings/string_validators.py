#!env\Scripts\python.exe

if __name__ == '__main__':
    s = input()

    r = False
    for _ in s:
        if _.isalnum():
            r = True
    print(r)

    r = False
    for _ in s:
        if _.isalpha():
            r = True
    print(r)

    r = False
    for _ in s:
        if _.isdigit():
            r = True
    print(r)

    r = False
    for _ in s:
        if _.islower():
            r = True
    print(r)

    r = False
    for _ in s:
        if _.isupper():
            r = True
    print(r)