from copy import deepcopy
n = int(input())
s_list = [ input().strip().split(",") for _ in range(n) ]
target_s = list(input())
print(s_list)


res = []
lst = deepcopy(target_s)
c = 0
d = {}
for i in s_list:
    p = 0
    for k in i:
        for j in target_s:
            if k == j:
                d[j] = [str(c),str(p)]
                target_s.pop(target_s.index(j))
                break
        p += 1
    c += 1
print(d)
for i in lst:
    res.append(d.get(i))
res = [ j for i in res for j in i ]
print(res)
print(",".join(res))




