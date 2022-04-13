
class Solution:
    """
    公共子串长度
    """
    def f(self, s: str, s1: str):
        if len(s) > len(s1):
            s, s1 = s1, s
        i = 0
        ans = 0
        while i < len(s):
            res = ""
            for j in range(i,len(s)):
                res += s[j]
                if res in s1:
                    ans = max(ans, j - i + 1)
            i += 1
        return ans
if __name__ == '__main__':
    s = " esc"
    s2 = "abcdefsc"
    print(Solution().f(s, s2))
