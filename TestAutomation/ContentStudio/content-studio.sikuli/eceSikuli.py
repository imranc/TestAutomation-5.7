from sikuli.Sikuli import *
import os
from ContentStudio import *
from SikuliCS import *
from ContentStudioClipboard import *
import logging

addImagePath("content-studio.sikuli\gfx")
class eceSikuli(object):
        
        def right_click_element(self, uiElement):
                uiElementImageName=uiElement+'.png'
                if exists(Pattern(uiElementImageName).similar(0.80)):
                        rightClick(Pattern(uiElementImageName).similar(0.80))
                else:
                        ScreenShot=capture_CS_screenshot()
                        raise AssertionError(uiElement+' does not exist. Screenshot: '+ScreenShot)


        def click_element(self, *args):
                wait(2)
                uiElement=args[0]
                #raise AssertionError(len(args))
                uiElementImageName=uiElement+'.png'
                if exists(Pattern(uiElementImageName).similar(0.80)):
                        if len(args) == 1:
                                click(Pattern(uiElementImageName).similar(0.80))
                        elif len(args) == 3:
                                click(Pattern(uiElementImageName).similar(0.80).targetOffset(int(args[1]), int(args[2])))
                        else:
                                raise AssertionError('Please follow the proper argument passing')
                else:
                        ScreenShot=capture_CS_screenshot()
                        raise AssertionError(uiElement+' does not exist. Screenshot: '+ScreenShot)

        def type_text(self, stringToType):
                type(stringToType)

        def type_key(self, *args):
                if args[0] == 'DOWN':
                        type(Key.UP)
                        #raise AssertionError(args[0])
                elif args[0] == 'ENTER':
                        type(Key.ENTER)
