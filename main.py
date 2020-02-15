import requests
import re
import os
import urllib.request
import platform
import subprocess
import getpass
import time


xitong_weishu=0
while True:
    print("欢迎进入哔哩哔哩爬虫")
    print("*"*100)
    print("正在进入系统检测，请稍后........")
    time.sleep(1)
    print('='*100)
    caozuoxitongbanbenxinxi=platform.platform()
    print('您的操作系统及其版本为：{}'.format(caozuoxitongbanbenxinxi))
    xitongmingcheng=platform.system().lower()
    print("您的系统名称为：{}".format(xitongmingcheng))
    xitongweishu=platform.architecture()
    print("您的系统位数为：{}".format(xitongweishu))
    print('='*100)
    xitongweishu_huoqu=list(xitongweishu)[0]
    xitongweishu_diyici=xitongweishu_huoqu.replace('bit','')
    tuichu=0
    print('将进入系统检测，请稍后........')
    print("*"*100)
    time.sleep(1)
    while True:
        if xitongmingcheng=='windows' and int(xitongweishu_diyici)==64:
            print("系统环境检测成功，您的系统为64位，将进入python环境配置......")
            time.sleep(1)
            xitong_weishu=int(xitongweishu_diyici)
            tuichu=1
            print('*'*100)
            break
        elif xitongmingcheng=='windows' and int(xitongweishu_diyici)==32:
            print("系统环境检测成功，您的系统为32位，将进入python环境配置......")
            time.sleep(1)
            xitongweishu=int(xitongweishu_diyici)
            tuichu=1
            print('*' * 100)
            break
        else:
            print("您的系统不支持本脚本运行")
            print("请使用windows系统，32位或者64位")
            print("*"*100)
            break
    if tuichu==1:
        break
    else:
        continue

print("正在进入环境配置中，请稍后........")
print("*"*100)
time.sleep(1)
#视频插件环境变量配置
huanjinglujing=os.path.realpath(r'./subject\build\ffmpeg-20200211-f15007a-win64-static\bin')
os.environ["PATH"] = huanjinglujing + ";" + os.environ["PATH"]
print("视频插件环境变量配置成功，正在执行下一步.........")
print("*"*100)
time.sleep(1)

#python版本检测和you-get检测
def python(zz):
    xx = zz.replace(' ', '')[:-5]
    cc = xx.lower()
    if 'python3' != cc:
        print("python版本不正确，需要安装python3版本")
        print('将自动打开python3安装包，请手动安装')
        print('*' * 100)
        return -2
    else:
        print("将自动检测是否有组件，请稍后......")
        print("*"*100)
        time.sleep(1)
        mokuan = os.popen("pip list").read().lower()
        mokuan1 = mokuan.find("you-get")
        mokuan2 = len("you-get") + mokuan1 + 1
        mokuan3 = ''
        for i in range(mokuan1, mokuan2 - 1):
            mokuan3 += mokuan[i]
        if mokuan1 == -1:
            print('已检测到没有装组件，正在帮你自动安装，请稍等........')
            print('*' * 100)
            time.sleep(1)
            os.system('pip -i https://pypi.tuna.tsinghua.edu.cn/simple you-get')
            print("已成功执行命令，正在执行下一步........")
            print('*' * 100)
            time.sleep(1)
        else:
            print('您已经安装所需组件，正在执行下一步.......')
            print('*' * 100)
            time.sleep(1)

#检测是否安装python
def popen(cmd):
    try:
        subprocess.Popen(cmd, stdout=subprocess.PIPE)
        python_banben = os.popen('python --version').read()
        return python_banben
    except BaseException as e:
        return -1

