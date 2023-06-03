#!/bin/bash

val=$(head -n1 /home/pi/log/log.txt | cut -d' ' -f1)
face=$(head -n1 /home/pi/log/log.txt | cut -d' ' -f3)

echo "val equal $val"
echo "$face"
sleep 1
if [ $val -eq 1 ]; then
    # ����ǣ��򲥷� /home/pi/Videos/master.mp4 ��Ƶ�ļ�
    vlc --x11-display=:0 /home/pi/Videos/master.mp4 --play-and-exit

    # ������� $face ���� "smile"���򲥷� /home/pi/Videos/happy.mp4 ��Ƶ�ļ�
    if [ "$face" = "smile" ]; then
        vlc --x11-display=:0 /home/pi/Videos/happy.mp4 --play-and-exit

    # ������� $face ���� "angry"���򲥷� /home/pi/Videos/angry.mp4 ��Ƶ�ļ�
    elif [ "$face" = "angry" ]; then
        vlc --x11-display=:0 /home/pi/Videos/angry.mp4 --play-and-exit

    # ������� $face ���� "sad"���򲥷� /home/pi/Videos/sad.mp4 ��Ƶ�ļ�
    elif [ "$face" = "sad" ]; then
        vlc --x11-display=:0 /home/pi/Videos/sad.mp4 --play-and-exit
    else
        echo "�������"

    fi

    # �ȴ� 3 ��
    sleep 1

    # ���� /home/pi/Videos/open.mp4 ��Ƶ�ļ�
    vlc --x11-display=:0 /home/pi/Videos/open.mp4 --play-and-exit

    # �ȴ� 5 ��
    sleep 5

    # ���� /home/pi/Videos/close.mp4 ��Ƶ�ļ�
    vlc --x11-display=:0 /home/pi/Videos/close.mp4 --play-and-exit

# ������� $val ���� 0���򲥷� /home/pi/Videos/stranger.mp4 ��Ƶ�ļ�
elif [ $val -eq 0 ]; then
    vlc --x11-display=:0 /home/pi/Videos/stranger.mp4 --play-and-exit
    sleep 1
fi






