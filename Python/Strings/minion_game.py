#!env\Scripts\python.exe

def minion_game(string):
    # your code goes here
    vowel = ["A", "E", "I", "O", "U"]
    stuart = kevin = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowel:
            kevin += n-i
        else:
            stuart += n-i
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)