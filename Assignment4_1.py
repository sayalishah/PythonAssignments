import functools

def main():
    arr=[]
    print("Enter number")
    no =int(input())
    
    print("Square of  number ",(lambda x : x * x)(no))

if __name__ == "__main__":
    main()