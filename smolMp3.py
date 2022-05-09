from pygame import mixer
from mutagen.mp3 import MP3
from os import walk
import pyinputplus as userin
import random
import threading
import time

mixlist = []
for (path, dirname, titles) in walk("//home//gmo//Music//"):
    mixlist = titles
stop = False
vol = 0.05
mixer.init()
currentSong = ""
threadPause= False

def playCorretly(myfre,music):
    mixer.quit() # you need to quite the mixer so the frequency can be properly set
    mixer.init(frequency=myfre) #you need to set the frequence so that music playes correctly
    mixer.music.set_volume(vol)
    mixer.music.load("//home//gmo//Music//"+music)
    mixer.music.play()
    
def get_RandomSong():
    index = 0
    
    if( not currentSong == ""):
        index = mixlist.index(currentSong)+1
        
    if index == len(mixlist):
        random.shuffle(mixlist)
        index = 0
    music = mixlist[index]
    mp3 = MP3("//home//gmo//Music//"+music)
    rate = mp3.info.sample_rate
    return rate,music


def playerRuning():
    global mixlist
    global vol
    global stop
    global currentSong
    global threadPause
    global index
    while(not stop):
        if(not threadPause):
            if(not mixer.music.get_busy()):
                (rate,music) = get_RandomSong()
                currentSong = music
                playCorretly(rate,music)
        


(rate,music) = get_RandomSong()
playCorretly(rate,music)
currentSong = music
# threads are nessary so that the track can change without haveing to wait for user input
thread1 = threading.Thread(target=playerRuning)
thread1.start()
# without the treads we can't have two loops runing at the same time


while not stop:
    print("\n currently playing "+currentSong)
    answer = input('\n p = pause, up = unpause, m = more instuciton\n ')
    if answer == 'p':
        mixer.music.pause()
    elif answer == 'up':
        mixer.music.unpause()
    elif answer == 's':
        stop = True
        mixer.music.stop()
    elif answer == '+':
        vol += 0.01
        mixer.music.set_volume(vol)
    elif answer == '-':
        if vol- 0.01 > 0:
            vol -= 0.01
            mixer.music.set_volume(vol)
    elif answer == 'r':
        threadPause = True  #pause proccess in thread
        time.sleep(0.1)
        (rate,music) = get_RandomSong()
        currentSong = music
        playCorretly(rate,music)
        threadPause = False  #unpauses thread
    elif answer == 'm':
            print("s = stop")
            print("+ = vol up")
            print("- = vol down")
            print("r = get next rand song")
         
            

    
