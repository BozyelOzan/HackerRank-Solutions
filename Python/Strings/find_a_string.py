#!env\Scripts\python.exe

def count_substring(string, sub_string):
    sub_count = 0
    k = len(sub_string)
    for i in range(len(string)):
        if string[i:i+k] == sub_string:
            sub_count += 1
        
    return sub_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)