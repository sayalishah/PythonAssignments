import functools

def FindFrequenceOfNumber(arr,inpuno):
    count = 0
    for iCnt in range(len(arr)):
        if(inpuno==arr[iCnt]):
            count=count+1
    return count    
   
   
def main():
    arr=[]
    print("Enter Size Of Array")
    size =int(input())

    for i in range(size):arr.append(int(input()))  

    print("Find Number count in array")
    inputno =int(input()) 

    print("Find Frequency Of given no  using function ",FindFrequenceOfNumber(arr,inputno))
    print("Count of number in array using lamda ",len(list(filter(lambda x: (x == inputno), arr))))
    
   

if __name__ == "__main__":
    main()