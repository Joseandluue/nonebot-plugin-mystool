## Changelog

### 更新内容

#### 💡 新特性
- 新增日志提示推送超话兑换码信息 - by @Joseandluue
- 适配微博多账号 - by @Joseandluue
- 改进人机验证日志输出 (#299)

#### 🐛 修复
- **修复较新版本的 nonebot2 导入插件失败的问题**
- 补充插件元数据以符合 nonebot 规定
- 微博超话兑换码相关代码优化 - by @Joseandluue
- Windows 下默认不使用多进程生成商品图片 (#282)
- 修复删除兑换计划出错的问题 (#297)

#### 🔧 杂项
- 替换所有 Workflow 文件，新增插件测试，通过 CI 自动检查插件能否导入成功

### 更新方式

如果使用的是镜像源，可能需要等待镜像源同步才能更新至最新版

- 使用 nb-cli 命令：
  ```
  nb plugin update nonebot-plugin-mystool
  ```

- 或 pip 命令（如果使用了虚拟环境，需要先进入虚拟环境）：
  ```
  pip install --upgrade nonebot-plugin-mystool
  ```

### 兼容性

- `>=v2.0.0` 为 `configV2.json`, `dataV2.json`, `.env` 文件，如果存在 V1 版本的文件，**会自动备份和升级**
- `>=v1.0.0, <v2.0.0` 插件配置/数据包含于 `plugin_data.json`
- `< v1.0.0` 插件配置文件为 `pluginConfig.json`

**Full Changelog**: https://github.com/Ljzd-PRO/nonebot-plugin-mystool/compare/v2.4.0…v2.5.0