# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/3/17 10:11 AM
# @File    : login.py
import browsercookie
import browser_cookie3
import requests
import click
import time
from requests.packages import urllib3
urllib3.disable_warnings()


# chrome_cookie = browsercookie.chrome()
chrome_cookie = browser_cookie3.chrome()
# chrome_cookie = browsercookie.safari()
cookie_hit = ["cmdb.win.oa.com", ".oa.com"]
# cookie_hit = ["ops.xiaoying.io"]
send_cookie = dict()
for cookie in chrome_cookie:
    if cookie.domain in cookie_hit:
        send_cookie[cookie.name] = cookie.value

# print(send_cookie) 

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json',
    'Origin': 'http://cmdb.win.oa.com',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://cmdb.win.oa.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


url = "http://cmdb.win.oa.com/api/v1/jms/host/apply/"


@click.command()
@click.argument("ip_list", nargs=-1)
def apply_ip_login(ip_list):
    if len(ip_list) <= 0:
        raise Exception("ip_list error:[%s]" % ip_list)
    req_json = {
        "user": "user_00",
        # "ips": "10.0.194.56\n10.0.121.208",
        "ips": "\n".join(ip_list),
        "action": 31,
        "time": "halfday",
        "remark_type": "下载文件",
        "remark": "X"
    }
    resp = requests.post(url, cookies=send_cookie, json=req_json, headers=headers)

    try:
        resp_json = resp.json()
        if resp_json["code"] != 0:
            print(resp_json)
            raise Exception("申请权限失败:[]" % resp.content)
        else:
            print("申请成功:\n%s" % req_json["ips"])
            time.sleep(1)
    except Exception as e:
        print(resp.content)
        raise e


if __name__ == '__main__':
    # pass
    apply_ip_login()
    
