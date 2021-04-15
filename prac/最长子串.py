
def findSubStr(a):
    res = [] #收集所有不重复子串
    for i in range(len(a)):
        tmp=a[i]
        for j in range(i+1, len(a)):
            if a[j] not in tmp:
                tmp+=a[j]
            else:
                break
        res.append(tmp)
    mlen = max(len(s) for s in res)  #所有子串中最长的长度
    ret =  [ s for s in res if len(s) == mlen]
    return mlen, ret

a = "abcdhaeagbcfagiajake"
ret = findSubStr(a)
print(ret)



