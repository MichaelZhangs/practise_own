while True:
        try:
            num = int(input().strip())
            md = {}
            for i in range(num):
                key, value = map(int, input().strip().split(" "))
                md[key] = md.get(key, 0) + value
            for i in sorted(md):  # 重点在sorted()方法对字典排序，否则会报错，我栽在这上面了-。-
                print(i, md[i])
        except:
            break