#python环境检测配置
def python_huanjing_peizhi_jiance():
    diyitiao_python_huanjing_lujing=''
    diertiao_python_huanjing_lujing=''
    wa=os.environ['PATH']
    zh=wa.split(';')
    z=getpass.getuser()
    try:
        huanjing_python=r'C:\Users\{}\AppData\Local\Programs'.format(z)
        huanjing_list_python=os.listdir(huanjing_python)
        a_python=r'C:\Users\{}\AppData\Local\Programs\Python'.format(z)
        list_a_python=os.listdir(a_python)
    except:
        print("您的python安装路径找不到")
        return '请正确的配置的python路径'
    for n_python in list_a_python:
        if n_python[:6]=='Python':
            pass
        else:
            print("您的python安装路径找不到")
            return '请正确的配置的python路径'
        print("进入python环境检测，请稍后........")
        print("*"*100)
        time.sleep(1)
        for zh_python in zh:
            if zh_python==a_python+'\\'+n_python:
                if zh_python==a_python+'\\'+n_python+'\\'+'Scripts':
                    print('您已经搭配好python环境，正在进行下一步......')
                    print("*"*100)
                    time.sleep(1)
                    break
                else:
                    continue
    for j_python in huanjing_list_python:
        if 'Python'==j_python:
            huanjing_python=huanjing_python+'\\'+j_python
            list_j_python=os.listdir(huanjing_python)
            for i_python in list_j_python:
                if i_python[:6]=='Python':
                    diyitiao_python_huanjing_lujing=huanjing_python+'\\'+i_python
                    diertiao_python_huanjing_lujing=diyitiao_python_huanjing_lujing+'\\Scripts'
    diyitiao_huanjing_peizhi = os.path.realpath(diyitiao_python_huanjing_lujing)
    diertiao_huanjing_peizhi=os.path.realpath(diertiao_python_huanjing_lujing)
    os.environ["PATH"] = diertiao_huanjing_peizhi + ";" + os.environ["PATH"]
    os.environ["PATH"] = diyitiao_huanjing_peizhi + ";" + os.environ["PATH"]
    print('pythonh环境已配置成功，正在执行下一步......')
    print('*'*100)
    time.sleep(1)

#python环境变量配置
if xitong_weishu==64:
    jiance_python=popen('pip list')
    if jiance_python==-1:
        print("您的电脑没有安装python")
        print("将自动打开python安装软件，请安装完毕后继续执行")
        print("*"*100)
        time.sleep(1)
        os.system(r'./哔哩哔哩爬虫\python配置文件\python-3.7.4-amd64.exe')
        while True:
            while True:
                tuichu_anzhuang=int(input("是否确认已经安装请输入数字（1）为是或（0）或不是："))
                print("*"*100)
                if tuichu_anzhuang==1:
                    jiance1_python = popen('pip list')
                    if jiance1_python == -1:
                        print("您的电脑没有安装python")
                        jinru_python = int(input('是否再次进入自动安装python软件，请输入数字（1）为是或（0）为不是：'))
                        print("*" * 100)
                        if jinru_python == 1:
                            os.system(r'./哔哩哔哩爬虫\python配置文件\python-3.7.4-amd64.exe')
                            continue
                        else:
                            print("请手动检查python是否安装")
                            print('要求的版本为python3')
                            print('*' * 100)
                            continue
                    else:
                        print("您已经安装python，正在进行下一步.......")
                        print('*'*100)
                        time.sleep(1)
                        break
                else:
                    print("请手动检查python是否安装")
                    print('要求的版本为python3')
                    print("*"*100)
                    continue
            zz=os.popen('pip list').read()
            zz_python=python(zz)
            if zz_python==-2:
                continue
            else:
                break
    else:
        print("您的电脑已安装python，python版本为：{}".format(jiance_python))
        print("*" * 100)
        time.sleep(1)
        zz1=popen('pip list')
        zz1_python=python(zz1)
        if zz1_python==-2:
            while True:
                while True:
                    tuichu_anzhuang = int(input("是否确认已经安装请输入数字（1）为是或（0）或不是："))
                    print("*" * 100)
                    if tuichu_anzhuang == 1:
                        jiance1_python = popen('pip list')
                        if jiance1_python == -1:
                            print("您的电脑没有安装python")
                            jinru_python = int(input('是否再次进入自动安装python软件，请输入数字（1）为是或（0）为不是：'))
                            print("*" * 100)
                            if jinru_python == 1:
                                os.system(r'./哔哩哔哩爬虫\python配置文件\python-3.7.4-amd64.exe')
                                continue
                            else:
                                print("请手动检查python是否安装")
                                print('要求的版本为python3')
                                print("*"*100)
                                continue
                        else:
                            print("您已经安装python，正在进行下一步.......")
                            print('*' * 100)
                            time.sleep(1)
                            break
                    else:
                        print("请手动检查python是否安装")
                        print('要求的版本为python3')
                        print("*" * 100)
                        continue
                zz = os.popen('pip list').read()
                zz_python = python(zz)
                if zz_python == -2:
                    continue
                else:
                    break
        else:
            print('正在进行python环境检测，请稍后......')
            print("*"*100)
            time.sleep(1)
            python_huanjing_peizhi_jiance()


