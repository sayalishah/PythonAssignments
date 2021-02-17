def CheckNumber(number):
    if number %5== 0:
        return True
    else:
        return False
   
def main():
    print("Enter Number")
    value = int(input())
    if (CheckNumber(value)):
        print("True")   
    else :
        print("False")   

if __name__ == "__main__":
    main()