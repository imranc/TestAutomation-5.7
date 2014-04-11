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
                wait(2)

        def type_text(self, stringToType):
                type(stringToType)

        def type_key(self, *args):
                if args[0] == 'DOWN':
                        type(Key.DOWN)
                        #raise AssertionError(args[0])
                elif args[0] == 'ENTER':
                        type(Key.ENTER)
                elif args[0] == 'ESC':
                        type(Key.ESC)
                elif args[0] == 'DELETE':
                        type(Key.DELETE)


        def click_element_if_exists(self, *args):
                checkElementExists = args[0]
                checkElementExistsImageName = checkElementExists+'.png'
                uiElement=args[1]
                uiElementImageName=uiElement+'.png'
             
                if exists(Pattern(checkElementExistsImageName).similar(0.80)):
                        if len(args) == 2:
                                eceSikuli.click_element(self, uiElement, 0, 0)
                        elif len(args) == 4:
                                eceSikuli.click_element(self, uiElement, args[2], args[3])

                wait(2)

        def drag_and_drop_element(self, *args):
                dragSource = args[0]
                dragSourceImageName = dragSource+'.png'
                dragDestination = args[1]
                dragDestinationImageName = dragDestination+'.png'
                
                if exists(Pattern(dragSourceImageName).similar(0.80)) and exists(Pattern(dragDestinationImageName).similar(0.80)):
                        dragDrop(dragSourceImageName, dragDestinationImageName)
                else:
                        ScreenShot=capture_CS_screenshot()
                        raise AssertionError("Either drag source or drop destination images showing some problems..")
                
                        

        def double_click_element(self, *args):
                wait(2)
                uiElement=args[0]
                #raise AssertionError(len(args))
                uiElementImageName=uiElement+'.png'
                if exists(Pattern(uiElementImageName).similar(0.80)):
                        if len(args) == 1:
                                doubleClick(Pattern(uiElementImageName).similar(0.80))
                        elif len(args) == 3:
                                doubleClick(Pattern(uiElementImageName).similar(0.80).targetOffset(int(args[1]), int(args[2])))
                        else:
                                raise AssertionError('Please follow the proper argument passing')
                else:
                        ScreenShot=capture_CS_screenshot()
                        raise AssertionError(uiElement+' does not exist. Screenshot: '+ScreenShot)


        def open_browser_to_publication(self, *args):
                if len(args) == 0:
                        eceSikuli.open_browser(self, os.environ['publication'])
                elif len(args) == 1:
                        url = os.environ['publication']
                        url = url+args[0]
                        eceSikuli.open_browser(self, url)

        def open_browser(self, *args):
                if len(args) == 0:
                        raise AssertionError('URL should be provider with "Open Browser" keyword.')
                elif len(args) == 1:
                        BrowserPath='C:\Program Files\Mozilla Firefox\\firefox.exe'
                        BrowserApp=App.open(BrowserPath)
                        switchApp("Mozilla Firefox")
                        wait(10)
                        type("l",KeyModifier.CTRL)
                        paste(args[0])
                        wait(5)
                        type(Key.ENTER)
                        wait(2)
                else:
                        raise AssertionError("Too many arguments")
