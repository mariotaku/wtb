# Twidere 过滤列表

## 列表介绍

* `bots.xml`：机器人推文，如果你发现某个来源经常自动发送推文，可以添加到这里。
* `harassment.xml`：使用提及、私信等骚扰用户，尤其是骚扰大量用户的。添加前请一定提供证据。

## 如何导入
在 Twidere - 过滤 - 设定 中添加订阅（功能待定）

## 文件格式

````xml
<?xml version="1.0" encoding="utf-8"?>
<filters>
    <-- key 为 "数字id@twitter.com" 的格式，name 即为名字， screenName 即为 @用户名。 -->
	<user key="[numericalId]@twitter.com" name="User name" screenName="screenName" />
</filters>
````