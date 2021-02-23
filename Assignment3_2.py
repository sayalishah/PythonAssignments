import functools

def ReturnMaxNo(arr):
    max = arr[0]
    for iCnt in range(len(arr)):
        if(max<arr[iCnt]):
            max= arr[iCnt]
    return max    
    
max =0
i = 0

def ReturnMaxNoRecursionMethod(arr):
    global max 
    global i
    
    if(i<len(arr)):
        if(max<arr[i]):
            max = arr[i]
            i=i+1
            ReturnMaxNoRecursionMethod(arr)
    return max    
   
def main():
    arr=[]
    print("Enter Size Of Array")
    size =int(input())

    for i in range(size):arr.append(int(input()))   

    print("Max No from array ",ReturnMaxNo(arr))
    print("Max No from array using  recursion ",ReturnMaxNoRecursionMethod(arr))
    print("Max No from array using lambda",functools.reduce(lambda v1, v2: max(v1, v2), arr))
   

if __name__ == "__main__":
    main()