elif xitong_weishu==32:
    jiance_python = popen('pip list')
    if jiance_python == -1:
        print("您的电脑没有安装python")
        print("将自动打开python安装软件，请安装完毕后继续执行")
        print("*" * 100)
        time.sleep(1)
        os.system(r'./哔哩哔哩爬虫\python配置文件\python-3.7.4.exe')
        while True:
            while True:
                tuichu_anzhuang = int(input("是否确认已经安装请输入数字（1）为是或（0）或不是："))
                print("*" * 100)
                if tuichu_anzhuang == 1:
                    jiance1_python = popen('pip list')
                    if jiance1_python == -1:
                        print("您的电脑没有安装python")
                        jinru_python = int(input('是否再次进入自动安装python软件，请输入数字（1）为是或（0）为不是：'))
                        print("*" * 100)
                        if jinru_python == 1:
                            os.system(r'./哔哩哔哩爬虫\python配置文件\python-3.7.4.exe')
                            continue
                        else:
                            print("请手动检查python是否安装")
                            print('要求的版本为python3')
                            print("*"*100)
                            continue
                    else:
                        print("您已经安装python，正在进行下一步.......")
                        print('*' * 100)
                        time.sleep(1)
                        break
                else:
                    print("请手动检查python是否安装")
                    print('要求的版本为python3')
                    print("*" * 100)
                    continue
            zz = os.popen('pip list').read()
            zz_python = python(zz)
            if zz_python == -2:
                continue
            else:
                break
    else:
        print("您的电脑已安装python，python版本为：{}".format(jiance_python))
        print("*" * 100)
        time.sleep(1)
        zz1 = os.popen('pip list')
        zz1_python = python(zz1)
        if zz1_python == -2:
            while True:
                while True:
                    tuichu_anzhuang = int(input("是否确认已经安装请输入数字（1）为是或（0）或不是："))
                    print("*" * 100)
                    if tuichu_anzhuang == 1:
                        jiance1_python = popen('pip list')
                        if jiance1_python == -1:
                            print("您的电脑没有安装python")
                            jinru_python = int(input('是否再次进入自动安装python软件，请输入数字（1）为是或（0）为不是：'))
                            print("*" * 100)
                            if jinru_python == 1:
                                os.system(r'./哔哩哔哩爬虫\python配置文件\python-3.7.4-amd64.exe')
                                continue
                            else:
                                print("请手动检查python是否安装")
                                print('要求的版本为python3')
                                print("*"*100)
                                continue
                        else:
                            print("您已经安装python，正在进行下一步.......")
                            print('*' * 100)
                            time.sleep(1)
                            break
                    else:
                        print("请手动检查python是否安装")
                        print('要求的版本为python3')
                        print("*" * 100)
                        continue
                zz = os.popen('pip list').read()
                zz_python = python(zz)
                if zz_python == -2:
                    continue
                else:
                    break
        else:
            print('正在进行python环境检测，请稍后......')
            print("*" * 100)
            time.sleep(1)
            python_huanjing_peizhi_jiance()

