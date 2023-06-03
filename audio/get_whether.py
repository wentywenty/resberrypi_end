import os
import subprocess
from aip import AipSpeech
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

""" APPID AK SK """
APP_ID = '33513297'
API_KEY = 'a6AW7ML0c42PUdpBgz8Miv8f'
SECRET_KEY = 's0B52BOTAREp3Gyz9Sgynu36im0G88qa'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 爬取天气
resp = urlopen('http://www.weather.com.cn/weather//101070101.shtml')
soup = BeautifulSoup(resp, 'html.parser')
tagToday = soup.find('p', class_="tem")  # 第一个包含class="tem"的p标签即为存放今天天气数据的标签
try:
    temperatureHigh = tagToday.span.string  # 有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
except AttributeError as e:
    temperatureHigh = tagToday.find_next('p', class_="tem").span.string  # 获取第二天的最高温度代替

temperatureLow = tagToday.i.string  # 获取最低温度
weather = soup.find('p', class_="wea").string  # 获取天气

text = f"主人，今天的天气是{weather}，最低温度{temperatureLow}，最高温度{temperatureHigh}℃"

result = client.synthesis(f'{text}', 'zh', 1, {
    'vol': 8,
    'per': 111,
    'pit': 6,
    'spd': 4,
})

# 识别正确返回语音二进制 错误则返回dict
if not isinstance(result, dict):
    # 保存MP3文件
    # with open(r'C:\Users\86157\OneDrive\桌面\111.mp3', 'wb') as file:
    #     file.write(result)
    # os.system(r'C:\Users\86157\OneDrive\桌面\111.mp3')
    # time.sleep(1)
    # os.remove(r'C:\Users\86157\OneDrive\桌面\111.mp3')
    with open('/home/pi/audio/5118.mp3', 'wb') as file:
        file.write(result)

    # 播放MP3文件
    subprocess.Popen(['vlc', '--play-and-exit', '/home/pi/audio/5118.mp3'])
    subprocess.call(["vlc", "--x11-display=:0", "/home/pi/Videos/speak.mp4", "--play-and-exit"])

    # 等待1秒钟，让文件能够正常播放
    time.sleep(1)

    # 删除MP3文件
    os.remove('/home/pi/audio/5118.mp3')
