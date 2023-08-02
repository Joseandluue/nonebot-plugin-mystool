基于[Ljzd-PRO/nonebot-plugin-mystool](https://github.com/Ljzd-PRO/nonebot-plugin-mystool)/dev/v1.2.0-beta.1修改:

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
v1.5经测试便笺自动检查推送相关有问题，当matcher='None'时，无法触发条件
    v1.6中便笺自动推送改为Ljzd-PRO/nonebot-plugin-mystoo/v1.01版本使用的BOT模块
```


# mysTool - 米游社辅助工具插件

## 📣 更新内容

### 2023.7.28 - v1.2.0-beta.1
- 增加对QQ频道的支持 #128
  > 说明文档：[🔗QQGuild 适配器](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Installation#QQGuild-适配器)
- 增加用户数据绑定关联功能（如QQ频道账号与QQ聊天账号的数据绑定）
  > 说明文档：[🔗用户数据绑定关联](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Information-UserBind)
- 增加原神便笺树脂提醒阈值的设置选项 #151 by @Joseandluue
  > 说明文档：[🔗对绑定的某个米哈游账户进行设置](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Information-Setting#%E5%AF%B9%E7%BB%91%E5%AE%9A%E7%9A%84%E6%9F%90%E4%B8%AA%E7%B1%B3%E5%93%88%E6%B8%B8%E8%B4%A6%E6%88%B7%E8%BF%9B%E8%A1%8C%E8%AE%BE%E7%BD%AE)
- 修复 `preference.override_device_and_salt` 关闭无效的问题


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
