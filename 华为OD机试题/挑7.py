def select_sev():
    while True:
        try:
            n = int(input())
            count = 0
            for i in range(1,n + 1):
                if "7" in str(i) or i % 7 == 0:
                    count += 1
            print(count)
        except:
            break
select_sev()