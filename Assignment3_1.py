import functools

def AdditionOfArray(arr):
    sum = 0
    for iCnt in range(len(arr)):
        sum=sum+arr[iCnt]
    return sum    
    
sum =0
i = 0

def AdditionOfArrayRecursionMethod(data):
    global sum 
    global i
    if(i<len(data)):
        sum= sum+data[i]
        i=i+1
        AdditionOfArrayRecursionMethod(data)
    return sum    
   
def main():
    arr=[]
    print("Enter Size Of Array")
    size =int(input())

    for i in range(size):arr.append(int(input()))   

    print("Result of addition ",AdditionOfArray(arr))
    print("Result of addition using  ",AdditionOfArrayRecursionMethod(arr))
    print("Result of addition using lamda ",functools.reduce(lambda v1, v2: v1+v2, arr))
   

if __name__ == "__main__":
    main()