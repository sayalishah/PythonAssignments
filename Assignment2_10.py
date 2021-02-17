def NumberOfDigitsAddition(num):
    sum = 0
    while(num>0):
        sum = sum + num % 10
        num=num//10
    print("The number contains digits are " ,sum)

   
def main():
    print("Enter input")
    sValue = int(input())
    NumberOfDigitsAddition(sValue)   
   

if __name__ == "__main__":
    main()