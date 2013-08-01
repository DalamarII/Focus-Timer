# Focus Timer.py
from time import sleep
import winsound

def StartTimer(minutes):
    seconds = int(minutes) * 60

    for k in range(seconds, 0, -1):
        print(k)
        sleep(1)

    winsound.PlaySound("chiming pottery.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)

while 1:
    minutes = input("Focus for how many minutes? ('q' to quit) ")
    if 'q' == minutes:
        break;
    StartTimer(minutes)
