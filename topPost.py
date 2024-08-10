import requests
import time
from datetime import datetime

url = "https://klpbbs.com/home.php?mod=magic&action=mybox&infloat=yes&inajax=1"

headers = {
    "Host": "klpbbs.com",
    # cookie
    "Cookie": "",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "zh-CN",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://klpbbs.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "iframe",
    "Referer": "https://klpbbs.com/thread-135877-1-1.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i",
    "Connection": "keep-alive"
}

data = {
    # formhash
    "formhash": "",
    "handlekey": "a_bump",
    "operation": "use",
    "magicid": "10",
    "tid": "135877",
    "usesubmit": "yes",
    "idtype": "tid",
    "id": "135877"
}

def use_bump_card():
    response = requests.post(url, headers=headers, data=data)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if response.status_code == 200:
        print(f"[{current_time}] 顶贴成功")
    else:
        print(f"[{current_time}] 顶贴失败")
        print(f"操作失败，状态码: {response.status_code}")

try:
    while True:
        use_bump_card()
        print("等待2小时...")
        time.sleep(7500)
except KeyboardInterrupt:
    print("脚本已终止")
