
def ChkNum(value1):
    if value1%2==0:
        return  True
    else:
        return False



def main():
    print("Enter number")
    inumber = int(input())
    if(ChkNum(inumber)):
        print("Number is Even")
    else:
         print("Number is Odd")

if __name__ == "__main__":
    main()