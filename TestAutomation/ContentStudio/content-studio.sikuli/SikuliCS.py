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
    elif len(args) == 1:
        wait(int(args[0]))
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
        
    screenshotsDir = "TestResults\Screenshots"
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
        
    screenshotsDir = "TestResults\Screenshots"
    switchApp("Java Console - Content Studio")
    type(Key.SPACE, KeyModifier.ALT)
    type('x')
    img = capture(App.focusedWindow())
    shutil.move(img, os.path.join(screenshotsDir, imageName+".png"))
    switchApp('Escenic Content Studio ')
    #C.stop()

def maximize_content_studio_window():
    #***This Keyword Maximized Escenic Content Studio****#
    #Full screent content studio with SPACE+ALT+X
    type(Key.SPACE+"x", KeyModifier.ALT)

def restore_content_studio_window():
    #***This Keyword restores Escenic Content Studio****#
    #Restore content studio window with SPACE+ALT+R
    type(Key.SPACE, KeyModifier.ALT)
    type('r')

def print_version():
    if os.environ.has_key("ECE_Version") and os.environ.has_key("WF_Version"):
        sys.stderr.write("Testing Content Studio on : "+ os.environ['ECE_EDITORIAL_HOST'] + ". Engine: " + os.environ['ECE_Version'] + ". WF: " + os.environ['WF_Version'])
    elif os.environ.has_key("ECE_Version"):
        sys.stderr.write("Testing Content Studio on : "+ os.environ['ECE_EDITORIAL_HOST'] + ". Engine Version: " + os.environ['ECE_Version'])
    elif os.environ.has_key("WF_Version"):
        sys.stderr.write("Testing Content Studio on : "+ os.environ['ECE_EDITORIAL_HOST'] + ". WF Version: " + os.environ['WF_Version'])
    else:
        sys.stderr.write("Testing Content Studio on : "+ os.environ['ECE_EDITORIAL_HOST'])
    
