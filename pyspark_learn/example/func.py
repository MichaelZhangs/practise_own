#conding:utf8
import jieba


def context_jieba(content):
    seq = jieba.cut_for_search(content)
    lst = []
    for word in seq:
        lst.append(word)
    return lst

def filter_words(data):
    """ 过滤 谷 帮 客"""
    return data not in ["谷", "帮", "客"]

def append_words(data):
    if data == "传智播":
        data = "传智播客"
    if data == "院校":
        data = "院校帮"
    if data == "博学":
        data = "博学谷"
    return (data, 1)

def extract_user_word(data):
    # data --> (1, "content")
    user_id = data[0]
    content = data[1]
    words = context_jieba(content)
    lst = []
    for word in words:
        # 过滤
        if filter_words(word):
            lst.append( (user_id+"_"+ append_words(word)[0], 1))

    return lst