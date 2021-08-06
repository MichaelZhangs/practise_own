while True:
    try:
        s=input().split()
        mm,l,k=int(s.pop(0)),[s.pop(0)],s.pop(-1)
        for i in range(0,2*mm-2,2):
            n,m=s[i],s[i+1]
            l.insert(l.index(m)+1,n)
        l.remove(k)
        print(" ".join(l)+" ")
    except:
        break