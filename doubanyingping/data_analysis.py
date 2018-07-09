# -*- coding:utf-8 -*-

import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba.posseg as pseg
import matplotlib.pyplot as plt

# 获取数据
def get_datas(filename):
    try:
        with open(filename, 'r') as fp:
            contents = fp.read()
        return contents
    except:
        return None

# 词性标注
def cixing_analysis(str):
    words = pseg.cut(str)
    for w in words:
        print(w.word, w.flag)

# 数据可视化
def data_view(str):
    words = jieba.cut(str, cut_all=False)
    text = ' '.join(words)
    wc = WordCloud(
        background_color='white',  # 设置背景颜色
        # mask=backgroud_Image,  # 设置背景图片
        font_path='/home/wangf/.local/lib/python3.5/site-packages/matplotlib/mpl-data/fonts/ttf/msyh.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        max_words=2000,  # 设置最大现实的字数
        stopwords=STOPWORDS,  # 设置停用词
        max_font_size=150,  # 设置字体最大值
        random_state=30  # 设置有多少种随机生成状态，即有多少种配色方案
    )
    wc.generate_from_text(text)

    plt.imshow(wc)
    plt.axis('off')
    plt.show()

    wc.to_file('comment.png')

if __name__ == '__main__':
    filename = '/home/wangf/PycharmProjects/scrapy_projects/doubanyingping/comment.csv'
    str = get_datas(filename)
    #cixing_analysis(str)
    data_view(str)