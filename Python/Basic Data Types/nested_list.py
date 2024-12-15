#!env\Scripts\python.exe

if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
    
    total_score = []
    for i in python_students:
        total_score.append(i[1])
    total_score = list(set(total_score))
    total_score.sort()
    min_sec = total_score[1]
    
    stu_name = []
    for i in python_students:
        if min_sec == i[1]:
            stu_name.append(i[0])
    stu_name.sort()
    for i in stu_name:
        print(i)