from sikuli.Sikuli import *
import os
from ContentStudio import *
import logging

addImagePath("content-studio.sikuli\gfx")
class ContentStudioClipboard(object):
        def go_to_clipboard(self):
                csInstance = ContentStudio()
                ContentStudio.switch_to_content_studio(csInstance)
                if exists(Pattern("ClipboardTab.png").similar(0.70)):
                        click("ClipboardTab.png")
                elif exists("SectionsTab.png"):
                        click("SectionsTab.png")
                        click("ClipboardTab.png")
                elif exists("SectionsTabSelected.png"):
                        click("SectionsTabSelected.png")
                        click("ClipboardTab.png")
                        raise AssertionError("1")
        
        def clean_up_clipboard(self):
                csInstance = ContentStudio()
                ContentStudio.switch_to_content_studio(csInstance)
                ContentStudioClipboard.go_to_clipboard(self)

                if exists(Pattern("FirstContentOfClipboard.png").similar(0.90)):
                        click(Pattern("FirstContentOfClipboard.png").similar(0.90))
                elif exists("ClipboardTab.png"):
                        click(Pattern("ClipboardTab.png").targetOffset(25, -25))
                elif exists("ClipboardTabSelected.png"):
                        click(Pattern("ClipboardTabSelected.png").targetOffset(25, -25))
                
                while exists(Pattern("InboxItemSelected.png").similar(0.90)):
                        type(Key.DELETE)
                        click(Pattern("ClipboardTabSelected.png").targetOffset(25, -25))

        def check_clipboard(self):
                csInstance = ContentStudio()
                ContentStudio.switch_to_content_studio(csInstance)
                ContentStudioClipboard.go_to_clipboard(self)
                
                if exists(Pattern("FirstContentOfClipboard.png").similar(0.80)):
                        logging.info("At least one content available in clipboard")
                        doubleClick(Pattern("FirstContentOfClipboard.png").similar(0.80))
                elif exists(Pattern("InboxItemSelected.png").similar(0.80)):
                        logging.info("At least one content available in clipboard")
                        doubleClick(Pattern("InboxItemSelected.png").similar(0.80))
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("Clipboard is EMPTY. Screenshot: "+ImageName)
            
        
                
        def drag_content(self, DragDirection, ListName):
                csInstance = ContentStudio()
                ContentStudio.switch_to_content_studio(csInstance)
                
                ListImageName=ListName+'.png'
                
                if not exists("InboxesTab.png"):
                        click("SectionsTab.png")

                if exists("ListsTab.png"):
                        click("ListsTab.png")
                #else:
                        #raise AssertionError("Problem here")

                if exists(Pattern(ListImageName).similar(0.95)):
                        doubleClick(Pattern(ListImageName).similar(0.95))
                elif exists("ListIcon.png"):
                        print("Do Nothing")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError(ListName+' does not exist in the section content was created. Screeshot: '+ImageName)
                
                ContentStudioClipboard.go_to_clipboard(self)
                if exists("ClipboardTab.png"):
                        click(Pattern("ClipboardTab.png").targetOffset(25, -25))
                elif exists("ClipboardTabSelected.png"):
                        click(Pattern("ClipboardTabSelected.png").targetOffset(25, -25))
                
                if DragDirection == 'clipboard_to_list':
                        click(Pattern("ClipboardTabSelected.png").targetOffset(25, -25))
                        dragDrop(Pattern('InboxItemSelected.png').targetOffset(-1,67),Pattern('ListIcon.png').targetOffset(-15,30))
                        click(Pattern('ListIcon.png').targetOffset(-15,30))
                else:
                        click(Pattern('ListIcon.png').targetOffset(-15,30))
                        dragDrop(Pattern('ListIcon.png').targetOffset(-15,30),Pattern('EmptyClipboard.png').similar(0.90))
                        click(Pattern("ClipboardTabSelected.png").targetOffset(25, -25))

                ##Assertion Check: If the drag was successful then there should be a content selected.

                if exists(Pattern("InboxItemSelected.png").similar(0.90)):
                        print("Drag from clipboard to list was successful")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("Drag between list and clipboard was not successful. Screenshot: "+ImageName)

        def drag(self, *args):
                DragStartImage=args[0]+'.png'
                DragEndImage=args[1]+'.png'
                
                dragDrop(DragStartImage, DragEndImage)
                if exists("ClipboardTab.png"):
                        click(Pattern("ClipboardTab.png").targetOffset(25, -25))
                elif exists("ClipboardTabSelected.png"):
                        click(Pattern("ClipboardTabSelected.png").targetOffset(25, -25))
                
                

        def check_if_exists(self, uiElement):
                uiElementImage=uiElement+'.png'
                wait(5)
                if exists(Pattern(uiElementImage).similar(0.90)):
                        print("Exists")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError(uiElement+' does not exist. Screenshot: ' + ImageName)

                if exists(uiElementImage):
                        csInstance = ContentStudio()
                        ContentStudio.switch_to_content_studio(csInstance)

        def check_if_not_exists(self, uiElement):
                uiElementImage=uiElement+'.png'
                wait(5)
                if exists(Pattern(uiElementImage).similar(0.90)):
                        ImageName=capture_CS_screenshot()
                        raise AssertionError(uiElement+' exists. Screeshot: ' + ImageName)
                else:
                        print("Exists")

                if exists(uiElementImage):
                        csInstance = ContentStudio()
                        ContentStudio.switch_to_content_studio(csInstance)
                
        def select_item_from_clipboard(self):
                if exists(Pattern('ClipboardTab.png').similar(0.80)):
                        click(Pattern("ClipboardTab.png").targetOffset(25, -25))
                elif exists(Pattern('ClipboardTabSelected.png')):
                        click(Pattern("ClipboardTabSelected.png").targetOffset(25, -25))
                else:
                        ContentStudioClipboard.go_to_clipboard(self)
                        click(Pattern("ClipboardTab.png").targetOffset(25, -25))

        def open_selected(self):
                rightClick('InboxItemSelected.png')
                type(Key.DOWN)
                type(Key.ENTER)
