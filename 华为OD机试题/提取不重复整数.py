def solution():
    s = input()
    a = ""
    for i in s[::-1]:
        if i not in a:
            a += i
    print(int(a))
solution()