def NumberOfDigits(num):
    count = 0
    while(num>0):
        count=count+1
        num=num//10
    print("The number contains digits are " ,count)

   
def main():
    print("Enter input")
    sValue = int(input())
    NumberOfDigits(sValue)   
   

if __name__ == "__main__":
    main()