import functools

class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        print("Enter First number ")
        self.value1=int(input())
        print("Enter Second number ")
        self.value2=int(input())


    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1//self.value2

    def PrintResults(self):
        print("Addition =",self.Addition())
        print("Subtraction =",self.Subtraction())
        print("Multiplication =",self.Multiplication())
        print("Division =",self.Division())               
        

def main():
    obj = Arithmetic()
    obj.Accept()
    obj.PrintResults()

    obj1 = Arithmetic()
    obj1.Accept()
    obj1.PrintResults()
   


if __name__ == "__main__":
    main()