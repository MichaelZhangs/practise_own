from typing import List
def f(digits: str) -> List[str]:
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    if digits == '':
        return []
    s = []
    for i in digits:
        s.append(phoneMap[i])
    import itertools
    res = []
    for i in itertools.product(*s):  # *s对列表s进行解压入参,获取所有排列组合
        res.append(''.join(i))
    return res

def g(digits: str) -> List[str]:
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    product = ['']
    for k in digits:
        product = [i + j for i in product for j in phoneMap[k]]
    return product

if __name__ == '__main__':
    digits = "234"
    print(g(digits))



