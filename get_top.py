import requests
import json
import os
import pickle


top_song_url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?tpl=3&page=detail&date=2019_00&topid=6&' \
                   'type=top&song_begin={}&song_num=30&g_tk=1039240975&loginUin=416893374&hostUin=0&format=json&' \
                   'inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'  # 港台排行榜
ip_poor = ['119.146.2.234', '219.234.5.128']
header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/{} Safari/'
                        '535.24'.format(ip_poor[0])}


def is_end(url, header):  # 判断末页
    ct = requests.get(url, headers=header)
    json_obj = ct.text
    j = json.loads(json_obj)
    # print(j)
    if j['data']['list']:
        return False
    else:
        return True


os.chdir("C:/Users/summer/Desktop/点歌系统/排行榜")
begin = 0
top_list = []
while begin <= 90:
    url = top_song_url.format(begin)
    ct = requests.get(url, headers=header)
    ct = json.loads(ct.content)
    for i in ct['songlist']:
        top_list.append([i['data']['songname'], i['data']['songmid'], i['data']['singer'][0]['name']])
    begin += 30
with open('港台排行榜.sj','ab') as f:
    pickle.dump(top_list, f)
# print(top_list)
# print(len(top_list))
