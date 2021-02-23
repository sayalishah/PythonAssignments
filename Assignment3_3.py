import functools

def ReturnMinNo(arr):
    max = arr[0]
    for iCnt in range(len(arr)):
        if(max>arr[iCnt]):
            max= arr[iCnt]
    return max    
   
   
def main():
    arr=[]
    print("Enter Size Of Array")
    size =int(input())

    for i in range(size):arr.append(int(input()))   

    print("Min No from array ",ReturnMinNo(arr))
    
    print("Min No from array",functools.reduce(lambda v1, v2: min(v1, v2), arr))
   

if __name__ == "__main__":
    main()