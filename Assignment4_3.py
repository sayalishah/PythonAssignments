import functools
   
def main():
    arr=[]
    print("Enter Size Of Array")
    size =int(input())

    for i in range(size):arr.append(int(input()))  

    #fun = lambda v1 : (v1>=70 and v1<=90 )
    #filterlist = (list)(filter(fun, arr))
    #print("filterlist ",filterlist)
    #mapfun = lambda v1 : v1+10
    #maplist= (list)(map(mapfun, filterlist))
    #print("maplist ",maplist)
    #reducefun = lambda v1,v2 : v1*v2
    print("output == ",functools.reduce(lambda v1,v2 : v1*v2,(list)(map(lambda v1 : v1+10, (list)(filter(lambda v1 : (v1>=70 and v1<=90 ), arr))))))





    
    
   

if __name__ == "__main__":
    main()