
def f(haystack: str, needle:str) -> int:
    if not needle:
        return 0
    for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
    return -1
if __name__ == '__main__':
    s = "abc"
    c = "c"
    print(f(s, c))