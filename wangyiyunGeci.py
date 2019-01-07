# -*- coding:utf-8 -*-
import requests
import json
import re
lrc_url = 'http://music.163.com/api/song/lyric?id=191232+&lv=1&kv=1&tv=-1'
lyric = requests.get(lrc_url)
print(lyric.text)
json_obj = lyric.text
j = json.loads(json_obj)
lrc = j['lrc']['lyric']
# pat = re.compile(r'\[.*\]')
pat = re.compile(r'\[(.*?)\]')
# content = re.findall(pat, lrc)
# print(content)
lrc = re.sub(pat, "", lrc)
lrc = lrc.strip()
print(lrc)