print("环境配置成功，正在执行下一步......")
print("*"*100)
time.sleep(1)

#会员
print("需要下载火狐浏览器，然后登入会员，并且配置会员信息路径")
print('不会的请查看配置会员信息的PDF')
print("没有会员将不能下载带有会员的视频")
print("*"*100)
huiyuantxt=''
huiyuanjiance=0
while True:
    try:
        print("正在进入会员自动检测，请稍后......")
        print("*"*100)
        time.sleep(1)
        zztxt = open('会员信息路径.txt', 'r').read()
        huiyuantxt=os.path.realpath(zztxt)
        if 'default-release\cookies.sqlite' in zztxt:
            print("自动检测成功，正在进行下一步......")
            huiyuanjiance=1
            print("*"*100)
            time.sleep(1)
            break
        else:
            print("自动检测txt文件中路径不对或没有，将进入手动操作模式")
            print("*"*100)
            print("按任意键为不是会员，直接进入普通下载模式")
            print("*" * 100)
            huiyuan=int(input("是否有会员服务（1）为是和（0）为不是："))
            if huiyuan==1:
                huiyuanjiance=huiyuan
                zztxt=open('会员信息路径.txt','r').read()
                huiyuantxt=os.path.realpath(zztxt)
                if 'default-release\cookies.sqlite' in zztxt:
                    print("路径检测成功，正在进行下一步.......")
                    print("*"*100)
                    time.sleep(1)
                    break
                else:
                    print('路径错误，请重新检查路径')
                    print('默认为没有会员，跳过此步骤')
                    print('可以关闭程序检查好路径重新运行程序')
                    print("*"*100)
                    break
            else:
                break
    except:
        break

print("正在进入文件夹名字筛选，请稍后.......")
print("*"*100)
time.sleep(1)
#网址的输入
# url='https://www.bilibili.com/video/av88158068'
url=input("请输入哔哩哔哩网址：")

