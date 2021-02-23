import functools
   
def main():
    arr=[]
    print("Enter Size Of Array")
    size =int(input())

    for i in range(size):arr.append(int(input()))  

    #fun = lambda i: all(i%j!=0 for j in range(2, i//2))
    #filterlist = (list)(filter(fun, arr))
    #print("filterlist ",filterlist)
    #mapfun = lambda v1 : v1*2
    #maplist= (list)(map(mapfun, filterlist))
    #print("maplist ",maplist)
    #reducefun = lambda v1,v2 : max(v1,v2)
    #print("output == ",functools.reduce(reducefun,maplist))
    print("output == ",functools.reduce(lambda v1,v2 : max(v1,v2),(list)(map(lambda v1 : v1*2, (list)(filter(lambda i: all(i%j!=0 for j in range(2, i//2)), arr))))))


if __name__ == "__main__":
    main()