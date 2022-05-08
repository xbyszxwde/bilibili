import re
import pandas
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib import font_manager

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '错误'

def save(html):
    soup = BeautifulSoup(html, 'html.parser')
    with open('./data/B_data.txt', 'r+', encoding='UTF-8') as f:
        f.write(soup.text)
    TScore = []
    name = []
    bfl = []
    pls = []
    scs = []
    for tag in soup.find_all('div', class_='info'):
        bf = tag.a.string
        name.append(str(bf))
    print(name)
    for tag in soup.find_all('div', class_='detail'):
        bf = tag.find('span', class_='data-box').get_text()
        if '亿' in bf:
            num = float(re.search(r'\d(.\d)?', bf).group()) * 10000
            bf = num
        else:
            bf = re.search(r'\d*(\.)?\d', bf).group()
        bfl.append(float(bf))
    print(bfl)
    for tag in soup.find_all('div', class_='detail'):
        pl = tag.find('span', class_='data-box').next_sibling.next_sibling.get_text()
        if '万' not in pl:
            pl = '%.1f' % (float(pl) / 10000)
        else:
            pl = re.search(r'\d*(\.)?\d', pl).group()
        pls.append(float(pl))
    print(pls)
    for tag in soup.find_all('div', class_='detail'):
        sc = tag.find('span', class_='data-box').next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        sc = re.search(r'\d*(\.)?\d', sc).group()
        scs.append(float(sc))
    print(scs)
    for tag in soup.find_all('div', class_='pts'):
        zh = tag.find('div').get_text()
        TScore.append(int(zh))
    print('综合评分', TScore)
    info = {'动漫名': name, '播放量(万)': bfl, '评论数(万)': pls, '收藏数(万)': scs, '综合评分': TScore}
    dm_file = pandas.DataFrame(info)
    dm_file.to_excel('Dongman.xlsx', sheet_name="动漫数据分析")
    return name, bfl, pls, scs, TScore


def view(info):
    my_font = font_manager.FontProperties(fname='./data/STHeiti Medium.ttc')  # 设置中文字体
    dm_name = info[0]
    dm_play = info[1]
    dm_review = info[2]
    dm_favorite = info[3]
    dm_com_score = info[4]
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax1 = plt.subplots()
    plt.bar(dm_name, dm_com_score, color='red')
    plt.title('综合评分和播放量数据分析', fontproperties=my_font)
    ax1.tick_params(labelsize=6)
    plt.xlabel('番剧名')
    plt.ylabel('综合评分')
    plt.xticks(rotation=90, color='green')
    ax2 = ax1.twinx()
    ax2.plot(dm_play, color='cyan')
    plt.ylabel('播放量')
    plt.plot(1, label='综合评分', color="red", linewidth=5.0)
    plt.plot(1, label='播放量', color="cyan", linewidth=1.0, linestyle="-")
    plt.legend()
    plt.savefig(r'E:1.png', dpi=1000, bbox_inches='tight')
    fig, ax3 = plt.subplots()
    plt.bar(dm_name, dm_review, color='green')
    plt.title('番剧评论数和收藏数分析')
    plt.ylabel('评论数（万）')
    ax3.tick_params(labelsize=6)
    plt.xticks(rotation=90, color='green')
    ax4 = ax3.twinx()
    ax4.plot(dm_favorite, color='yellow')
    plt.ylabel('收藏数（万）')
    plt.plot(1, label='评论数', color="green", linewidth=5.0)
    plt.plot(1, label='收藏数', color="yellow", linewidth=1.0, linestyle="-")
    plt.legend()
    plt.savefig(r'E:2.png', dpi=1000, bbox_inches='tight')
    fig, ax5 = plt.subplots()
    plt.bar(dm_name, dm_com_score, color='red')
    plt.title('综合评分和收藏数量数据分析')
    plt.ylabel('综合评分')
    ax5.tick_params(labelsize=6)
    plt.xticks(rotation=90, color='green')
    ax6 = ax5.twinx()
    ax6.plot(dm_favorite, color='yellow')
    plt.ylabel('收藏数（万）')
    plt.plot(1, label='综合评分', color="red", linewidth=5.0)
    plt.plot(1, label='收藏数', color="yellow", linewidth=1.0, linestyle="-")
    plt.legend()
    plt.savefig(r'E:3.png', dpi=1000, bbox_inches='tight')
    fig, ax7 = plt.subplots()
    plt.bar(dm_name, dm_play, color='cyan')
    plt.title('播放量和评论数 数据分析')
    plt.ylabel('播放量（万）')
    ax7.tick_params(labelsize=6)
    plt.xticks(rotation=90, color='green')
    ax8 = ax7.twinx()
    ax8.plot(dm_review, color='green')
    plt.ylabel('评论数（万）')
    plt.plot(1, label='播放量', color="cyan", linewidth=5.0)
    plt.plot(1, label='评论数', color="green", linewidth=1.0, linestyle="-")
    plt.legend()
    plt.savefig(r'E:4.png', dpi=1000, bbox_inches='tight')
    plt.show()

def main():
    url = 'https://www.bilibili.com/v/popular/rank/bangumi'
    html = get_html(url)
    info = save(html)
    view(info)

if __name__ == '__main__':
    main()
