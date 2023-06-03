#!/bin/bash

while true; do
  echo "你好，主人，欢迎回家！"
  echo "1.主人，想获取今天的天气吗？"
  echo "2.主人，你今天心情如何？"
  echo "3.主人，想和我互动吗？"
  echo "4.退出系统"
  read -s num

  if [ $num -eq 1 ]
  then
    echo -ne "\033[2K\r" #清除当前行的内容
    echo "主人，梦梦奈正在努力获取天气，请稍后~"
    # 播放视频素材
    vlc --x11-display=:0 /home/pi/Videos/whether.mp4 --play-and-exit
    # 打开文件get_whether
    python /home/pi/audio/get_whether.py
    #vlc --x11-display=:0 /home/pi/Videos/speak.mp4 --play-and-exit
    sleep 1 # 等待一秒钟，以便用户看到操作信息
    tput reset # 清除整个终端屏幕
  elif [ $num -eq 2 ]
  then
    echo -ne "\033[2K\r" # 清除当前行的内容
    echo "1.我很生气"
    echo "2.我很开心"
    echo "3.我很伤心"
    read -s subnum

    if [ $subnum -eq 1 ]
    then
      echo -ne "\033[2K\r" # 清除当前行的内容
      # 播放视频生气.mp4
      vlc --x11-display=:0 /home/pi/Videos/angery.mp4 --play-and-exit
      sleep 1 # 等待一秒钟，以便用户看到操作信息
      tput reset # 清除整个终端屏幕
    elif [ $subnum -eq 2 ]
    then
      echo -ne "\033[2K\r" # 清除当前行的内容
      # 播放视频开心.mp4
      vlc --x11-display=:0 /home/pi/Videos/happy.mp4 --play-and-exit
      sleep 1 # 等待一秒钟，以便用户看到操作信息
      tput reset # 清除整个终端屏幕
    elif [ $subnum -eq 3 ]
    then
      echo -ne "\033[2K\r" # 清除当前行的内容
      # 播放视频伤心.mp4
      vlc --x11-display=:0 /home/pi/Videos/sad.mp4 --play-and-exit
      sleep 1 # 等待一秒钟，以便用户看到操作信息
      tput reset # 清除整个终端屏幕
    else
      echo "输入错误，请输入数字1，2或3"
      continue
    fi

  elif [ $num -eq 3 ]
  then
    echo -ne "\033[2K\r" #清除当前行的内容
       echo "1.跳个舞"
       echo "2.摸摸头"
       read -s subnum2

    if [ $subnum2 -eq 1 ]
    then
      vlc --x11-display=:0 /home/pi/Videos/dance.mp4 --play-and-exit
    elif [ $subnum2 -eq 2 ]
    then
      echo -ne "\033[2K\r" # 清除当前行的内容
      vlc --x11-display=:0 /home/pi/Videos/patting.mp4 --play-and-exit
      sleep 1 # 等待一秒钟，以便用户看到操作信息
      tput reset # 清除整个终端屏幕
    else
      echo "输入错误，请输入数字1或2"
          continue
      fi

  elif [ $num -eq 4 ]
  then
    echo "主人，再见。希望您过得开心~"
    # 播放视频素材
    vlc --x11-display=:0 /home/pi/Videos/exist.mp4 --play-and-exit 
    sleep 5 # 等待五秒钟，以便用户看到操作信息
    break # 退出 while 循环
  else
    echo "输入错误，请输入数字1，2，3或4"
    continue
  fi
done