import winsound
import random
import os
import glob



def Enter_command():
    global soundfile
    soundfile = ''
    path = 'C:\soundfile'
    soundfiles = glob.glob(path + '\*.wav', recursive=False)
    soundfile = random.choice(soundfiles)
    print(soundfile)
    return int(soundfile.split('.')[1])


def stop_command():
    winsound.PlaySound(None, winsound.SND_ASYNC)


def music_one():
    winsound.PlaySound(soundfile, winsound.SND_ASYNC)








