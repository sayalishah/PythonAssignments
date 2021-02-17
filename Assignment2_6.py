def PrintSign(num):
    for iCnt in range(num,0,-1):
        print ("*   "*iCnt)
   
def main():
    print("Enter input")
    sValue = int(input())
    PrintSign(sValue)   
   

if __name__ == "__main__":
    main()