while True:
    try:
        num=int(input())
        m=int(input())
        table=[]
        for each in range(num):
            tableLine=input().split(' ')
            name,score=tableLine[0],int(tableLine[1])
            table.append((name,score))
        if m==0:
            newTable=sorted(table,key=lambda x:x[1],reverse=True)
        else:
            newTable=sorted(table,key=lambda x:x[1])
        for each in newTable:
            print(each[0]+' '+str(each[1]))
    except:
        break