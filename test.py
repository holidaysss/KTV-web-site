import pickle
import os
import requests
import json

album_info = []
os.chdir("C:/Users/summer/Desktop/点歌系统/歌曲/港台歌曲")  # 换路径
for root, dirs, files in os.walk('C:/Users/summer/Desktop/点歌系统/歌曲/港台歌曲'):
    for i in files:
        with open(i, 'rb')as f:
            output = pickle.load(f)
            for j in output:
                if j[5] and j[1][0] and j[4]:
                    album_info.append((j[1][0], j[4], j[5]))
album_info=list(set(album_info))

os.chdir("C:/Users/summer/Desktop/点歌系统/歌曲/内地歌曲")  # 换路径
for root1, dirs1, files1 in os.walk('C:/Users/summer/Desktop/点歌系统/歌曲/内地歌曲'):
    for i in files1:
        with open(i, 'rb')as f:
            output = pickle.load(f)
            for j in output:
                if j[5] and j[1][0] and j[4]:
                    album_info.append((j[1][0], j[4], j[5]))
album_info=list(set(album_info))

os.chdir("C:/Users/summer/Desktop/点歌系统/歌曲/日本歌曲")  # 换路径
for root2, dirs2, files2 in os.walk('C:/Users/summer/Desktop/点歌系统/歌曲/日本歌曲'):
    for i in files2:
        with open(i, 'rb')as f:
            output = pickle.load(f)
            for j in output:
                if j[5] and j[1][0] and j[4]:
                    album_info.append((j[1][0], j[4], j[5]))
album_info=list(set(album_info))

os.chdir("C:/Users/summer/Desktop/点歌系统/歌曲/欧美歌曲")  # 换路径
for root3, dirs3, files3 in os.walk('C:/Users/summer/Desktop/点歌系统/歌曲/欧美歌曲'):
    for i in files3:
        with open(i, 'rb')as f:
            output = pickle.load(f)
            for j in output:
                if j[5] and j[1][0] and j[4]:
                    album_info.append((j[1][0], j[4], j[5]))
album_info=list(set(album_info))
print(album_info)
print(len(album_info))

# os.chdir("C:/Users/summer/Desktop/点歌系统/")  # 换路径
# with open('专辑信息.sj', 'ab')as f:
#     pickle.dump(album_info, f)
# with open('专辑信息.sj', 'rb')as f:
#     output = pickle.load(f)
#     print(output)


# with open('专辑信息.sj', 'ab')as g:
#     pickle.dump(album_infos, g)

# with open('专辑信息.sj', 'rb')as f:
#     output = pickle.load(f)
#     for i in output:
#         print(i)

# ids = [1,4,3,3,4,2,3,4,5,6,1]
# ids = list(set(ids))
# print(ids)