import os
import time
import sys
import requests
POP20_CC = ("CN IN US ID BR PK NG  BD RU JP "
            "MX PH VN ET EG DE IR TR CD FR").split()
BASE_URL = "http://flupy.org/data/flags"
BASE_DIR = "./downloads/"

def save_flag(img, filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path,"wb") as fp:
        fp.write(img)

def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return  resp.content

def show(text):
    print("=====")
    print(text, end=" ")
    sys.stdout.flush()

def dowload_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = dowload_many(POP20_CC)
    print("count=", count)
    end = time.time() - t0
    print("--->",end)
#     76.42522954940796 s
if __name__ == '__main__':
    main(dowload_many)



