"""
给你一个只包含 '(' 和 ')' 的字符串，
找出最长有效（格式正确且连续）括号子串的长度。
"""

def f(s: str) -> int:
    # if not s:
    #     return 0
    # i = 0
    # temp = 0
    # while i < len(s):
    #     print(i)
    #     if i >= 1 and s[i-1] == "(" and s[i] == ")":
    #         temp += 2
    #     i += 1
    # return temp
    stack = [-1]
    ret = 0
    lg = len(s)
    for i in range(lg):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ret = max(ret, i - stack[-1])
    return ret


if __name__ == '__main__':
    s =  "()(())"
    print(f(s))