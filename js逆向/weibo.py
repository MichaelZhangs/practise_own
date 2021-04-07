import requests
def weibo():
    url = "https://weibo.com/tv/api/component?page=%2Ftv%2Fhome&n=4&m=home"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "x-xsrf-token": "rF6usqRbJBNM01cVWebjB2kR",
        "referer": "https://weibo.com/tv/home"
    }
    data = {"Component_Home_Recommend": {"next_cursor": 1}}
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)

weibo()