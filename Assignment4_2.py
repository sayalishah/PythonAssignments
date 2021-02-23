import functools

def main():
    arr=[]
    print("Enter first  number")
    no =int(input())

    print("Enter Second  number")
    no1 =int(input())
    
    print("Multiplication of  number ",(lambda x,x1 : x * x1)(no,no1))

if __name__ == "__main__":
    main()