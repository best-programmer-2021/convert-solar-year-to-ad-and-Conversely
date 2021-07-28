from typing import get_origin


print(""" welcome 

    1- help
    2- Convert solar year to AD
    3- Convert AD to solar year

""")
go = input("choose one of them : ")
if go == "1" :
    print(""" hello welcome to program 
    this program convert the year to solar year or ad 
    work with tis program its very easy you choose a convert and say the year of your birthday
    good luck """)
elif go == "2" :
    year = input("please enter the year of birthday : ")
    year = int(year)
    went = year    
    went += 621
    print(went)
elif go == "3" :
    ye = input("please enter the year of birthday : ")    
    ye = int(ye)
    le = ye
    le -= 621
    print(le)
else:
    print("your choose is incorrect")
    print("please try again")
ex = input("choose one key to exit : ")        