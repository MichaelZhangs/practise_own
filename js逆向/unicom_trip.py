import requests
import execjs


def getData():
    # url = "https://unicom_trip.133.cn/api/v1/city/source-top/V0440300?date=20210301"
    # # url="https://unicom_trip.133.cn/api/v1/city/trip-top/V0440300?date=20200301"
    # headers  = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    # }
    # resp = requests.get(url=url, headers=headers)
    # encode_data = resp.text
    # print(encode_data)
    form_data = {
        "date": "20210403"
    }
    # encode_data = "eyJpdiI6Im94dGY4ZWFLdG16NFNDMnhPcWFTYlE9PSIsInZhbHVlIjoiZG9vamZpYitFWHJzd3dRdDNQZnVBSlBkM3FNRlBvaDBUcGhmbEdCaHBYRzZcL0VqRWQrOFk3VGR1akxFRStYU1NrM2ZyUUNZbUxiTlJJblRvTEpsc0p6SVZFVnZGV091MmlENkVENG0xeWJweVRycytheUc1Q2pGYjdPT2VudGpMZVl0Mk5Mbjl4XC9OdWgzMENXWnd5R0lNVzEra0dCazd0ZDRJWHltY0hieTI2XC9QbG9kSnJ1ZUVtVStBWkxpT1NvV0J4NDlWZFVRMGJsSWtrS3hHMzdaSHZwUTIyUlcwNnl4THRENmZ3Wm5nOTFkeGM1cXVwQzhPTWFKUEVYOUpjVGlqS0NBM1JNaUp3TjF6ZmZxeXNURXlEaFFLT2NcL25yeVRSMjdcL0tcL2w0b1ZzOTVyalBcL1VydE44NjF4QTM3VEJzRFRlQ2Exb0FrUDdleDRSaW52UVR3RSsyajl6UEdlSFBMMzNnbFJ2b0xxQnF3ZVFvaHE4UStyVWRaVHY5SHhpakR0ZWNiQUpqQTNIVTdxanZhOEpnK0Q4T2hsYXNhZFUwZmtuUlVEb1VJRnA0QmhZRnViMHhzV1JOZ0c0SXVYOGZcL1c0djVVKzVXVncwOEJpVG5sb21sc0t4dGx6ZnNzak5LcDdhYU5kRDlKc3dHbFZoeDZHWFFEM0h4Q1JhMEdNR2pDYjVZQ1pMQ3ZxVXdBVDg3c0MwM3p6VndSYkEwSnl0bSsyNVRCUzRUa1RLSEMwUzhuV1VmajJFMmdkZG41ZWw5cExseFpQZUphZElBSVpOeEo4aDJ3T0M1eVZwekNTc1E2WnU3NG9iMmxIa0dOXC9wM2RWTDhpNmRSb21BaGlpMFBoVXJ6RGNQZWpqSDczdFpQeHkwUEh5Z1BEYnhIZlYyRWlCWTVOQjliU3B5OXgra0l3RWhmK2FHdTVVaHNrZmFZaVBhRUFjM1dONEx3cWd2SFR0VHIxNHBhY2NJSVpyTGc2dk5KMENJcGFoNmplMUtsWndWTnNxUzdJT0J2UldxSTVYWENaRExMT05NWVF2SWJEQkd6b2F6NEJ4SW9wbVwvazRMSlVMb0F0ZmVGMDlvZUJHTTRUU0FQbWZuM0pvV1hBOGtlKzZ2Q1YxcmI2cGQzYm5Fc0V5Zjd1SUxSMWVpQmFoNVdFU0FDeWUrU2FLOWFJMlF0K1FOXC9ucTQ4d2pZbmc3MEVQQlBqeWZBbzRtSjJleXJpT2t3d1pETUxFZjF2bFNIOFhjNGV4UGExN0VxRnRBY0xQdHppdDZIQ2wzdlFBa28rNUdMVXVtcm1uQTBJZmpqMWN4WU4yc1Z4TGtrazRDbWVXbjJ6eDRleTdWMzE4OXFiY0l0cXA5b1VRcnk4QnZmT1JEQUNuVkxxa3lBNG5yZDRmWndTM3l3R3ZDXC9cL1poamdkXC8zMXUyTmFSY2NuOWw4eVZ1YVwvTjhjcEZ1MURYMTlqT3lnRG5WaEFKeUl0N1BISDI2Q3NwV08yYkRwVG9QYWRlQzltVm03ZFJzWkF0a3lvVGpvbDF3cmRObnc4d0lJRU81QjlFcUJsdDVFR3I1cHdGVFhwbXRtZlJRbDduQWMzS3ZPVXVKZGdvVUFPeERIMmdPYzJvRm5SRnJReFljYlNOT0FIMTRCUExIR2lcLzF2UW1tMUlJNnJqSGxYbWs2SklWOUJiRE5RMEpScHJaQmlvK1J3eXVuWVRLT1JsMFErejdcL2lweWNrUUxpbXRFM2FjaXc5bUNoN1ZpdHh3YmplYW15bURTbVVZVVk1Y3NTc2phb3l4Nm51VzdzNjBMM2JDVmV0bDQrbTlITDRlNUNRMHJqdThaXC93OFd2eXNHUnhRdGdHN3pldVwvdGs5TDBHNjRwRFdOUytkY0tVbU1jTEJ2S2pRUVRwdmgwSjJZZVZhUFFBPT0iLCJtYWMiOiI3YmE2MWI3MWViNGEwMTYzODJlMGJmODljOTQzNzUyYTkxY2E0NzQyNzU4MjVhODYzOGNhNDk5YWMyMjA1NjExIn0="
    encode_data = "eyJpdiI6IkhvSkoxR2ozbnhWZHEzR1BQejFWb2c9PSIsInZhbHVlIjoiakswU2UyM01FbjBnZDFRUlNZdWtQYWJZc2lzZzhCdm1UXC9NS0lMdmdrM3laVk5IaXRYXC9lSkVpOCtZRWRTcFFKWGEzV2l1SlNGektQSFowT3M1a0gxdWhka3lXM2RmSDNsZmJhcW5meWtIZ1NXQ3NBZVEzUWhpR2JQOEc4K0F1c2c0WVE1ZmN0WlZsSW94VEZGTnhNK3VjVmFHTnFWYXJ3OHp4U2VqbzQyaktpSFwvSVZoaDNDTUFJbFZaSlBBMjBSVnFKOXFWTVF1N1pXTUxpWlFMcWRiSDBrSGRZRXJvaXNpMUxuWGFWYmhtaz0iLCJtYWMiOiIwNjhiNGE3YzU2NzJhNzViMzU4OTVmNzE1M2ViNTJmMTliYzJjZDIzNGYxMzdiOTMzMzE2MDlmMjg0MDlmYzIzIn0="
    with open("./unicom.js", encoding="utf8") as f:
        js_code = f.read()
    value = execjs.compile(js_code).call("dataDecode", encode_data)
    print(value)
    # dic=value["data"]
    # print(dic)
    # with open("unicom.txt","a+", encoding="utf8" ) as f:
    #     for d in dic:
    #         f.write(json.dumps(d, ensure_ascii=False))
    #         f.write("\n")

getData()