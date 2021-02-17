def IsNumberPrime(num):
    sum = 0
    if num <= 1:
        print(num,"Is not prime number")
    else:
        for iCnt in range(2,num):
            if num % iCnt == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
                break
   
       
   
def main():
    print("Enter input")
    sValue = int(input())
    IsNumberPrime(sValue)   
   

if __name__ == "__main__":
    main()