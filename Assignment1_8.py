def PrintAsterick(number):
    for iCnt in range(number):
        print("*", end = " ") 
    print(" ")     
   
def main():
    print("Enter Number")
    value = int(input())
    PrintAsterick(value)   

if __name__ == "__main__":
    main()