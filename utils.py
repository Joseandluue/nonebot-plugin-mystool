import random
import string

USER_AGENT_MOBILE = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.25.1"
"""移动端 User-Agent"""
USER_AGENT_PC = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
"""桌面端 User-Agent"""
X_RPC_DEVICE_MODEL = "OS X 10.15.7"
"""Headers所用的 x-rpc-device_model"""
X_RPC_DEVICE_NAME = "Microsoft Edge 103.0.1264.62"
"""Headers所用的 x-rpc-device_name"""
UA = "\".Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"103\", \"Chromium\";v=\"103\""
"""Headers所用的 sec-ch-ua"""


def generateDeviceID() -> str:
    """
    生成随机的x-rpc-device_id
    """
    return "".join(random.sample(string.ascii_letters + string.digits,
                                 8)).lower() + "-" + "".join(random.sample(string.ascii_letters + string.digits,
                                                                           4)).lower() + "-" + "".join(random.sample(string.ascii_letters + string.digits,
                                                                                                                     4)).lower() + "-" + "".join(random.sample(string.ascii_letters + string.digits,
                                                                                                                                                               4)).lower() + "-" + "".join(random.sample(string.ascii_letters + string.digits,
                                                                                                                                                                                                         12)).lower()


def cookie_str_to_dict(cookie_str: str) -> dict[str, str]:
    """
    将字符串Cookie转换为字典Cookie
    """
    cookie_str = cookie_str.replace(" ", "")
    # Cookie末尾缺少 ; 的情况
    if cookie_str[-1] != ";":
        cookie_str += ";"

    cookie_dict = {}
    start = 0
    while start != len(cookie_str):
        mid = cookie_str.find("=", start)
        end = cookie_str.find(";", mid)
        cookie_dict.setdefault(cookie_str[start:mid], cookie_str[mid + 1:end])
        start = end + 1
    return cookie_dict


def cookie_dict_to_str(cookie_dict: dict[str, str]) -> str:
    """
    将字符串Cookie转换为字典Cookie
    """
    cookie_str = ""
    for key in cookie_dict:
        cookie_str += (key + "=" + cookie_dict[key] + ";")
    return cookie_str