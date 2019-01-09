from flask import Flask, render_template, request, flash, redirect, url_for
from dbInit import db
import config
import json, os
import re
import pickle
from table import Singer, Song, Top, Album


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # os.chdir("C:/Users/summer/Desktop/点歌系统/欧美歌曲")  # 换路径
        # for root, dirs, files in os.walk('C:/Users/summer/Desktop/点歌系统/欧美歌曲'):
        #     # print(files)  # 当前路径下所有非目录子文件
        #     for i in files:  # 将目录下每一个文件写进数据库
        #         output = pickle.load(open(str(i), 'rb'))
        #         print(i)
        #         for j in range(len(output)):
        #             # print(output[j][0], output[j][1][0], output[j][2][28:42], output[j][4])
        #             song = Song(name=output[j][0], singer=output[j][1][0],
        #                         songmid=output[j][2][28:42], albummid=output[j][4])
        #             db.session.add(song)
        #         db.session.commit()
        # input()

        # os.chdir("C:/Users/summer/Desktop/点歌系统/曲库")  # 换路径
        # for root, dirs, files in os.walk('C:/Users/summer/Desktop/点歌系统/曲库'):
        #     print(files)  # 当前路径下所有非目录子文件
        #     for i in files:  # 将目录下每一个文件写进数据库
        #         print(i)
        #         output = json.load(open(str(i), 'r'))
        #         for j in range(len(output)):
        #             print(output[j][0], output[j][1])
        #             singer = Singer(name=output[j][0], singermid=output[j][1])
        #             db.session.add(singer)
        #         print('insert!!!')
        #         db.session.commit()

        # os.chdir("C:/Users/summer/Desktop/点歌系统/排行榜")  # 换路径
        # with open('港台排行榜.sj', 'rb') as f:
        #     ct = pickle.load(f)
        #     for i in ct:
        #         top = Top(area=2, songname=i[0], singername=i[2], songmid=i[1])
        #         db.session.add(top)
        #         print(i)
        #     db.session.commit()
        # os.chdir("C:/Users/summer/Desktop/点歌系统")
        # with open('专辑信息.sj', 'rb')as f:
        #     output = pickle.load(f)
        #     for n, i in enumerate(output):
        #         print(i)
        #         if i[2]:
        #             album = Album(name=i[2], albummid=i[1], singer=i[0])
        #             db.session.add(album)
        #     db.session.commit()
        # print('!!!!!!!!!!!!!!!!!!!!!!!!!')
        return render_template('home.html')
    else:
        search = request.form.get('search')  # 写啥
        print(search)
        return redirect(url_for('search', search=search, page=1))


@app.route('/search/<search>/<int:page>')
def search(search, page=1):
    print(search)
    singer = Singer.query.filter(Singer.name.contains(search)).first()
    if singer:
        if singer.area == 5:
            print('!!!!')
            songs1 = Song.query.filter(Song.singer.contains(singer.name[:singer.name.index('(')-1]))  # 欧美歌手名字去翻译
            songs = songs1.paginate(page, 40, False)
            print(songs.items)
            return render_template('search.html', search=search, songs=songs)
        print('!!!!')
        songs1 = Song.query.filter(Song.singer.contains(singer.name))
        songs = songs1.paginate(page, 40, False)
        s_a_lsit = []
        for i in songs.items:
            s_a_lsit.append(i.albummid)
        album1 = Album.query.filter(Album.albummid.in_(s_a_lsit))
        albums = album1.paginate(page, 40, False)
        num = len(songs.items)
        print(albums.items)
        # print(songs.items)
        return render_template('search.html', search=search, songs=songs, albums=albums, num=num)
    else:
        print('song')
        songs = Song.query.filter(Song.name.contains(search))
        song = songs.paginate(page, 20, False)
        print(song)
        return render_template('search.html', search=search, songs=song)


@app.route('/hot/<int:page>', methods=['POST', 'GET'])
def hot(page=1):

    tops = Top.query.filter(Top.id > 0)
    top = tops.paginate(page, 15, False)
    print(top)
    return render_template('hot.html', tops=top)


@app.route('/english/<int:page>', methods=['GET'])
def english(page=1):
    singers = Singer.query.filter(Singer.area == 5)
    singer = singers.paginate(page, 15, False)
    print(singer)
    return render_template('english.html', singers=singer)


@app.route('/china/<int:page>', methods=['GET'])
def china(page=1):
    singers = Singer.query.filter(Singer.area == 200 or Singer.area == 2)
    singer = singers.paginate(page, 15, False)
    print(singer)
    return render_template('china.html', singers=singer)


@app.route('/japan/<int:page>', methods=['GET'])
def japan(page=1):
    singers = Singer.query.filter(Singer.area == 4)
    singer = singers.paginate(page, 15, False)
    print(singer)
    return render_template('japan.html', singers=singer)


if __name__ == '__main__':

    app.run(debug=True)