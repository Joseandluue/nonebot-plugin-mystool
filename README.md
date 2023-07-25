基于[Ljzd-PRO/nonebot-plugin-mystool](https://github.com/Ljzd-PRO/nonebot-plugin-mystool)/v1.1.0修改:

add：
```
打码积分查询 
原神实时便笺阈值提醒推送
用户可自行更改便笺阈值（/账号设置）
```
modify：
```
×打码返回内容的获取对象
```


# mysTool - 米游社辅助工具插件

## 📣 更新内容
### 2023.7.23 - v1.1.0
- 增加崩坏：星穹铁道的便笺功能 #140 #143 by @Joseandluue @RemiDre
    > 说明文档：[🔗星穹铁道实时便笺](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Information-StarRailStatus)
- 修复每小时都发送便笺通知的Bug #135
- 人机验证打码平台支持自定义JSON内容 #133
    > 说明文档：[🔗geetest_json](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Configuration-Preference#geetest_json)
- 修复商品兑换API #110
- 不在好友列表的用户数据在删除前将进行备份 #129
    > 备份目录：`data/nonebot_plugin_mystool/deletedUsers`
- 防止因插件数据文件中默认存在 device_config, salt_config 而导致更新后默认配置被原配置覆盖的问题
- 若需要修改 device_config 配置，修改后还设置插件数据文件中 preference.override_device_and_salt 为 true 以覆盖默认值
    > 说明文档：
    > - [🔗网络请求设备信息 `class DeviceConfig`](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Configuration-DeviceConfig)
    > - [🔗override_device_and_salt](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Configuration-Preference#override_device_and_salt)
- 增加了是否使用多进程生成商品图片的配置项 `good_list_image_config`.`MULTI_PROCESS`，如果遇到生成图片失败可以尝试关闭该项
- 在兑换开始后的一段时间内不断尝试兑换，直到成功 #110
- 兑换开始后将不会延迟兑换，用户数据文件中 `preference.exchange_latency` 将作为同一线程下每个兑换请求之间的时间间隔 #110
- 兑换请求日志内容增加了发送请求时的时间戳




### [📃源码说明](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Source-Structure)
### 适配 [绪山真寻Bot](https://github.com/HibiKier/zhenxun_bot) 的分支
- https://github.com/MWTJC/zhenxun-plugin-mystool
- https://github.com/ayakasuki/nonebot-plugin-mystool
