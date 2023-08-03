import json
import requests

cookie = "x_host_key_access=41e1a43afc6bc6ee33aae990f5d3a3cb12a59d20_s; x-client-ssid=1864d9cc290-a459db0e65d412fe2488224716860b91af6a8a7d; TCOA_TICKET=TOF4TeyJ2IjoiNCIsInRpZCI6InB3WmY3ZUM3bUM4SmNjNHdJWlNqcFVQRk1lcGo4alF5IiwiaXNzIjoiMTAuOTkuMjA4LjYxIiwiaWF0IjoiMjAyMy0wMy0wN1QxMTowNDoyNC42NTQ3MDQ5NTYrMDg6MDAiLCJhdWQiOiIxMC44Ny4zOC4zNyIsImhhc2giOiI5ODI0RDM0RUU3MUEwMTM5OUM4QzM1NTEyMkJFNDhFNTAwOTFBMUQ4Q0Q1NjVEMDU1RDYxQjc5RDI1QTQyNEE0IiwibmgiOiJDNzI5QThENEZGMzhBQ0MzOTlBOTVDNDk0NzhEOUE4QTRFRDJEMzUzMzA1MjA2NDhDOTU0NzlGQjdDN0JGMDA5In0; TCOA=pwZf7eC7mC8Jcc4wIZSjpUPFMepj8jQy; RIO_TCOA_TICKET=tof:TOF4TeyJ2IjoiNCIsInRpZCI6InB3WmY3ZUM3bUM4SmNjNHdJWlNqcFVQRk1lcGo4alF5IiwiaXNzIjoiMTAuOTkuMjA4LjYxIiwiaWF0IjoiMjAyMy0wMy0wN1QxMTowNDoyNC42NTQ3MDQ5NTYrMDg6MDAiLCJhdWQiOiIxMC44Ny4zOC4zNyIsImhhc2giOiI5ODI0RDM0RUU3MUEwMTM5OUM4QzM1NTEyMkJFNDhFNTAwOTFBMUQ4Q0Q1NjVEMDU1RDYxQjc5RDI1QTQyNEE0IiwibmgiOiJDNzI5QThENEZGMzhBQ0MzOTlBOTVDNDk0NzhEOUE4QTRFRDJEMzUzMzA1MjA2NDhDOTU0NzlGQjdDN0JGMDA5In0"

def request_post(url, param):
    global text
    fails = 0
    while True:
        try:
            if fails >= 5:
                break

            headers = {'cookie': cookie, 'content-type': 'application/json;charset=utf8'}
            ret = requests.post(url, json=param, headers=headers, timeout=10)

            if ret.status_code == 200:
                text = json.loads(ret.text)
            else:
                continue
        except:
            fails += 1
            print('网络连接出现问题, 正在尝试再次请求: ', fails)
        else:
            break
    return text
