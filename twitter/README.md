# wtb

WHO TO BLOCK

## 使用方法

从Twitter Settings - Blocked accounts选择import from list

## 如何贡献

### 基本要求

* Python 2.7.9+
* 全局翻墙（其实可以用API代理不过效果未知）
* 有效的Twitter Consumer Key/Secret，例如[这里](https://gist.github.com/mariotaku/5465786)

**或者**

显示Twitter ID的客户端 ;)

### 操作步骤

1. 调用 `obtain_token.py` to get an application only token to access twitter
2. Call `show_twitter_id.py [name or url]` to get target user's twitter id
3. Add this ID to desired CSV file
4. Make a pull request


## 文件介绍

| 文件名 | 描述 | 定义 |
| :--: | :--: | :--: |
| pink_\*.csv | 爱国小粉红 | 看起来像是平常微博的萌萌二次元，使用各种表情包 |
| wumao_\*.csv | 五毛 | 传统意义上的五毛 |


如果有更多的类型，欢迎做出贡献。比如挺转基因组、反转基因组、中医粉组、中医黑组、爆照组、秀恩爱组。本repo旨在建立一个开放的，中立（雾）的，订阅列表。
