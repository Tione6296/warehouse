import pprint
import time
import os
import urllib.error
import urllib.request

# range 4376 , url_list[100:4376]
path = os.getcwd()

url_list = ['https://static.image.mihoyo.com/hsod2_webview/images/broadcast_top/equip_icon/png/{:03}.png'.format(i) for i in range(4376)]
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


