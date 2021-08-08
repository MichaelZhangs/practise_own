import sys
s_list= sys.stdin.readline().strip().split(",")
print(s_list)
def sort_list(s_list):
    for i in range(len(s_list)):
        for j in range(i,len(s_list)):
            if len(s_list[i]) > len(s_list[j]):
                s_list[i], s_list[j] = s_list[j],s_list[i]

    s_list = [ sorted(i) for i in s_list]
    s_list = ["".join(i) for i in s_list]
    return s_list
def aa(s_list):
    res = []
    for i in range(len(s_list)):
        for j in range(i+1,len(s_list)):
            print(s_list[i],s_list[j])
            for k in s_list[i]:
                if k  in s_list[j]:
                    break
            else:
                res.append(len(s_list[i]) * len(s_list[j]))
    if res:
        print(max(res))
    else:
        print("0")

s_list = sort_list(s_list)
aa(s_list)




