#!env\Scripts\python.exe

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%400 == 0) and (year%100 == 0):
        leap = True
        return leap
    elif (year%4 == 0) and (year%100 != 0):
        leap = True
        return leap 
    else:
        return leap