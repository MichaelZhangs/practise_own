
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
"""
def f(n: int) -> int:
    # dp = [0] * (n + 1)
    # dp[0] = dp[1] = 1
    # for i in range(2, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]
    #     print(dp)
    # return dp[-1]
    a = b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    print(f(3))
