import requests

cookies = {
    'PS_DEVICEFEATURES': 'width:1920 height:1200 pixelratio:1 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0',
    'authAppCode': '',
    '_csrf': '7d6vdT4hv0W1MZWNjAj8w9vYqZMA_OFF',
    'uid': 'lei.he%40yingzt.com',
    'stoken': '%7B%22prod%22%3A%229WRVQUPVLMCX%22%7D',
    'PHPSESSID': 'per5alprj9f23j5tmo9ia8ub30',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json',
    # 'Cookie': 'PS_DEVICEFEATURES=width:1920 height:1200 pixelratio:1 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; authAppCode=; _csrf=7d6vdT4hv0W1MZWNjAj8w9vYqZMA_OFF; uid=lei.he%40yingzt.com; stoken=%7B%22prod%22%3A%229WRVQUPVLMCX%22%7D; PHPSESSID=per5alprj9f23j5tmo9ia8ub30',
    'Origin': 'http://cmdb.win.oa.com',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://cmdb.win.oa.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

json_data = {
    'user': 'user_00',
    'ips': '10.90.77.9',
    'action': 31,
    'time': 'halfday',
    'remark_type': '下载文件',
    'remark': 'X',
}

response = requests.post(
    'http://cmdb.win.oa.com/api/v1/jms/host/apply/',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
