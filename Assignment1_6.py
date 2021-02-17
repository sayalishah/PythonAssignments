def CheckNumber(number):
    if number > 0:
        print("Positive Number")
    elif number == 0:
        print("Zero")
    else:
        print("Negative Number")
   
def main():
    print("Enter Number")
    value = int(input())
    CheckNumber(value)

if __name__ == "__main__":
    main()