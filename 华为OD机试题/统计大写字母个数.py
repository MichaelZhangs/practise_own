import re
while True:
    try:
        s = input()
        s_list = re.findall(r'[A-Z]', s)
        print(len("".join(s_list)))
    except:
        break