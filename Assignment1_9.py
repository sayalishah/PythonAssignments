def PrintEvenNumber():
    iCnt = 1
    cuurentnum = 1
    while iCnt < 11:
        if(cuurentnum%2==0):
            print(cuurentnum,end = "   ")
            iCnt=iCnt+1
            cuurentnum=cuurentnum+1
        else:
            cuurentnum=cuurentnum+1

   
def main():
    PrintEvenNumber()   
    print("")

if __name__ == "__main__":
    main()