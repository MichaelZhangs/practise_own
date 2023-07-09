import jieba

content = "小明毕业于清华大学， 现在在中国科学院计算所"

res = jieba.cut(content, True)
print(list(res))
print(type(res))

result = jieba.cut_for_search(content)
print(list(result))