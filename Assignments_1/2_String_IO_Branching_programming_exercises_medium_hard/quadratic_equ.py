import math

def quadratic_eqa(a,b,c):
    d=b**2-2*a*c
    if d>0:
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        return(math.floor(root1),math.floor(root2))
    elif d==0:
        root =-b/(2*a)
        return (math.floor(root))
    else:
        r=-b /(2*a)
        i=math.sqrt(-d)/(2*a)
        return (r + i * 1j, r - i * 1j)
    
def main():
    a=int(input("Enter coefficients: a="))
    b=int(input("b="))
    c=int(input("c="))

    roots=quadratic_eqa(a,b,c)
    print("Roots:",roots)

if __name__ == '__main__':
    main()