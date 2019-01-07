import pickle
import os

os.chdir("C:/Users/summer/Desktop/点歌系统/日本歌曲")  # 换路径
with open('周杰伦歌曲库.sj', 'rb')as f:
    output = pickle.load(f)
    for i in output:
        print(i[0])
    print(len(output))
a = 'asd'.index('s')
print(a)