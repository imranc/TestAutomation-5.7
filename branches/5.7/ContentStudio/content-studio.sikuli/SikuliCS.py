from sikuli.Sikuli import *
import os
import logging
from sikuli.Sikuli import *
from ContentStudio import *
import shutil
from time import gmtime, strftime
import datetime
#import castro

ScreenShot=0
addImagePath("content-studio.sikuli\gfx")

def wait_for(*args):
    ##This function works same as wait(pattern object, time in seconds)

    if len(args) == 2:
        wait_time=(args[1]-1)

        for x in range(0,args[1]):
            if exists(args[0]):
                break
                raise AssertionError('test')
            elif x == wait_time:
                #ScreenShotImageName='ScreenShot-'+str(ScreenShot)
                ImageName=capture_CS_screenshot()
                raise AssertionError("Something went wrong while waiting for " + str(args[0])+". Check screenshot "+ImageName)
            else:
                wait(1)
    else:
        for x in range(0,1000):
            if exists(args[0]):
                break
            else:
                wait(1)

def capture_CS_screenshot(*args):
    if len(args) == 0:
        imageName=(os.environ['BuildNumber'])
        currentTime=datetime.datetime.now().strftime("%B-%d-%H-%M-%S")
        imageName = imageName+ '.' + currentTime
    else:
        imageName=args[0]
        
    screenshotsDir = "C:/Test-automation/ContentStudio/TestResults/Screenshots"
    img = capture(App.focusedWindow())
    shutil.move(img, os.path.join(screenshotsDir, imageName+".png"))
    capture_java_console_screenshot()
    return imageName+'.png'

def capture_java_console_screenshot():
    #C = Castro()
    #C.start()
    imageName=(os.environ['BuildNumber'])
    currentTime=datetime.datetime.now().strftime("%B-%d-%H-%M-%S")
    imageName = imageName + '.JAVA_CONSOLE' + '-' + currentTime
        
    screenshotsDir = "C:/Test-automation/ContentStudio/TestResults/Screenshots"
    switchApp("Java Console - Content Studio")
    type(Key.SPACE, KeyModifier.ALT)
    type('x')
    img = capture(App.focusedWindow())
    shutil.move(img, os.path.join(screenshotsDir, imageName+".png"))
    switchApp('Escenic Content Studio '+ os.environ['ECE_Version'])
    #C.stop()

def maximize_content_studio_window():
    #***This Keyword Maximized Escenic Content Studio****#
    #Full screent content studio with SPACE+ALT+X
    type(Key.SPACE, KeyModifier.ALT)
    type('x')

def restore_content_studio_window():
    #***This Keyword restores Escenic Content Studio****#
    #Restore content studio window with SPACE+ALT+R
    type(Key.SPACE, KeyModifier.ALT)
    type('r')

def print_version():
    sys.stderr.write("Testing Content Studio Version: " + os.environ['ECE_Version'])
    
