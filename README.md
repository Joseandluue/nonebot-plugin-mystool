# 套套适配方式

### 一、

修改`get_validate`函数部分代码

```
    try:
        async for attempt in get_async_retry(retry):
            with attempt:
                async with httpx.AsyncClient() as client:
                    res = await client.post(
                        geetest_url,
                        params=params,
                        json=content,
                        timeout=60
                    )
                geetest_data = res.json()
                logger.debug(f"{plugin_config.preference.log_head}验证初步提交：{geetest_data}")
                content_v2 = {'appkey': content['appkey']}
                content_v2['resultid'] = (geetest_data['resultid'])
                logger.info('等待识别时间中')
                time.sleep(6) 
                async with httpx.AsyncClient() as client:
                    res = await client.post(
                        'http://api.ttocr.com/api/results',
                        json=content_v2,
                        timeout=60
                    )
                geetest_data_v2 = res.json()
                logger.debug(f"{plugin_config.preference.log_head}人机验证结果：{geetest_data_v2}")
                validate = geetest_data_v2['data']['validate']
                seccode = geetest_data_v2['data'].get('seccode') or f"{validate}|jordan"
                return GeetestResult(validate=validate, seccode=seccode)
    except tenacity.RetryError:
        logger.exception(f"{plugin_config.preference.log_head}获取人机验证validate失败")
```


！需要注意的是插件中人机验证的用户变量暂未适配套套，套套目前只能使用全局变量进行人机验证



### 二、

[后端](https://github.com/Sakamakiiizayoi/ttocr_auto/tree/main)  (省事)

