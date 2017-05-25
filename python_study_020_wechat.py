# -*- coding:UTF-8 -*-
import itchat
import re

itchat.login()
friends = itchat.get_friends(update=True)[0:]
tList = []
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)

# 拼接字符串
text = "".join(tList)

# jieba分词
import jieba

wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image

d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d, "wechat.png")))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='msyh.ttc') \
    .generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 保存图片 并发送到手机
my_wordcloud.to_file(os.path.join(d, "wechat_cloud.png"))
itchat.send_image("wechat_cloud.png", 'filehelper')