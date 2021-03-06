
class Circle:
    Pi = 3.14
    def __init__(self):
        self.radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        print("Enter radius")
        self.radius =float(input())

    def CalculateArea(self):
        self.Area=self.Pi*self.radius*self.radius
        
    def CalculateCircumference(self):
        self.Circumference=2*self.Pi*self.radius
         
    def Display(self):
        print("Radius == ",self.radius)
        print("Area == ",self.Area)
        print("Circumference == ",self.Circumference)





def main():
    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__":
    main()