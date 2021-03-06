import functools

class Demo:
    def __init__(self,i,j):
        self.no1 = i
        self.no2 = j

    def Fun(self):
        print("i  == ",self.no1)
        print("j  == ",self.no2)

    def Gun(self):
        print("i  == ",self.no1)
        print("j  == ",self.no2)


def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()


if __name__ == "__main__":
    main()