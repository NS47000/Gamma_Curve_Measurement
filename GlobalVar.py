import cv2
import os
import time
def Q35_close():
    os.system("adb shell am force-stop org.codeaurora.gallery")
    
def Q35_showpattern(img):
    Q35_close()
    cv2.imwrite("ReadyToPush.png",img)
    os.system("adb push ReadyToPush.png /storage/emulated/0/Pictures/")
    time.sleep(0.5)
    os.system("adb shell am start -t image/png -d file:///storage/emulated/0/Pictures/ReadyToPush.png -a android.intent.action.VIEW")
    time.sleep(0.5)
    


    

def Q35_remove_all():
    os.system("adb shell rm /storage/emulated/0/Pictures/*.png")

