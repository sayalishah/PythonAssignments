def DisplayString(sValue):
    for iCnt in range(sValue):
        print("*   "*sValue)
       
   
def main():
    print("Enter input")
    sValue = int(input())
    DisplayString(sValue)   
   

if __name__ == "__main__":
    main()