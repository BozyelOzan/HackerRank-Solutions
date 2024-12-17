#!env\Scripts\python.exe

import os 

# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    ans = []
    
    for _ in s:
        ans.append(_.capitalize())
    return " ".join(ans)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()