if '/av' in url:
    #文件夹名字筛选
    wenjianjiamingzi=requests.get(url).content.decode('utf-8')
    zh_wenjianjiamingzi=re.findall('"true">.*?_哔哩哔哩',wenjianjiamingzi)
    wh_wenjianjiamingzi=''.join(zh_wenjianjiamingzi)
    diyicishaichu=wh_wenjianjiamingzi.replace(' ','')
    diercishaichu=diyicishaichu.replace('_哔哩哔哩','')
    zhenshi_wenjianjiamingzi=diercishaichu.replace('"true">','')
    print("文件夹删选成功，正在进行下一步.......")
    print("*"*100)
    time.sleep(1)

    #json网址和初步目标视频地址
    print("正在进入网址筛选，请稍后.......")
    print("*"*100)
    time.sleep(1)
    shanxuan1=re.findall('av\d*',url)
    shanxuan2=' '.join(shanxuan1)[2:]
    wangzhi1='https://www.bilibili.com/video/av{}?p='.format(shanxuan2)
    json='https://api.bilibili.com/x/player/pagelist?aid={}&jsonp=jsonp'.format(shanxuan2)
    print("初步筛选已成功，正在执行下一步......")
    print("*"*100)
    time.sleep(1)

    #json数据筛选
    wangzhijson=urllib.request.urlopen(json).read().decode("utf-8")
    shanxuanjson=re.findall('"page":\d*',str(wangzhijson))
    mingzi=re.findall('"part":".*?"',str(wangzhijson))

    #数字和名字的筛选
    liebiaoshuzi=[]
    zhenshishuzi=[]
    jishu=0
    for i in shanxuanjson:
        jsonshuju=i.replace('"','')
        jsonshuju1=jsonshuju.replace('page:','')
        zhenshishuzi.append(jsonshuju1)
        liebiaoshuzi.append(jishu)
        jishu+=1
    print("已完成视频数目的筛选，正在执行下一步.......")
    print("*"*100)
    time.sleep(1)

    liebiaomingzi=[]
    for mingzijosn in mingzi:
        yi=mingzijosn.replace('"','')
        er=yi.replace('part:','')
        liebiaomingzi.append(er)
    print("已完成视频名字的删选，正在进行下一步.......")
    print("*"*100)
    time.sleep(1)

    #视频数量和名字的合成
    zidian={}
    for zidiancunchu in liebiaoshuzi:
        zidian[liebiaomingzi[zidiancunchu]]=int(zhenshishuzi[zidiancunchu])
    print("已完成所有的筛选，正在进行下一步.......")
    print("*"*100)
    time.sleep(1)

    if huiyuanjiance==0:
        print("您现在处于非会员模式中，正在执行下一步......")
        print("*"*100)
        time.sleep(1)
        jishu=0
        for iii,ii in zidian.items():
            while True:
                if os.path.exists(zhenshi_wenjianjiamingzi):
                    baocunlujing=os.path.realpath("./{}".format(zhenshi_wenjianjiamingzi))
                    print("已传输完成命令，正在进行下一步......")
                    os.system('you-get -o {} {}{}'.format(baocunlujing,wangzhi1,ii))
                    print("第{}个视频--{}--已下载成功".format(ii,iii))
                    print("*"*100)
                    time.sleep(1)
                    while True:
                        wenjianliebiao=os.listdir('./{}'.format(zhenshi_wenjianjiamingzi))
                        tuichu=''
                        for wenjianlie in wenjianliebiao:
                            if wenjianlie.endswith('.xml'):
                                os.remove('./{}\\{}'.format(zhenshi_wenjianjiamingzi,wenjianlie))
                                print("已删除无用的文件，正在进行下一步.....")
                                print("*" * 100)
                                time.sleep(1)
                                tuichu=wenjianlie
                            if tuichu=='':
                                continue
                            if len(zhenshishuzi)>3:
                                if wenjianlie.endswith('mp4'):
                                    os.rename('./{}\\{}'.format(zhenshi_wenjianjiamingzi,wenjianlie),'./{}\\{}.mp4'.format(zhenshi_wenjianjiamingzi,iii))
                                    print("已成功修改文件名称，文件名字为{}.mp4".format(zidian[ii]))
                                    print("正在进行下一步.......")
                                    print("*"*100)
                                    time.sleep(1)
                                    break
                                elif wenjianlie.endswith('.flv'):
                                    os.rename('./{}\\{}'.format(zhenshi_wenjianjiamingzi,wenjianlie), './{}\\{}.flv'.format(zhenshi_wenjianjiamingzi,iii))
                                    print("已成功修改文件名称，文件名字为{}.flv".format(zidian[ii]))
                                    print("正在进行下一步.......")
                                    print("*" * 100)
                                    time.sleep(1)
                                    break
                            else:
                                break
                        if tuichu!='':
                            break
                    break
                else:
                    os.makedirs(zhenshi_wenjianjiamingzi)
                    # txt文件介绍
                    txt_wenjian = open('./{}\\下载后必看.txt'.format(zhenshi_wenjianjiamingzi), 'w')
                    txt_wenjian.write('**********************************************\n')
                    txt_wenjian.write('   本脚本使用方法为把网址输入进入就可以直接下载\n')
                    txt_wenjian.write('----------->如打开有不出画面问题<-----------\n')
                    txt_wenjian.write('         请使用腾讯视频观看，谢谢配合\n')
                    txt_wenjian.write('**********************************************')
                    txt_wenjian.close()
                    print("程序介绍文件成功生成，正在执行下一步......")
                    print("*" * 100)
                    time.sleep(1)
    else:
        print("您现在处于会员模式中，正在执行下一步.......")
        print("*"*100)
        time.sleep(1)
        jishu = 0
        for iii, ii in zidian.items():
            while True:
                if os.path.exists(zhenshi_wenjianjiamingzi):
                    baocunlujing = os.path.realpath("./{}".format(zhenshi_wenjianjiamingzi))
                    print("已传输完成命令，正在进行下一步......")
                    os.system('you-get -c {} -o {} {}{}'.format(huiyuantxt,baocunlujing,wangzhi1, ii))
                    print("第{}个视频--{}--已下载成功".format(ii, iii))
                    print("*" * 100)
                    time.sleep(1)
                    while True:
                        wenjianliebiao = os.listdir('./{}'.format(zhenshi_wenjianjiamingzi))
                        tuichu = ''
                        for wenjianlie in wenjianliebiao:
                            if wenjianlie.endswith('.xml'):
                                os.remove('./{}\\{}'.format(zhenshi_wenjianjiamingzi, wenjianlie))
                                print("已删除无用的文件，正在进行下一步.....")
                                print("*" * 100)
                                time.sleep(1)
                                tuichu = wenjianlie
                            if tuichu == '':
                                continue
                            if len(zhenshishuzi) > 3:
                                if wenjianlie.endswith('mp4'):
                                    os.rename('./{}\\{}'.format(zhenshi_wenjianjiamingzi, wenjianlie),
                                              './{}\\{}.mp4'.format(zhenshi_wenjianjiamingzi, iii))
                                    print("已成功修改文件名称，文件名字为{}.mp4".format(zidian[ii]))
                                    print("正在进行下一步.......")
                                    print("*" * 100)
                                    time.sleep(1)
                                    break
                                elif wenjianlie.endswith('.flv'):
                                    os.rename('./{}\\{}'.format(zhenshi_wenjianjiamingzi, wenjianlie),
                                              './{}\\{}.flv'.format(zhenshi_wenjianjiamingzi, iii))
                                    print("已成功修改文件名称，文件名字为{}.flv".format(zidian[ii]))
                                    print("正在进行下一步.......")
                                    print("*" * 100)
                                    time.sleep(1)
                                    break
                            else:
                                break
                        if tuichu != '':
                            break
                    break
                else:
                    os.makedirs(zhenshi_wenjianjiamingzi)
                    # txt文件介绍
                    txt_wenjian = open('./{}\\下载后必看.txt'.format(zhenshi_wenjianjiamingzi), 'w')
                    txt_wenjian.write('**********************************************\n')
                    txt_wenjian.write('   本脚本使用方法为把网址输入进入就可以直接下载\n')
                    txt_wenjian.write('----------->如打开有不出画面问题<-----------\n')
                    txt_wenjian.write('         请使用腾讯视频观看，谢谢配合\n')
                    txt_wenjian.write('**********************************************')
                    txt_wenjian.close()
                    print("程序介绍文件成功生成，正在执行下一步......")
                    print("*" * 100)
                    time.sleep(1)

