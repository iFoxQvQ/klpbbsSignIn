# klpbbsSignIn
苦力怕论坛自动推广/顶贴脚本

特别说明

## 特别说明

仅供学习参考，请下载后于24h内删除

## 安装

直接下载源码即可

## 修改配置

### topPost.py

您需要在 line 10 填上您在 苦力怕论坛 的 cookie 

**获取方法**

1. 打开苦力怕论坛
2. 登录自己的账号
3. 打开 f12 开发工具
4. 打开网络一栏，刷新后选择 `klpbbs.com` 下拉复制 cookie

![image-20240811094959437](https://s2.loli.net/2024/08/11/ItSNCmwLJHlvMqU.png)

您需要在 line 32 填入您在 苦力怕论坛 的 formhash

**获取方法**

1. 打开苦力怕论坛
2. 登录自己的账号
3. 打开 f12 开发工具
4. 打开网络一栏，刷新后按 `ctrl f` 搜索 `fromhash` 点击第一个结果后即可在 响应 部分找到 formhash

![image-20240811095223168](https://s2.loli.net/2024/08/11/SlDCKBPQfj8A47z.png)

### promotion

您需要事先准备好 clash verge

[clash-verge-rev/clash-verge-rev: Continuation of Clash Verge - A Clash Meta GUI based on Tauri (Windows, MacOS, Linux) (github.com)](https://github.com/clash-verge-rev/clash-verge-rev)

自备多节点，打开web ui，然后选择你想要使用的代理组，记得开全局，或者是自行写分流规则

![image-20240811095600232](https://s2.loli.net/2024/08/11/2THYgtQyAIu156j.png)

line 10 处填写 clash api 地址，通常是

```
http://127.0.0.1:9097
```

line 13 处填写您的 代理组名称

line 16 处填写您的 苦力怕论坛推广链接

**获取方法**

[访问推广 - Minecraft(我的世界)苦力怕论坛 (klpbbs.com)](https://klpbbs.com/home.php?mod=spacecp&ac=promotion)

line 68 和 line101 处填写您的 苦力怕论坛cookie 获取方法同上面所述

line 134 处可以修改 页面加载最长时间 ，原因是访问链接时只要有页面出现即可增加推广量，避免浪费时间可以自行调整，默认 20s

