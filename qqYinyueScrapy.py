# -*- coding:utf-8 -*-
import requests
import re
import json
import os
import pickle


def get_page_songs_info(url, name, area_code, header):  # 获取每页的歌曲信息
    ct = requests.get(url, headers=header)
    json_obj = ct.text
    j = json.loads(json_obj)
    songs_name = []
    page_songs_info = []
    for song in j['data']['list']:
        song_name = song['musicData']['songname']  # 歌名
        song_mid = song['musicData']['songmid']  # 曲链编号
        song_link = 'https://y.qq.com/n/yqq/song/' + song_mid + '.html'  # 歌曲链接
        singers = song['musicData']['singer']
        song_album_mid = song['musicData']['albummid']
        song_album_name = song['musicData']['albumname']
        singer_name = []
        songs_name.append(song_name)
        for singer in singers:  # maybe 合唱
            singer_name.append(singer['name'])
        song_info = [song_name, singer_name, song_link, area_code, song_album_mid, song_album_name]
        page_songs_info.append(song_info)
    # singer_name = j['data']['list'][0]['musicData']['singer'][0]['name']  # 歌手
    print('songs_name: {}'.format(songs_name))
    # print('songs_info: {}'.format(page_songs_info))
    # infos = []
    # print(page_songs_info)
    return page_songs_info


def is_end(url, header):  # 判断末页
    ct = requests.get(url, headers=header)
    json_obj = ct.text
    j = json.loads(json_obj)
    # print(j)
    if j['data']['list']:
        return False
    else:
        return True


def get_all_singers(url, header):  # 获取所有歌手的mid

    content = requests.get(url, headers=header)

    json_object = content.text
    j = json.loads(json_object)
    singers_info_list = j['singerList']['data']['singerlist']
    singers_list = []
    singers_mid_list = []
    for singer in singers_info_list:
        singer_name = singer['singer_name']
        singer_mid = singer['singer_mid']
        singers_list.append([singer_name, singer_mid])
        singers_mid_list.append(singer_mid)

    return singers_list


if __name__ == '__main__':
    # {增量80}{页数}
    singers_page_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getUCGI18199371139067178&g_tk=5381&' \
                       'jsonpCallback=getUCGI18199371139067178&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8' \
                       '&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&' \
                       'data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A10000%7D%2C%22singerList%22%3A%7B%22' \
                       'module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22' \
                       'get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22' \
                       'genre%22%3A-100%2C%22index%22%3A-100%2C%22sin%22%3A{}%2C%22cur_page%22%3A{}%7D%7D%7D'

    singers_page_url2 = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI49096072855637685&g_tk=5381&loginUin=0&' \
                        'hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&' \
                        'needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A10000%7D%2C%22singerList%' \
                        '22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%' \
                        '22%2C%22param%22%3A%7B%22area%22%3A5%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%' \
                        '3A-100%2C%22sin%22%3A{}%2C%22cur_page%22%3A{}%7D%7D%7D'  # 欧美歌手JSON包

    singers_page_url3 = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI16904978519098712&g_tk=5381&loginUin=0&' \
                        'hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&' \
                        'needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A10000%7D%2C%22singerList%' \
                        '22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%' \
                        '22%2C%22param%22%3A%7B%22area%22%3A2%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%' \
                        '3A-100%2C%22sin%22%3A{}%2C%22cur_page%22%3A{}%7D%7D%7D'   # 港台歌手JSON包

    singers_page_url4 = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI3824984122862256&g_tk=5381&loginUin=0&' \
                        'hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&' \
                        'needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A10000%7D%2C%22singerList%' \
                        '22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%' \
                        '22%2C%22param%22%3A%7B%22area%22%3A200%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%' \
                        '3A-100%2C%22sin%22%3A{}%2C%22cur_page%22%3A{}%7D%7D%7D'  # 内地歌JSON包

    singers_page_url5 = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI4727150700811087&g_tk=5381&loginUin=0&' \
                        'hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&' \
                        'needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A10000%7D%2C%22singerList%' \
                        '22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%' \
                        '22%2C%22param%22%3A%7B%22area%22%3A4%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%' \
                        '3A-100%2C%22sin%22%3A{}%2C%22cur_page%22%3A{}%7D%7D%7D'

    singer_home_url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&singermid={}&order=listen&begin={}&num=30&songstatus=1'

    ip_poor = ['119.146.2.234', '219.234.5.128']
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/' \
             '{} Safari/535.24'.format(ip_poor[0])}

    add = 0  # 增量80
    singers_page = 1  # 歌手页
    file_dir = 'C:/Users/summer/Desktop/点歌系统/曲库'
    os.chdir("C:/Users/summer/Desktop/点歌系统/曲库")  # 换路径

    # singer_list = []
    # with open('日本歌手.json', 'w')as f:  # json储存
    #     for i in range(3):  # 获取前三页歌手信息
    #         url = singers_page_url5.format(add, singers_page)  # 歌手页url
    #         singer_list += get_all_singers(url, header)
    #         add += 80
    #         singers_page += 1
    #     print(singer_list)
    #     json.dump(singer_list, f)

    # for root, dirs, files in os.walk(file_dir):
    #     # print(files)  # 当前路径下所有非目录子文件
    #     ref = re.compile(r'song/(.*).html')
    #     ref1 = re.compile(r'\'(.*?)\'')
    #     ref2 = re.compile(r"\[(.*?)], 'https")
    #     for file in files:  # 每个文件
    #         with open(file, 'r') as f:
    #             # print(f.read())
    #             for i in f.readlines():
    #                 song_name = re.findall(ref1, i[1:-2])[0]  # 歌名
    #                 song_singer = re.findall(ref2, i[1:-2])[0].replace("'", '')  # 歌手
    #                 song_mid = re.findall(ref, i)[0]  # mid
    #                 print(song_singer)
    #                 print(song_mid)
    #                 print(song_name)
    #             input()
    area_dict = {'内地': 200, '港台': 2, '欧美': 5, '日本': 4}

    with open('欧美歌手.json', 'r')as f:  # json读取
        for i in json.load(f):
            songs_page = 0  # 歌曲页
            print(i[0], i[1])
            name = str(i[0])
            infos = []
            os.chdir("C:/Users/summer/Desktop/点歌系统/欧美歌曲")  # 换路径
            while True:
                songs_page_url = singer_home_url.format(str(i[1]), songs_page)
                if is_end(songs_page_url, header):  # 一次写入
                    with open(str(name) + '歌曲库.sj', 'ab')as g:  # pickle储存
                        try:
                            pickle.dump(infos, g)
                        except Exception as e:
                            print(e)
                            print('wrong')
                            pass
                    print('end!')
                    break
                area_code = area_dict[f.name[0:2]]
                infos += get_page_songs_info(songs_page_url, str(i[0]), area_code, header)
                songs_page += 30  # 曲增量
