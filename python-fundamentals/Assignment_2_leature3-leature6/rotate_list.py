def rotate_list(lst,k):
    return lst[::k]

def main():
    lst=int(input("Input: "))
    k=int(input("Input(Enter the number of rotation): "))
    rotate_list(lst,len(lst)-k)

if __name__ == '__main__':
    main()