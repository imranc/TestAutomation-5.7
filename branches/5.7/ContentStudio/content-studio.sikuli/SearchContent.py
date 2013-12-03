from sikuli.Sikuli import *
import os
from ContentStudio import *
from SikuliCS import *
from ContentStudioClipboard import *
import logging

addImagePath("content-studio.sikuli\gfx")
class SearchContent(object):
        def search(self, searchType):
                csInstance = ContentStudio()
                ContentStudio.switch_to_content_studio(csInstance)
                
                if not exists(Pattern("AdvancedButton.png").similar(0.80)):
                        click("SearchTab.png")
                        #wait(50)
                if not searchType=='simple':
                        click("AdvancedButton.png")
                        wait(2)
                        click(Pattern("PublishedContent.png").similar(0.90))

                ##Assertion: Check if exists a content for a minute ago
                
                for x in range(0,10):
                        wait(10)
                        click("ExecuteSearch.png")
                        if exists(Pattern("CreatedOneMinAgo.png").similar(0.50)):
                            break
                        elif x==10:
                            ImageName=capture_CS_screenshot()
                            raise AssertionError("Problem with search. Screenshot: "+ImageName)

           
                ##Change back to simple search
                if not searchType=='simple':
                        keyDown(Key.CTRL)
                        click(Pattern("PublishedContentSelected.png").similar(0.80))
                        keyUp(Key.CTRL)
                        click("AdvancedButton.png")

        def check_search(self):
                csInstance = ContentStudio()
                ContentStudio.switch_to_content_studio(csInstance)
                
                SearchContent.search(self, 'simple')
                click(Pattern("ClipboardTab.png").targetOffset(25, 100))
                
                if exists(Pattern("FirstContentOfClipboard.png").similar(0.90)):
                        logging.info("At least one content available in clipboard")
                        doubleClick(Pattern("FirstContentOfClipboard.png").similar(0.90))
                elif exists(Pattern("InboxItemSelected.png").similar(0.90)):
                        logging.info("At least one content available in clipboard")
                        doubleClick(Pattern("InboxItemSelected.png").similar(0.90))
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("Clipboard is EMPTY. Screenshot: "+ImageName)
