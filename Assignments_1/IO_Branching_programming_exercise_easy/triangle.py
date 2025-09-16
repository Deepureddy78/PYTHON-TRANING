def triangle():
    sides=input("Enter the sides\n").split()
    a=int(sides[0])
    b=int(sides[1])
    c=int(sides[2])
    if a<=0 or b<=0 or c<=0:
        print("Invalid triangle")
    elif a==b==c:
        print("Eqvilaternal triangle")
    elif a==b or b==c or c==a:
        print("Isosceles triangle")
    elif a!=b!=c:
        print("Scalene Triangle")

def main():
    triangle()

if __name__ == '__main__':
    main()