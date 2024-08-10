import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

# 事先准备好clash core，并打开web ui切换到全局节点组
# Clash API地址
clash_api_url = ""

# 代理组名称
proxy_group = ""

# 推广链接
url = ""

def get_proxy_nodes(proxy_group):
    url = f"{clash_api_url}/proxies/{proxy_group}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            proxies = response.json().get("all", [])
            return proxies
        else:
            print(f"获取代理组失败 - 状态码: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"获取代理组时发生错误: {e}")
        return []

def get_current_node(proxy_group):
    url = f"{clash_api_url}/proxies/{proxy_group}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            current_node = response.json().get("now", "")
            return current_node
        else:
            print(f"获取当前节点失败 - 状态码: {response.status_code}")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"获取当前节点时发生错误: {e}")
        return ""

def switch_to_next_node(proxy_group, nodes, current_index):
    next_index = (current_index + 1) % len(nodes)
    node_name = nodes[next_index]
    url = f"{clash_api_url}/proxies/{proxy_group}"
    payload = {
        "name": node_name
    }
    try:
        response = requests.put(url, json=payload)
        if response.status_code == 204:
            print(f"成功切换到节点: {node_name}")
        else:
            print(f"切换节点失败: {node_name} - 状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"切换节点时发生错误: {e}")
    return next_index

def apply_task():
    url = "https://klpbbs.com/home.php?mod=task&do=apply&id=1"
    headers = {
        "Host": "klpbbs.com",
        # cookie
        "Cookie": "",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Accept-Language": "zh-CN",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://klpbbs.com/home.php?mod=task&item=new",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    try:
        response = requests.get(url, headers=headers)
        if "任务申请成功" in response.text:
            print("成功领取任务")
            return True
        else:
            print("领取任务失败")
            return False
    except requests.exceptions.RequestException as e:
        print(f"领取任务时发生错误: {e}")
        return False

def claim_task_reward():
    url = "https://klpbbs.com/home.php?mod=task&do=draw&id=1"
    headers = {
        "Host": "klpbbs.com",
        # cookie
        "Cookie": "",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Accept-Language": "zh-CN",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://klpbbs.com/home.php?mod=space&do=notice&view=system",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    try:
        response = requests.get(url, headers=headers)
        if "请注意查收" in response.text:
            print("成功领取任务奖励")
            return True
        else:
            print("领取任务奖励失败")
            return False
    except requests.exceptions.RequestException as e:
        print(f"领取任务奖励时发生错误: {e}")
        return False

def open_link_in_incognito(url):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    # 这里调整强制关闭浏览器时间，现在是20s
    driver.set_page_load_timeout(20)  
    try:
        driver.get(url)
        time.sleep(1)
    except TimeoutException:
        print("页面加载超时，强制关闭浏览器")
    finally:
        driver.quit()

def main():
    nodes = get_proxy_nodes(proxy_group)
    if not nodes:
        print("无法获取代理节点列表")
        return
    current_node = get_current_node(proxy_group)
    if not current_node:
        print("无法获取当前节点")
        return
    try:
        current_index = nodes.index(current_node)
    except ValueError:
        print("当前节点不在代理节点列表中")
        return
    while True:
        if apply_task():
            time.sleep(1)  
            if claim_task_reward():
                print("任务成功完成，暂停1小时5分钟后再继续")
                time.sleep(3900)  
            else:
                print("奖励领取失败，继续切换节点")
                current_index = switch_to_next_node(proxy_group, nodes, current_index)
                open_link_in_incognito(url)
                time.sleep(1)  
        else: 
            print("领取任务失败，可能是已经领取")
            time.sleep(1)  
            if claim_task_reward():
                print("任务成功完成，暂停1小时5分钟后再继续")
                time.sleep(3900)  
            else:
                print("奖励领取失败，继续切换节点")
                current_index = switch_to_next_node(proxy_group, nodes, current_index)
                open_link_in_incognito(url)
                time.sleep(1)  
if __name__ == "__main__":
    main()
