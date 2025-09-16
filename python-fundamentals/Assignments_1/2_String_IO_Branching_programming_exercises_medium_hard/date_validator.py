'''5. Date Validator
Description: Check if the entered date (DD/MM/YYYY) is valid (including leap year rules).
Example Input:
Enter date: 29/02/2024
Expected Output:
Valid date'''

def check_valid(dd,mm,yy):
    if (yy % 400 == 0) or (yy % 4 == 0 and yy % 100 != 0): 
        if mm in [1,3,5,7,8,10,12] and dd > 0 and dd < 31:
            print("valid date")
        elif mm in [4,6,9,11] and dd > 0 and dd < 30:
            print("valid date")
        elif mm in [2] and dd>0 and dd<28:
            print("valid date")
        else:
            print("Invalid date")
    else:
        if mm in [1,3,5,7,8,10,12] and dd > 0 and dd < 31:
            print("valid date")
        elif mm in [4,6,9,11] and dd > 0 and dd < 30:
            print("valid date")
        elif mm in [2] and dd>0 and dd<29:
            print("valid date")
        else:
            print("Invalid date")
        
date=input("Enter date:(dd/mm/yyyy)").split("/")
dd=int(date[0])
mm=int(date[1])
yy=int(date[2])

check_valid(dd,mm,yy)