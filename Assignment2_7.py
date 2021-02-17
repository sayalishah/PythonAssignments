def PrintSign(num):
    for iCnt in range(1,num+1):
        for inCnt in range(1,num+1):
            print(inCnt,end = "      ")
        print("  ")

   
def main():
    print("Enter input")
    sValue = int(input())
    PrintSign(sValue)   
   

if __name__ == "__main__":
    main()