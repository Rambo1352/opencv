import requests
import json


# 获取access_token
#https请求方式: GET
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET


class wxTool():
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret

    def get_access_token(self):
        url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}'
        resp = requests.get(url).json()
        access_token = resp.get('access_token')
        print(access_token)
        return access_token

    def post_data(self, open_id, msg='有人非法闯入'):
        url = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={self.get_access_token()}'
        req_data = {
            "touser": open_id,
            "msgtype": "text",
            "text":
                {
                    "content": msg
                }
        }
        res = requests.post(url, data=json.dumps(req_data, ensure_ascii=False).encode('utf-8'))
        print(res)






# 利用access_token发送通知

# http请求方式: POST
# https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN




if __name__ == '__main__':
    app_id = 'wxad038f4b72518a75'
    app_secret = '3d1f73d4cadf65871f67faecab1803cb'
    wx_tool = wxTool('wxad038f4b72518a75', '3d1f73d4cadf65871f67faecab1803cb')
    wx_tool.post_data('oyptN63RmNTWDkqwsU-0X11GT748')

