#coding:utf8
import json
import pandas

def read_js():
    pd = pandas.read_json('../test_data/info.json')
    print(pd)
def read_js2():
    with open('../test_data/address.json', encoding='utf-8') as f:
        for line in f:
            line_js = line.strip()
            # print(line_js)
            d = json.loads(line_js)
            print(d)






if __name__ == '__main__':
    read_js2()