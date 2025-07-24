# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/10/17 17:50
# @File    : qiandao.py
import requests

# curl 'https://chat.link-ai.tech/api/chat/web/app/user/sign/in' \
#   -H 'Accept: application/json, text/plain, */*' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI0MTY0IiwiaWF0IjoxNjk3NTM2MDg4LCJleHAiOjE2OTgxNDA4ODh9.inVlLNzLMRsmJPrMdqpB9Gym1ZMInD1m_Zov5WH81BpgYEX7Vp2HBigM3K6fTPFZleIsSwG4ieE1dE_M8JCtVQ' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: https://chat.link-ai.tech/console/account' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   --compressed



token = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI0MTY0IiwiaWF0IjoxNjk3NTM2MDg4LCJleHAiOjE2OTgxNDA4ODh9.inVlLNzLMRsmJPrMdqpB9Gym1ZMInD1m_Zov5WH81BpgYEX7Vp2HBigM3K6fTPFZleIsSwG4ieE1dE_M8JCtVQ"
login_token = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI0MTY0IiwiaWF0IjoxNjk3NTM2MDg4LCJleHAiOjE2OTgxNDA4ODh9.inVlLNzLMRsmJPrMdqpB9Gym1ZMInD1m_Zov5WH81BpgYEX7Vp2HBigM3K6fTPFZleIsSwG4ieE1dE_M8JCtVQ"



class LinkAI(object):
    def __init__(self):
        self.session = requests.session()
        self.auth_token = ""

    def login(self):
        url = "https://chat.link-ai.tech/api/login"
        username = "17621584633"
        password = "helei0123456"
        data = {"username": username, "password": password}
        headers = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        resp = self.session.post(url, headers=headers, data=data)
        resp_data = resp.json()
        if resp_data["code"] == 200 and resp_data["success"] is True:
            self.auth_token = "Bearer " + resp_data["data"]["token"]
        else:
            print(resp_data)
            raise Exception("登录失败")

    def sign(self):
        url = "https://chat.link-ai.tech/api/chat/web/app/user/sign/in"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": self.auth_token,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        print(headers)
        resp = self.session.get(url, headers=headers)
        resp_data = resp.json()
        if resp_data["code"] == 200 and resp_data["success"] is True:
            print("签到成功")
        else:
            print(resp_data)
            raise Exception("签到失败")


if __name__ == '__main__':
    link = LinkAI()
    link.login()
    link.sign()
