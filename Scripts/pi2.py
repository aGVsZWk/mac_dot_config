# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/8/21 15:07
# @File    : pi2.py
import requests
import re
import os

cpolar_username = "qq905713813@163.com"
cpolar_password = "qwera1234"
ssh_username = "luke"
ssh_password = "1234"


def get_tcp_address(username, password):
    session = requests.session()
    login_page_url = "https://dashboard.cpolar.com/login"

    resp = session.get(login_page_url)
    result = re.search(r".*<input.+?name=\"csrf_token\".+?value=\"(.+?)\"", resp.text)

    csrf_token = result.group(1)

    data = {
        "login": username,
        "password": password,
        "csrf_token": csrf_token
    }
    resp = session.post(login_page_url, data=data)
    status_url = "https://dashboard.cpolar.com/status"
    resp = session.get(status_url)
    result = re.search(r"https://(.+?)\.vip\.cpolar\.cn</a>", resp.text)
    url = result.group(0).split("\"")[0]
    print(url)

    # print(session.get(url).text)
    return url


url = get_tcp_address(cpolar_username, cpolar_password)

