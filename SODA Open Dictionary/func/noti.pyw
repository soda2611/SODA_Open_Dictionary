from time import sleep
from SOpenDict import SOD_word_list
from notifypy import Notify
import random
import os

with open("func/setting/setting.txt", "r", encoding="utf-8") as fi:
    setting=fi.readlines()
    settings={}
    for index in setting:
        option, properties=index.strip().split(": ")
        settings[option]=properties

with open('func/pid.txt', 'w', encoding="utf-8") as f:
    f.write(str(os.getpid()))

while True:
    sleep(float(settings["waiting time"])*360)
    word=random.choice(SOD_word_list())
    notification = Notify(default_notification_application_name="SODA Open Dictionary", default_notification_icon='func/Logo.ico', default_notification_audio="func/setting/sound_effect/noti.wav")
    notification.title = f'{word["word"]} ({word["type"]})'
    notification.message = f'{word["definition"]}'
    notification.send()