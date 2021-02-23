import functools

def main():
    arr=[]
    print("Enter Size Of Array")
    size =int(input())

    for i in range(size):arr.append(int(input()))  

    print("Result of prime number addition == ",functools.reduce(lambda v1,v2:v1+v2,list(filter(lambda i: all(i%j!=0 for j in range(2, i//2)), arr))))

if __name__ == "__main__":
    main()