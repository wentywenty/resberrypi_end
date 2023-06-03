#!/bin/bash

val=$(head -n1 /home/pi/log/log.txt | cut -d' ' -f1)
face=$(head -n1 /home/pi/log/log.txt | cut -d' ' -f3)

echo "val equal $val"
echo "$face"
sleep 1
if [ $val -eq 1 ]; then
    # 如果是，则播放 /home/pi/Videos/master.mp4 视频文件
    vlc --x11-display=:0 /home/pi/Videos/master.mp4 --play-and-exit

    # 如果变量 $face 等于 "smile"，则播放 /home/pi/Videos/happy.mp4 视频文件
    if [ "$face" = "smile" ]; then
        vlc --x11-display=:0 /home/pi/Videos/happy.mp4 --play-and-exit

    # 如果变量 $face 等于 "angry"，则播放 /home/pi/Videos/angry.mp4 视频文件
    elif [ "$face" = "angry" ]; then
        vlc --x11-display=:0 /home/pi/Videos/angry.mp4 --play-and-exit

    # 如果变量 $face 等于 "sad"，则播放 /home/pi/Videos/sad.mp4 视频文件
    elif [ "$face" = "sad" ]; then
        vlc --x11-display=:0 /home/pi/Videos/sad.mp4 --play-and-exit
    else
        echo "输入错误"

    fi

    # 等待 3 秒
    sleep 1

    # 播放 /home/pi/Videos/open.mp4 视频文件
    vlc --x11-display=:0 /home/pi/Videos/open.mp4 --play-and-exit

    # 等待 5 秒
    sleep 5

    # 播放 /home/pi/Videos/close.mp4 视频文件
    vlc --x11-display=:0 /home/pi/Videos/close.mp4 --play-and-exit

# 如果变量 $val 等于 0，则播放 /home/pi/Videos/stranger.mp4 视频文件
elif [ $val -eq 0 ]; then
    vlc --x11-display=:0 /home/pi/Videos/stranger.mp4 --play-and-exit
    sleep 1
fi






