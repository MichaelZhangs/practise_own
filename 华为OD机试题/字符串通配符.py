import re
while True:
    try:
        str1 = input()#记录第一行
        str2 = input()#记录第二行
        str1 = list(str1)
        counter=0#初始判定值
        for i in range (len(str1)):
            if str1[i] == "*" and counter ==0:
                counter = 1#当为相隔后第一个*时，保留此*并继续
            elif str1[i] == "*" and counter ==1:#当后续依然为*时，去除多余*因为*本身代表0-n个，从而减小计算复杂度
                str1[i] = ""#比如最后一个例子“h*h*ah**ha*h**h***hha” 重复*太多复杂度太大
            else:
                counter=0#一旦不是连续的*则重置判定值
        str1=''.join(str1)#合并为str
        str1 = str1.lower()
        str2 = str2.lower()#不分大小写，统一小写处理
        str1=str1.replace('?', '[0-9 a-z]')#统一小写+数字，不能用\w因为\w包括下划线，别涂省事规规矩矩打上
        str1=str1.replace('*','[0-9 a-z]*')#统一小写+数字 *代表0或多个
        str1=str1.replace('.','\.' )#由于.本身代表匹配除换行符以外的任意字符，需要转义
        str1 = "^"+str1+"$"
        search = re.match(str1, str2)#这道题用match()，如果是要求匹配整个字符串，直到找到一个匹配的规则的字符串则用search()
        if search != None:
            print('true')
        else:
            print('false')
    except:
        break