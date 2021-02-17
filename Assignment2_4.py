def AdditionOfFactors(num):
    sum = 0
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num):
            if num % i == 0:
                sum = sum + i
            else:
                pass    

    
    print("The Sum factors of num ",num,"is",sum)
   
       
   
def main():
    print("Enter input")
    sValue = int(input())
    AdditionOfFactors(sValue)   
   

if __name__ == "__main__":
    main()