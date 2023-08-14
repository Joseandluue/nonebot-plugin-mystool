基于[Ljzd-PRO/nonebot-plugin-mystool](https://github.com/Ljzd-PRO/nonebot-plugin-mystool)/v1.2.3修改:

add：
```
rrocr积分查询 
```
modify：
```
打码返回内容的获取对象 
```
  > 修改的签到代码 from @Night-stars-1 [mystool](https://github.com/Night-stars-1/nonebot-plugin-mystool)

fix：
```
（待重新测试）v1.5经测试便笺自动检查推送相关有问题，当matcher='None'时，无法触发条件
    v1.6中便笺自动推送改为Ljzd-PRO/nonebot-plugin-mystoo/v1.01版本使用的BOT模块
```


# mysTool - 米游社辅助工具插件

## 📣 更新内容
### 2023.8.14 - v1.2.3
- 修复新用户无法正常使用登录功能的问题 #162
- 优化登录操作中DeviceID相关
- 修复可能存在重复的用户数据对象导致判断当前用户数有误的问题
- 修复用户数据绑定时QQ频道相关操作Bug
- 修复用户绑定功能部分响应文本显示不全的问题
- 改进生成的二维码风格
- 增加短信验证码发送失败返回的错误类型识别
- 修复 v1.2.2 无法使用登录功能的Bug

### 2023.8.13 - v1.2.1
- 在无需人机验证的情况下，登录操作时将自动发送短信验证码
- 修复登录功能无法正常使用的问题 #158
- 修复启动时如果插件数据中含有已失效的兑换计划会导致运行出错的问题
- 修复游戏签到尝试完成人机验证任务时，发送提示消息失败的问题 #159

## 功能和特性

- 支持QQ聊天和QQ频道
- 短信验证登录，免抓包获取 Cookie
- 自动完成每日米游币任务
- 自动进行游戏签到
- 可制定米游币商品兑换计划，到点兑换（因加入了人机验证，成功率较低）
- 可支持多个 QQ 账号，每个 QQ 账号可绑定多个米哈游账户
- QQ 推送执行结果通知
- 原神、崩坏：星穹铁道状态便笺通知

## 使用说明

### 🛠️ NoneBot2 机器人部署和插件安装

请查看 -> [🔗Installation](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Installation)

### 📖 插件具体使用说明

请查看 -> [🔗Wiki 文档](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki)

### ❓ 获取插件帮助信息

#### 插件命令

```
/帮助
```

> ⚠️ 注意 此处没有使用 [🔗 插件命令头](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Configuration-Config#commandstart)

## 其他

### 贡献
<a href="https://github.com/Ljzd-PRO/nonebot-plugin-mystool/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Ljzd-PRO/nonebot-plugin-mystool&max=1000" alt="贡献者"/>
</a>

### 源码说明
[📃Source-Structure](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Source-Structure)

### 适配 [绪山真寻Bot](https://github.com/HibiKier/zhenxun_bot) 的分支
- https://github.com/MWTJC/zhenxun-plugin-mystool
- https://github.com/ayakasuki/nonebot-plugin-mystool
