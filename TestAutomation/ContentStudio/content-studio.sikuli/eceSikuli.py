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
                wait(5)

        def mouse_over(self, *args):
                wait(2)
                uiElement=args[0]
                #raise AssertionError(len(args))
                uiElementImageName=uiElement+'.png'
                if exists(Pattern(uiElementImageName).similar(0.80)):
                        if len(args) == 1:
                                mouseMove(Pattern(uiElementImageName).similar(0.80))
                        elif len(args) == 3:
                                mouseMove(Pattern(uiElementImageName).similar(0.80).targetOffset(int(args[1]), int(args[2])))
                        else:
                                raise AssertionError('Please follow the proper argument passing')
                else:
                        ScreenShot=capture_CS_screenshot()
                        raise AssertionError(uiElement+' does not exist. Screenshot: '+ScreenShot)
                wait(5)

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
                elif args[0] == 'TAB':
                        type(Key.TAB)
                elif args[0] == 'SPACE':
                        type(Key.SPACE)
                elif args[0] == 'f' and args[1] == 'ALT':
                        type('f',KeyModifier.ALT)
                elif args[0] == 'CTRL' and args[1] == '7':
                        type('7', KeyModifier.CTRL)
                elif args[0] == 'UP':
                        type(Key.UP)


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

        def type_text_if_element_exists(self, *args):
                checkElementExists = args[0]
                checkElementExistsImageName = checkElementExists+'.png'
             
                if exists(Pattern(checkElementExistsImageName).similar(0.95)):
                        if len(args) == 2:
                                eceSikuli.click_element(self, checkElementExists, 0, 0)
                                eceSikuli.type_text(self, args[1])
                        elif len(args) == 4:
                                eceSikuli.click_element(self, checkElementExists, args[1], args[2])
                                eceSikuli.type_text(self, args[3])
                        else:
                                raise AssertionError("Image name and a text must be passed as argument.")

                wait(2)

        def drag_and_drop_element(self, *args):
                dragSource = args[0]
                dragSourceImageName = dragSource+'.png'
                dragDestination = args[1]
                dragDestinationImageName = dragDestination+'.png'
                if len(args) == 2:
                        if exists(Pattern(dragSourceImageName).similar(0.80)) and exists(Pattern(dragDestinationImageName).similar(0.80)):
                                dragDrop(dragSourceImageName, dragDestinationImageName)
                elif len(args) == 4:
                        offset_x = int(args[2])
                        offset_y = int(args[3])
                        if exists(Pattern(dragSourceImageName).similar(0.80)) and exists(Pattern(dragDestinationImageName).similar(0.80)):
                                corner=find(Pattern(dragSourceImageName).targetOffset(0,0))
                                drop_point = find(Pattern(dragDestinationImageName).targetOffset(offset_x,offset_y))
                                dragDrop(corner, drop_point)                         
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


        def open_browser_to_studio(self, *args):
                if len(args) == 0:
                        csInstance = ContentStudio()
                        csUrl=ContentStudio.getCsAddress(csInstance)
                        eceSikuli.open_browser(self, csUrl)
                elif len(args) == 1:
                        csInstance = ContentStudio()
                        csUrl=ContentStudio.getCsAddress(csInstance)
                        url = csUrl+'?'+args[0]
                        eceSikuli.open_browser(self, url)
                wait(5)
        
        def open_browser_to_publication(self, *args):
                if len(args) == 0:
                        eceSikuli.open_browser(self, os.environ['publication'])
                elif len(args) == 1:
                        url = os.environ['publication']
                        url = url+args[0]
                        eceSikuli.open_browser(self, url)
                wait(5)

        def open_browser(self, *args):
                if len(args) == 0:
                        raise AssertionError('URL should be provider with "Open Browser" keyword.')
                elif len(args) == 1:
                        BrowserPath='C:\Program Files\Mozilla Firefox\\firefox.exe'
                        BrowserApp=App.open(BrowserPath)
                        switchApp("Mozilla Firefox")
                        while exists("FirefoxStoppedWorking.png"):
                                switchApp("Firefox")
                                click(Pattern("FirefoxStoppedWorking.png").targetOffset(-100,50))
                                BrowserPath='C:\Program Files\Mozilla Firefox\\firefox.exe'
                                BrowserApp=App.open(BrowserPath)
                                switchApp("Mozilla Firefox")
                        wait(10)
                        type("l",KeyModifier.CTRL)
                        paste(args[0])
                        wait(5)
                        type(Key.ENTER)
                        wait(5)
                        eceSikuli.maximize_browser_window(self)
                        wait(2)
                else:
                        raise AssertionError("Too many arguments")

        def open_browser_to_webstudio(self):
                eceSikuli.open_browser(self, eceSikuli.getWsAddress(self))

        def maximize_browser_window(self):
                #***This Keyword Maximizes browser window****#
                #Full screent content studio with SPACE+ALT+X
                type(Key.SPACE, KeyModifier.ALT)
                type('x')
        
        def getWsAddress(self):
                ece_host= os.environ['ECE_EDITORIAL_HOST']
                ece_port= os.environ['ECE_EDITORIAL_PORT']
                ece_ws_address= 'http://'+ece_host+':'+ece_port+'/escenic'
                return ece_ws_address

        def change_input_language(self):
                type(Key.SHIFT, KeyModifier.ALT)
                wait(2)


        def scroll_element(self, *args):
                #***This keyword scroll a element to specified target axis***#
                                
                ScrollImageName = args[0]+'.png'
                                
                offset_x = int(args[1])
                                
                offset_y = int(args[2])
                                
                if exists(Pattern(ScrollImageName).similar(0.90)):
                        corner=find(Pattern(ScrollImageName).targetOffset(0,0))
                        drop_point = corner.getTarget().offset(offset_x, offset_y)
                        dragDrop(corner, drop_point)
                                
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError(ScrollImageName+'Image does not exist. Screenshot: '+ImageName)
                
        def get_content_id(self, *args):
                csInstance = ContentStudio()
                ContentStudio.switch_to_content_studio(csInstance)
                wait(2)
                doubleClick(Pattern("ContentInfoPanel.png").targetOffset(65,60))
                wait(2)
                type("c", KEY_CTRL)
                wait(2)
                return Env.getClipboard().strip()

        def clean_up_desk(self, sectionName):
                csInstance = ContentStudio()
                ContentStudio.open_section_panel(csInstance)
                SectionImageName=sectionName+'Section.png'
                wait(2)
                if exists(Pattern(SectionImageName).similar(0.95)):
                        doubleClick(Pattern(SectionImageName).similar(0.95))
                        wait(2)		   
                else:
                       print("Do nothing")
                       
                
                #setAutoWaitTimeout(10)
                wait(10)
                #wait(Pattern("FirstContentOfInbox.png").similar(0.80), 20)
                #wait(2)
                
                if exists(Pattern("FirstContentOfDesk.png").similar(0.70)):
                        click(Pattern("FirstContentOfDesk.png").targetOffset(10,15).similar(0.70))
                        wait(2)
                
                        while exists(Pattern("DeskItemselected.png").similar(0.90)):
                        #click(Pattern("FirstContentOfInbox.png").targetOffset(-1,60).similar(0.90))
                                type(Key.DELETE)
                                if exists(Pattern("FirstContentOfDesk.png").similar(0.70)):
                                        click(Pattern("FirstContentOfDesk.png").targetOffset(10,15).similar(0.70))
                                        wait(2)

                        wait(3)
                        if exists("SaveButton.png"):
                                click("SaveButton.png")
                        wait(10)
                
                        if exists("PublishButtonSimple.png"):
                                click("PublishButtonSimple.png")