elif 'play/' in url:
    #文件名字筛选
    wenjianmingzi=requests.get(url).content.decode('utf-8')
    mingzishanxuan=re.findall('title>.*?_番剧_bilibili_哔哩哔哩',wenjianmingzi)
    huiyuan_bianweizifuchan = ''.join(mingzishanxuan)
    huiyuan_diyici = huiyuan_bianweizifuchan.replace('title>', '')
    huiyuan_disanci = huiyuan_diyici.replace(r'\xa0', '')
    huiyuan_disici = huiyuan_disanci.replace('_番剧_bilibili_哔哩哔哩', '')
    huiyuan_diwuci = huiyuan_disici.replace(' ', '')

    if huiyuanjiance==1:
        print("您现在处于会员模式中，正在执行下一步.......")
        print("*" * 100)
        time.sleep(1)
        while True:
            if os.path.exists(huiyuan_diwuci):
                huiyuan_lujing=os.path.realpath('./{}'.format(huiyuan_diwuci))
                print("如果是多个视频文件，下载好的，.xml格式文件请不要管，全部下载完后，程序自动帮你清理")
                print("*"*100)
                print("已传达指令，请稍等视频下载完成.......")
                print("*"*100)

                os.system('you-get --playlist -c {} -o {} {}'.format(huiyuantxt,huiyuan_lujing,url))
                print("*"*100)
                print('*'*100)
                time.sleep(1)
                jishu=1
                while True:
                    huijian_liebiao=os.listdir('./{}'.format(huiyuan_diwuci))
                    for huiyua_wenjianbanduan in huijian_liebiao:
                        if huiyua_wenjianbanduan.endswith('.xml'):
                            os.remove('./{}\\{}'.format(huiyuan_diwuci,huiyua_wenjianbanduan))
                            print("已删除第{}个----{}----文件".format(jishu,huiyua_wenjianbanduan))
                            jishu+=1
                            print('*'*100)
                        else:
                            continue
                    break
                break
            else:
                os.makedirs(huiyuan_diwuci)
                txt_wenjian = open('./{}\\下载后必看.txt'.format(huiyuan_diwuci), 'w')
                txt_wenjian.write('**********************************************\n')
                txt_wenjian.write('   本脚本使用方法为把网址输入进入就可以直接下载\n')
                txt_wenjian.write('----------->如打开有不出画面问题<-----------\n')
                txt_wenjian.write('         请使用腾讯视频观看，谢谢配合\n')
                txt_wenjian.write('**********************************************')
                txt_wenjian.close()
                print("程序介绍文件成功生成，正在执行下一步......")
                print("*" * 100)
                time.sleep(1)
    else:
        print("您现在处于非会员模式中，正在执行下一步.......")
        print("*" * 100)
        time.sleep(1)
        while True:
            if os.path.exists(huiyuan_diwuci):
                huiyuan_lujing=os.path.realpath('./{}'.format(huiyuan_diwuci))
                print("如果是多个视频文件，下载好的，.xml格式文件请不要管，全部下载完后，程序自动帮你清理")
                print("*"*100)
                print("已传达指令，请稍等视频下载完成.......")
                print("*"*100)

                os.system('you-get --playlist -o {} {}'.format(huiyuan_lujing,url))
                print("*" * 100)
                print('*' * 100)
                time.sleep(1)
                jishu = 1
                while True:
                    huijian_liebiao = os.listdir('./{}'.format(huiyuan_diwuci))
                    for huiyua_wenjianbanduan in huijian_liebiao:
                        if huiyua_wenjianbanduan.endswith('.xml'):
                            os.remove('./{}\\{}'.format(huiyuan_diwuci, huiyua_wenjianbanduan))
                            print("已删除第{}个----{}----文件".format(jishu, huiyua_wenjianbanduan))
                            jishu += 1
                            print('*' * 100)
                        else:
                            continue
                    break
                break
            else:
                os.makedirs(huiyuan_diwuci)
                txt_wenjian = open('./{}\\下载后必看.txt'.format(huiyuan_diwuci), 'w')
                txt_wenjian.write('**********************************************\n')
                txt_wenjian.write('   本脚本使用方法为把网址输入进入就可以直接下载\n')
                txt_wenjian.write('----------->如打开有不出画面问题<-----------\n')
                txt_wenjian.write('         请使用腾讯视频观看，谢谢配合\n')
                txt_wenjian.write('**********************************************')
                txt_wenjian.close()
                print("程序介绍文件成功生成，正在执行下一步......")
                print("*" * 100)
                time.sleep(1)

print("已全部下载完成")
input("按任意键退出")
