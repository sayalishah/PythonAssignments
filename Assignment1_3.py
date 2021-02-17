def Add(value1,value2):
    return  value1+value2
   
def main():
    print("Enter first number ")
    ifirstnuber = int(input())
    print("Enter first number ")
    isecondtnuber = int(input())
    iResult= Add(ifirstnuber,isecondtnuber)
    print("Addition Result  ",iResult)

if __name__ == "__main__":
    main()