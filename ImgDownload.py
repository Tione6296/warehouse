import pprint
import time
import os
import urllib.error
import urllib.request

#day at 20211130

path = os.getcwd()

#url_list = ['https://hsod2-webview.s3.amazonaws.com/images/broadcast_top/equip_icon/{:03}.jpg'.format(i) for i in range(4376)]#601
#url_list = ['https://static-image.benghuai.com/hsod2_webview/images/broadcast_top/equip_icon/png/{:03}.png'.format(i) for i in range(4376)]#3170
#url_list = ['https://static.image.mihoyo.com/hsod2_webview/images/broadcast_top/equip_icon/png/{:03}.png'.format(i) for i in range(4376)]#4376
#url_list = ['https://hsod2-webview.s3.amazonaws.com/images/broadcast_top/equip_image/{:03}I.png'.format(i) for i in range(3170)]#3170
#url_list = ['https://hsod2-webview.s3.amazonaws.com/images/broadcast_top/skin/{}.png'.format(i) for i in range(50)]#36
#url_list = ['https://static.image.mihoyo.com/hsod2_webview/images/broadcast_top/map_icon/picture/properties/{:03}.png'.format(i) for i in range(100)]#61
#url_list = ['https://static.image.mihoyo.com/hsod2_webview/images/broadcast_top/Skill_icon_website/{:03}.png'.format(i) for i in range(100)]#61
#url_list = ['https://static.image.mihoyo.com/hsod2_webview/images/broadcast_top/equip_website/zombie/{}.png'.format(i) for i in range(100)]#92
#url_list = ['https://static.image.mihoyo.com/hsod2_webview/images/broadcast_top/equip_website/bubble/{}.png'.format(i) for i in range(100)]#92
#url_list = ['https://static-image.benghuai.com/hsod2_webview/images/broadcast_top/equip_website/{:03}.png'.format(i) for i in range(4376)]#3739
url_list = ['https://static-image.benghuai.com/hsod2_webview/images/broadcast_top/emblem_list/{:03}.png'.format(i) for i in range (400)]

#url_list = [''.format(i) for i in range(4376)]

sleep_time_sec = .2

def download_file(url, path):
    try:
        with urllib.request.urlopen(url) as web_file, open(path, 'wb') as local_file:
            local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)

def download_file_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))

for url in url_list:
    download_file_dir(url, path)
    time.sleep(sleep_time_sec)


