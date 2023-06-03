import base64
import urllib
import requests
import json
import re
import os
import cv2
import datetime
import time
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
API_KEY = "YxUFBE2njyuxfusXFBBE4Gb4"
SECRET_KEY = "jn6OrcPhxmcjNTDr18ZIKIaVfn6GP50k"
global index
index=1
inn=1
def main():
    global index,inn
    imgget()
    if(index!=inn):
        inn=index
        url = "https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=" + get_access_token()
        # image 可以通过 get_file_content_as_base64("C:\fakepath\tupian2.jpg",False) 方法获取
        payload = json.dumps({
            "image": get_file_content_as_base64("/home/pi/Pictures/tupian"+  str(index-1) + ".jpg",False),
            "image_type": "BASE64",
            #"face_field": "age,beauty,expression,face_shape,glasses,mask",
            "face_field": "age,beauty,expression",
            "max_face_num": 2,
            "face_type": "LIVE"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        
        open("/home/pi/Pictures/tupiantext" + str(index-1) + ".txt", 'w').write(response.text) 
        print(response.text)
        nn=duqutxt(index)
        if nn>0:
            main1()
            writetxt()
def timee():
    curr_time = datetime.now()
    timestamp = datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S') 
    return timestamp
def imgget():
    global index
    cap = cv2.VideoCapture(0)
    flag = cap.isOpened()
    while (flag):
        ret, frame = cap.read()
        cv2.imshow("Capture", frame)
        k = cv2.waitKey(1) & 0xFF
        t=0
        t=gett()
        print(t+'/n')
        if  int(t) == 3:  # 按下s键，进入下面的保存图片操作
            cv2.imwrite("/home/pi/Pictures/tupian" + str(index) + ".jpg", frame)
            print("save " + str(index) + ".jpg successfuly!")
            print("-------------------------")
            index += 1
        #elif k == ord('q'):  # 按下q键，程序退出
            break
    cap.release() # 释放摄像头
    cv2.destroyAllWindows()# 释放并销毁窗口
def get_file_content_as_base64(path, urlencoded=False):
    global index
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content

def get_access_token():
    global index
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
def main1():
    global index
    url = "https://aip.baidubce.com/rest/2.0/face/v3/search?access_token=" + get_access_token()
    
    # image 可以通过 get_file_content_as_base64("C:\fakepath\tupian1.jpg",False) 方法获取
    payload = json.dumps({
        "group_id_list": "1,2,3,4,5",
        "image": get_file_content_as_base64("/home/pi/Pictures/tupian"+str(index-1)+".jpg",False),
        "image_type": "BASE64",
        "max_user_num": 1,#此处修改max num
        "match_threshold":70
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    open("/home/pi/Pictures/tupiantextMAIN1" + str(index-1) + ".txt", 'w').write(response.text) 
    print(response.text)
def duqutxt(index):
# for index in range(1,10):
    path = ("/home/pi/Pictures/tupiantext" + str(index-1) + ".txt")
    with open(path, "r", encoding='utf-8') as f:
        content = f.read()
    # 提取“4.4 报告期内基金投资策略和运作分析”和“4.5 报告期内基金的业绩表现”之间的内容
    re_str = r'face_num":(.+),"face_list'
    resp = re.findall(re_str, content, re.S)
    result = ' '.join(resp)
    result.split('\n')  #删除换行符
    nu=int(result)
    return nu
    #print(result)
def readmain(pat,re_str):
    global inde
    path = ("/home/pi/Pictures/"+str(pat) + str(index-1) + ".txt")
    print(path)
    with open(path, "r", encoding='utf-8') as f:
        content = f.read()
    # 提取“4.4 报告期内基金投资策略和运作分析”和“4.5 报告期内基金的业绩表现”之间的内容
    #re_str = r'"user_id":"(.+)","user_info":"","sc'
    #re_str1= r'expression":{"type":"(.+)","probability":1},"face_shape":{"typ'
    resp = re.findall(re_str, content, re.S)
    result = ' '.join(resp)
    return result
def writetxt():
    global index
    stanger=1
    result=readmain("tupiantextMAIN1",r'ser_id":"(.+)","user_info":"","sc')
    result1=readmain("tupiantext",r'ession":{"type":"(.+)","probabili')
    if(str(result)==""):
        stanger=0
        result="stranger"
    message = str(stanger)+" "+str(result)+" "+str(result1)+" " # 读取全部信息
    filename = '/home/pi/log/log.txt'
    with open(filename, 'a') as file_object:
        #for message in messageall:
            print(message)  # 输出一条信息
            file_object.write(str(message)+"\n")
    print("\n ", "=" * 20, "over", "=" * 20, "\n")



import time
import RPi.GPIO as GPIO
class keypad(object):
  KEYPAD=[
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']]
 
  ROW    =[19,12,13,16]#行
  COLUMN =[20,26,25,24]#列
 
#初始化函数
def __init__():
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)
#取得键盘数函数
def getkey():
  GPIO.setmode(GPIO.BCM)
#设置列输出低
  for i in range(len(keypad.COLUMN)):
    GPIO.setup(keypad.COLUMN[i],GPIO.OUT)
    GPIO.output(keypad.COLUMN[i],GPIO.LOW)
#设置行为输入、上拉
  for j in range(len(keypad.ROW)):
    GPIO.setup(keypad.ROW[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
#检测行是否有键按下，有则读取行值
  RowVal=-1
  for i in range(len(keypad.ROW)):
    RowStatus=GPIO.input(keypad.ROW[i])
    if RowStatus==GPIO.LOW:
       RowVal=i
       #print('RowVal=%s' % RowVal)
#若无键按下,则退出，准备下一次扫描
  if RowVal<0 or RowVal>3:
    exit()
    return
 
#若第RowVal行有键按下，跳过退出函数，对掉输入输出模式
#第RowVal行输出高电平，
  GPIO.setup(keypad.ROW[RowVal],GPIO.OUT)
  GPIO.output(keypad.ROW[RowVal],GPIO.HIGH)
#列为下拉输入
  for j in range(len(keypad.COLUMN)):
    GPIO.setup(keypad.COLUMN[j],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
 
#读取按键所在列值
  ColumnVal=-1
  for i in range(len(keypad.COLUMN)):
    ColumnStatus=GPIO.input(keypad.COLUMN[i])
    if ColumnStatus==GPIO.HIGH:
      ColumnVal=i
#等待按键松开
      while GPIO.input(keypad.COLUMN[i])==GPIO.HIGH:
        time.sleep(0.05)
        #print ('ColumnVal=%s' % ColumnVal)
#若无键按下，返回
  if ColumnVal<0 or ColumnVal>3:
    exit()
    return
 
  exit()
  return keypad.KEYPAD[RowVal][ColumnVal]
 
 
def exit():
 
  import RPi.GPIO as GPIO
  for i in range(len(keypad.ROW)):
    GPIO.setup( keypad.ROW[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)
  for j in range(len( keypad.COLUMN)):
    GPIO.setup( keypad.COLUMN[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)


#key=None
def gett(): 
    while True:
        key=getkey()
        if not key==None:
            print ('You enter the  key:',key)
            break
    return key





if __name__ == '__main__':
    main()
    
