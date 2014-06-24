from sikuli.Sikuli import *
import os
from SikuliCS import *
from time import gmtime, strftime
import datetime
from org.sikuli.script.natives import Vision


addImagePath("content-studio.sikuli\gfx")

class ContentStudio(object):
        def start_content_studio(self, *args):
                #***This Keyword Opens content studio from a browser
                ##Then login with UserName and password argument passed
                ##If UserName and Password not passed,
                ##this keyword logs in to Content Studio with ECE_UserName and ECE_Password variables passed from Jenkins***#
                
                browser=os.environ['browser']
                
                if browser=='IE':
                        BrowserPath='C:\Program Files\Internet Explorer\iexplore.exe'
                        BrowserApp=App.open(BrowserPath)
                        wait(5)
                        if exists("IE_prompt.png"):
                                click("IE_prompt.png")
                        switchApp("Internet Explorer")
                        wait(20)
                        while(1):
                               if exists("ie_address_bar.png"):
                                   break
                               else:
                                    type("l",KeyModifier.CTRL) 
                else:
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
        
                csUrl=ContentStudio.getCsAddress(self)
                paste(csUrl)
                print (csUrl)
                wait(5)
                type("\n")
                wait_for(Pattern("FirefoxOpenWithJavaws.png"),20)
                if exists("FirefoxOpenWithJavaws.png"):
                        wait(2)
                        type("\n")
                wait(60)
                #ContentStudio.switch_to_content_studio(self)
                if exists("JavaWarning.png"):
                        if exists("CheckBox.png"):
                                click("CheckBox.png")
                        
                        type(Key.ENTER)
                        
                wait(Pattern("login_content_studio.png").targetOffset(-248,1),500)
                
                if len(args) == 0:
                        userName=os.environ['ECE_UserName']
                        password=os.environ['ECE_Password']
                else:
                        userName=args[0]
                        password=args[1]
                        
                type(userName)
                wait(2)
                type(Key.TAB + password + Key.TAB + Key.ENTER)
                
                ContentStudio.close_browser(self)
                switchApp("Escenic Content Studio")
                maximize_content_studio_window()
                
                ##Assertion: Check if Section Tab or Search Tab exists
                wait_for("SearchTab.png", 100)
                
                if exists(Pattern("SearchTab.png")) or exists(Pattern("SectionTab.png")) or exists(Pattern("SectionsTabSelected.png")):
                        wait(2)
                        print("Log in successful")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError('Login Failed! Screenshot: '+ImageName)

        
                                      
        def getCsAddress(self):
                #***This keyword returns Content Studio url with the variables passed from Jenkins***#
                ece_host= os.environ['ECE_EDITORIAL_HOST']
                
                if "ECE_EDITORIAL_PORT" in os.environ:
                        ece_port= os.environ['ECE_EDITORIAL_PORT']
                        ece_Cs_address= 'http://'+ece_host+':'+ece_port+'/studio/Studio.jnlp'
                        
                else:
                        ece_Cs_address= 'http://'+ece_host+'/studio/Studio.jnlp'
                return ece_Cs_address
        
        def create_rss_feedpanel(self):
                #***This Keyword Creates RSS Feed panel with bbc technology rss feel***#
                ContentStudio.switch_to_content_studio(self)
                wait(2)
                ##Full screen content studio with SPACE+ALT+X
                type(Key.SPACE, KeyModifier.ALT)
                type('x')
                #Configure Research panel with CTRL+8
                type("8",KeyModifier.CTRL)
                if exists("new_research_panel.png", 200):
                    click("new_research_panel.png")
                wait(2)
                #type(Key.TAB + Key.TAB + Key.TAB + Key.TAB)
                click("rssFeedPanelUrl.png")
                wait(5)
                paste("http://feeds.bbci.co.uk/news/technology/rss.xml")
                click("OK_button.png")

                #Open created RSS feed Panel (CTRL+4) and close panel (CTRL+4)
                type("4", KeyModifier.CTRL)
                wait(10)
                type("4", KeyModifier.CTRL)

        
        def create_search_panel(self):
                #***This Keyword create search research panel***#
                ContentStudio.switch_to_content_studio(self)
                wait(2)
                ##Full screent content studio with SPACE+ALT+X
                type(Key.SPACE, KeyModifier.ALT)
                type('x')
                
                wait(10)
                #Configure Research panel with CTRL+8
                type("8",KeyModifier.CTRL)
                
                if exists("new_research_panel.png"):
                    click("new_research_panel.png")
                wait(2)
                click("ResearchPanelTypeDropdown.png")
                type(Key.DOWN)
                type(Key.ENTER)
                wait(2)
                click(Pattern("OK_button.png").similar(0.60))
                wait(5)

                #Open created RSS feed Panel (CTRL+4) and close panel (CTRL+4)
                #type("4", KeyModifier.CTRL)
                #wait(10)
                #type("4", KeyModifier.CTRL)

        def verify_research_panel(self, ResearchPanelType):
                #***This Keyword is the Assertion for creating resarch panel
                #Checks if resarch panel icon and Header is present or not***#
                ContentStudio.switch_to_content_studio(self)

                #CTRL+4  Show Research Panel
                type("4", KeyModifier.CTRL)
                
                wait(10)
                if exists("bbc_rss_feed_read.png")  and ResearchPanelType == 'RSS/ATOM':
                    print("PASS: BBC feed panel reviewd")
                elif exists("SearchResearchPanelAssertion.png") and ResearchPanelType == 'SEARCH':
                    print("PASS: Escenic Search Panel reviewed")
                else:
                    ImageName=capture_CS_screenshot()
                    type("4", KeyModifier.CTRL)
                    raise AssertionError('Actual and expected results are different! Screenshot: '+ImageName)

                #CTRL+4  Hide Research Panel
                type("4", KeyModifier.CTRL)

        def remove_research_panel(self):
                #***This Keyword removes Last created research panel***#
                type("8",KeyModifier.CTRL)
                while (exists("remove_panel.png")):
                        click("remove_panel.png")
                        wait(2)
                click(Pattern("OK_button.png").similar(0.60))

        def switch_to_content_studio(self):
                #***This Keyword switches focus to Escenic Content Studio***#
                #Vision.setParameter("MinTargetSize", 6)
                eceAppName="Escenic Content Studio "
                ScreenHighlighter.closeAll()
                #eceVersion=os.environ['ECE_Version']
                #eceAppName=eceAppName+eceVersion
                switchApp(eceAppName)

##        def maximize_content_studio_window(self):
##                #***This Keyword Maximized Escenic Content Studio****#
##                #Full screent content studio with SPACE+ALT+X
##                type(Key.SPACE, KeyModifier.ALT)
##                type('x')

        def open_section_panel(self):
                #***This Keyword makes section panel visible ***#
                ContentStudio.switch_to_content_studio(self)
                maximize_content_studio_window()
                
                if exists(Pattern("ExpansionIcon.png").similar(0.90)):
                        click("ExpansionIcon.png")
                elif exists("InboxesTab.png"):
                        print("Do nothing")
                else:
                        click("SectionTab.png")
                        wait(2)
                        
                        if exists(Pattern("ExpansionIcon.png").similar(0.90)):
                                click(Pattern("ExpansionIcon.png").similar(0.90))
                        elif not exists("HomeSection.png"):
                                type("4", KeyModifier.CTRL)
                                wait(2)
                                type("4", KeyModifier.CTRL)
                                click(Pattern("ExpansionIcon.png").similar(0.90))
                        else:
                                print("Do nothing")
                                
                if exists(Pattern("HomeSection.png").similar(1.00)):
                        click(Pattern("HomeSection.png").similar(1.00))
                        
        def right_click_section(self, SectionName):
                ContentStudio.open_section_panel(self)
                SectionImageName=SectionName+'Section.png'
                #if exists(Pattern("SectionTab.png")):
                      #  click("SectionTab.png")
                      #  if exists("HomeSection.png"):
                      #          click("HomeSection.png")
                #ContentStudio.close_allopen_tabs(self)
                
                        
                if exists(Pattern(SectionImageName).similar(0.95)):
                        rightClick(Pattern(SectionImageName).similar(0.95))
                else:
                        click(Pattern("ListsTab.png").targetOffset(0,-12))
                        wait(2)
                        corner=find(Pattern("ListsTab.png").targetOffset(0,-23))
                        drop_point = corner.getTarget().offset(50, 250)
                        dragDrop(corner, drop_point)

                        while exists(Pattern("ExpansionIcon.png").similar(0.90)):
                                click("ExpansionIcon.png")
                        
                        if exists(Pattern(SectionImageName).similar(0.95)):
                                rightClick(Pattern(SectionImageName).similar(0.95))
                        else:
                                ImageName=capture_CS_screenshot()
                                raise AssertionError(SectionName+' Section does not exist. Screenshot: '+ImageName)
                wait(2)
        
        def create_content_in_section(self, *args):
                #***This Keyword creates an Article in the specified section***#
                #***Create Content In Section SectionName***#

                ContentStudio.switch_to_content_studio(self)

                SectionName=args[0]
                
                if not exists(Pattern("InboxesTab.png").similar(0.60)):
                        click("SectionsTab.png")
                        
                ContentStudio.right_click_section(self, SectionName)
                wait_for("NewContent.png",20)
                click(Pattern("NewContent.png").targetOffset(100,0))
                wait_for("PictureContent.png",20)
                if exists("StoryContent.png"):
                        click("StoryContent.png")
                elif exists("NewsContent.png"):
                        click("NewsContent.png")
                wait(3)

                if len(args) > 1:
                        type(args[1])
                        type(Key.TAB)
                        type(args[1])
                        type(Key.TAB)
                        type(args[1])
                        type(Key.TAB)
                        type(args[1])
                else: 
                        type("This is the Title of an Article -- By Automated smoke tests")
                        type(Key.TAB)
                        type("This is the Subtitle of an Article -- By Automated smoke tests")
                        type(Key.TAB)
                        type("This is the Lead text of an Article -- By Automated smoke tests")
                        type(Key.TAB)
                        type("This is the Body of an Article -- By Automated smoke tests")
                        
                wait(3)
                click("SaveButton.png")
                wait(10)
                #wait_for("ContentUrl.png",30)
                
                if exists("PublishButton.png"):
                        click("PublishButton.png")
                elif exists(Pattern("ContentStatesList.png").targetOffset(65,0)):
                        click(Pattern("ContentStatesList.png").targetOffset(65,0))
                        wait(2)
                        click(Pattern("PublishButton.png").similar(0.50))
                        wait(1)
                        click("SaveButton.png")
                        
                wait(2)
                #wait_for("ContentUrl.png",30)        
                #type("7", KeyModifier.CTRL)
                
                if exists(Pattern("ContentUrl.png").similar(0.90)):
                        print("Content was successfully created")
                        click(Pattern("ContentUrl.png").targetOffset(12,10))
                else:
                        if exists(Pattern("ShowSideBar.png").similar(0.60)):
                                click(Pattern("ShowSideBar.png").similar(0.60))
                                if exists("ShowSideBar.png"):
                                        click("ShowSideBar.png")
                                if not exists(Pattern("ContentUrl.png").similar(0.90)):
                                        ImageName=capture_CS_screenshot()
                                        raise AssertionError("Content Url was not created. Check Content Studio. Screenshot: "+ImageName)
                                else:
                                        click(Pattern("ContentUrl.png").targetOffset(12,10))
                        else:
                                ImageName=capture_CS_screenshot()
                                raise AssertionError("Content Url was not created. Check Content Studio. Screenshot: "+ImageName)
                        
                wait(10)
                
                #while not exists("InboxesTab.png"):
                        #type("7", KeyModifier.CTRL)
                        #ContentStudio.switch_to_content_studio(self)

        def create_image_in_section(self, *args):
                #***This Keyword creates an Image in the specified section***#
                #***Create Image In Section  SectionName***#
                ContentStudio.switch_to_content_studio(self)

                SectionName=args[0]

                if not exists(Pattern("InboxesTab.png").similar(0.60)):
                        click("SectionsTab.png")
                
                ContentStudio.right_click_section(self, SectionName)
                wait(2)
                click(Pattern("NewContent.png").targetOffset(100,0))
                wait(2)
                click("PictureContent.png")
                wait(3)
                type("C:\Users\Public\Pictures\Sample Pictures\Lighthouse.jpg")
                type(Key.ENTER)
                #wait(Pattern("ContentUrl.png").similar(0.90),20)
                wait(10)
                type("a", KEY_CTRL)

                if len(args)>1:
                        type(args[1])
                else:
                        type("This image is created by automated smoke test BOT")
                        
                wait(2)
                wait(Pattern("SaveButton.png").similar(0.65),20)
                
                if exists("PublishButton.png"):
                        click("PublishButton.png")
                elif exists(Pattern("PublishButtonSimple.png")):
                        click(Pattern("PublishButtonSimple.png"))
                else:
                        click(Pattern("ContentStatesList.png").targetOffset(65,0))
                        wait(2)
                        click(Pattern("PublishButton.png").similar(0.50))
                        wait(1)
                        click("SaveButton.png")
                
                        
                type("7", KeyModifier.CTRL)
                
                if exists(Pattern("ContentUrl.png").similar(0.90)):
                        print("Content was successfully created")
                        click(Pattern("ContentUrl.png").targetOffset(12,10))
                else:
                        if exists(Pattern("ShowSideBar.png").similar(0.60)):
                                click(Pattern("ShowSideBar.png").similar(0.60))
                                if exists("ShowSideBar.png"):
                                        click("ShowSideBar.png")
                                if not exists(Pattern("ContentUrl.png").similar(0.90)):
                                        ImageName=capture_CS_screenshot()
                                        raise AssertionError("Content Url was not created. Check Content Studio. Screeshot: "+ImageName)
                                else:
                                        click(Pattern("ContentUrl.png").targetOffset(12,10))
                        else:
                                ImageName=capture_CS_screenshot()
                                raise AssertionError("Content Url was not created. Check Content Studio. Screenshot: "+ImageName)
                
                wait(5)
                
                while not exists("InboxesTab.png"):
                        type("7", KeyModifier.CTRL)
                        ContentStudio.switch_to_content_studio(self)

        def add_content_to_section(self, inboxSection, destinationSection):
                #***This keyword drags the first content from 1st argument section to 2nd Argument
                #section's Center Column***#
                ContentStudio.switch_to_content_studio(self)
                #maximize_content_studio_window()
                
                if not exists("InboxesTab.png"):
                        click("SectionsTab.png")
                
                if exists("HomeSection.png"):
                        click("HomeSection.png")
                #else:
                        #click("SectionsTab.png") 
                        
                inboxSectionImageName=inboxSection+'Section.png'
                destinationSectionImageName=destinationSection+'Section.png'
                wait(Pattern(destinationSectionImageName),10)
                wait(Pattern(inboxSectionImageName),10)
                doubleClick(Pattern(destinationSectionImageName).similar(0.95))

                if exists("HomeSection.png"):
                        click("HomeSection.png")

                click(Pattern(inboxSectionImageName).similar(0.95))

                click("InboxesTab.png")
                #waitVanish(Pattern("InboxLoading.png").similar(0.90), 30)
                #setAutoWaitTimeout(10)
                wait(Pattern("FirstContentOfInbox.png").targetOffset(-1,67), 20)
                wait(2)
                
                if exists('CenterColumn.png') or exists('ContentArea.png'):
                        ##Drag content from inbox to center column
                        print("Do nothing")
                elif exists("RightColumn.png"):
                        click("RightColumn.png")

                wait(10)
                
                if exists('CenterColumn.png'):
                        dragDrop(Pattern('FirstContentOfInbox.png').targetOffset(-1,67),'CenterColumn.png')
                elif exists('ContentArea.png'):
                        dragDrop(Pattern('FirstContentOfInbox.png').targetOffset(-1,67),'ContentArea.png')
                        
                wait(Pattern("SaveButton.png").similar(0.65),10)
                if exists(Pattern("PublishButton.png")):
                        click(Pattern("PublishButton.png"))
                elif exists(Pattern("PublishButtonSimple.png")):
                        click(Pattern("PublishButtonSimple.png"))
                
                if inboxSection==destinationSection:
                        print("Content added to destination Section")
                else:
                        wait(2)

        def remove_content_from_section(self, sectionName):
                ContentStudio.switch_to_content_studio(self)
                maximize_content_studio_window()
                wait(5)
                
                if not exists("InboxesTab.png"):
                        click("SectionsTab.png")
                        #raise AssertionError('Problem Here')
                
                if exists("HomeSection.png"):
                        click("HomeSection.png")
                        
                sectionImageName=sectionName+'Section.png'
                wait(Pattern(sectionImageName),10)
                doubleClick(Pattern(sectionImageName).similar(0.95))
                
                if exists('CenterColumn.png') or exists('ContentArea.png'):
                        print("Do nothing")
                elif exists("RightColumn.png"):
                        ##If center column is selected, Deselect it by pressing UP key
                        click("RightColumn.png")
                        
                if exists('CenterColumn.png'):
                        click('CenterColumn.png')
                elif exists('ContentArea.png'):
                        click('ContentArea.png')
                        
                type(Key.DOWN)
                type(Key.DELETE)
                wait(5)
                
                if exists(Pattern("PublishButton.png").similar(0.65)):
                        #wait(Pattern("PublishButton.png"),10)
                        click(Pattern("PublishButton.png").similar(0.65))
                elif exists(Pattern("PublishButtonSimple.png")):
                        click(Pattern("PublishButtonSimple.png"))
                else:
                        print("No content in the section")

        def close_allopen_tabs(self):
                ContentStudio.switch_to_content_studio(self)
                maximize_content_studio_window()
                count=0
                
                while exists(Pattern("CloseTabs.png").similar(0.80)):
                        click("CloseTabs.png")
                        wait(1)
                        if count>50:
                                ImageName=capture_CS_screenshot()
                                raise AssertionError("Something went wrong while closing open tabs. Screenshot: "+ImageName)
                                break
                        count +=1
                        if exists("DontSaveButton.png", 1):
                                click("DontSaveButton.png")
                                wait(3)

        def deselect_contents_inbox(self):
                ##"Clean Up Inbox" and "Create Content In Section" before running this keyword
                ContentStudio.switch_to_content_studio(self)
                maximize_content_studio_window()
                click("InboxesTab.png")
                if exists(Pattern("InboxDeselectDropDown.png").similar(0.90)):
                        click(Pattern("InboxDeselectDropDown.png").similar(0.90).targetOffset(25,0))
                        wait(1)
                        click("InboxDeselect.png")
                        type(Key.ESC)
                        wait(Pattern("SaveButton.png").similar(0.65),10)

                        if exists(Pattern("SaveButton.png").similar(0.65)):
                                click(Pattern("SaveButton.png").similar(0.65))
                        elif exists(Pattern("PublishButton.png").similar(0.65)):
                                click(Pattern("PublishButton.png").similar(0.65))
                else:
                        restore_content_studio_window()
                        maximize_content_studio_window()
                        if not exists(Pattern("InboxDeselectDropDown.png").similar(0.90)):
                                ImageName=capture_CS_screenshot()
                                raise AssertionError("Create A Content Before Deselecting inbox or May be content is already Deselected from Inbox. Screenshot: "+ImageName)

                ##Check if content exists in the inbox
                wait(20)
                
                click(Pattern("FirstContentOfInbox.png").similar(0.70))
                if exists(Pattern("InboxItemSelected.png").similar(0.90)):
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("Deselect was not successful. Screenshot: "+ImageName)
                else:
                        print("Successful deselection")

        def select_contents_inbox(self):
                ContentStudio.switch_to_content_studio(self)
                maximize_content_studio_window()
                click("InboxesTab.png")
                if exists(Pattern("InboxSelectDropDown.png").similar(0.90)):
                        click(Pattern("InboxSelectDropDown.png").similar(0.90).targetOffset(11,1))
                        click("InboxSelect.png")
                        type(Key.ESC)
                        wait(Pattern("SaveButton.png").similar(0.65),10)
                        
                        if exists(Pattern("SaveButton.png").similar(0.65)):
                                click(Pattern("SaveButton.png").similar(0.65))
                        elif exists(Pattern("PublishButton.png").similar(0.65)):
                                click(Pattern("PublishButton.png").similar(0.65))
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("Create A Content and Deselect inbox Before Selecting inbox or May be content is already selected. Screenshot: "+ImageName)

                ##Check if content exists in the inbox
                wait(15)
                
                click(Pattern("FirstContentOfInbox.png").similar(0.80))
                if exists(Pattern("InboxItemSelected.png").similar(0.90)):
                        print("Inbox selection was successful")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("Inbox selection was not successful. Screenshot: "+ImageName)

        def clean_up_inbox(self, sectionName):
                ContentStudio.open_section_panel(self)
                SectionImageName=sectionName+'Section.png'
                if exists(Pattern(SectionImageName).similar(0.95)):
                        click(Pattern(SectionImageName).similar(0.95))
                else:
                        print("Do nothing")
                click("InboxesTab.png")       
                waitVanish(Pattern("InboxLoading.png").similar(0.90))
                #setAutoWaitTimeout(10)
                wait(2)
                #wait(Pattern("FirstContentOfInbox.png").similar(0.80), 20)
                #wait(2)
                ContentStudio.close_allopen_tabs(self)
                if exists(Pattern("FirstContentOfInbox.png").similar(0.70)):
                        click(Pattern("FirstContentOfInbox.png").similar(0.70))
                
                while exists(Pattern("InboxItemSelected.png").similar(0.90)):
                        #click(Pattern("FirstContentOfInbox.png").targetOffset(-1,60).similar(0.90))
                        type(Key.DELETE)

        def create_new_list(self, sectionName, listName):
                ContentStudio.switch_to_content_studio(self)
                ContentStudio.open_section_panel(self)
                
                SectionImageName=sectionName+'Section.png'
                if exists(Pattern(SectionImageName).similar(0.95)):
                        click(Pattern(SectionImageName).similar(0.95))
                else:
                        print("Do nothing")



                ContentStudio.right_click_section(self, sectionName)
                if exists("CreateNewList.png"):
                        click("CreateNewList.png")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("CreateNewList does not exists. Screenshot: "+ImageName)

                type(Key.SPACE)
                type(listName)
                type(Key.ENTER)
                wait(2)

                if exists(Pattern("FailedToCreate.png").similar(0.90)):
                        ImageName=capture_CS_screenshot()
                        type(Key.ENTER)
                        raise AssertionError("Create List with a diffrent name. List with the same name already exists. Screenshot: "+ImageName)

        def add_content_to_list(self, sectionName):
                ContentStudio.switch_to_content_studio(self)
                sectionListsInboxImage = sectionName + 'ListsInbox.png'
                if sectionName == "Home" and exists(Pattern("ListsDropDown.png").similar(1.00)):
                        click(Pattern("ListsDropDown.png").similar(1.00).targetOffset(-15,0))
                elif exists(Pattern("ListsDropDownHomeSection.png")):
                        click(Pattern("ListsDropDownHomeSection.png").targetOffset(-14,0))
                else:
                        #Uncheck from inbox
                        click(Pattern(sectionListsInboxImage).targetOffset(30, 0))
                        wait(2)
                        click("InboxDeselect.png")
                        type(Key.ESC)
                        click("HomeSection.png")
                        click(Pattern(sectionListsInboxImage).similar(0.80).targetOffset(98, 1))
                        wait(2)
                        
                if exists(Pattern("NewsListCheckbox.png").similar(0.90)):
                        click(Pattern("NewsListCheckbox.png").similar(0.90))
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("A list named NewsList should be created first. Screenshot: "+ImageName)
                
                type(Key.ESC)
                #click(sectionName+'Section.png')
                #click(Pattern(sectionListsInboxImage).targetOffset(0, 0))
                wait(2)
                #if exists("InboxSelect.png"):
                #        click("InboxSelect.png")
                type(Key.ESC)
                

                if exists(Pattern("PublishButton.png").similar(0.80)):
                        click(Pattern("PublishButton.png").similar(0.80))
                elif exists(Pattern("PublishButtonSimple.png").similar(0.80)):
                        click(Pattern("PublishButtonSimple.png").similar(0.80))
                else:
                        click(Pattern("SaveButton.png").similar(0.65))
                        
                click("ListsTab.png")
                
                if exists(Pattern("NewsList.png").similar(0.90)):
                        doubleClick(Pattern("NewsList.png").similar(0.90))
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("A list named NewsList should be created first in the section: "+ sectionName +'. Screenshot: '+ImageName)

                ###Assertion check
                #wait(Pattern("ListAssertion.png"), 50)
                wait(15)
                if exists(Pattern("ListAssertion.png")):
                        print("Select The content's list was successful")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError("There is no article in the list. Screenshot: "+ImageName)
                
                if sectionName=="Home":
                        doubleClick(Pattern("HomeSection.png").targetOffset(19,15))


        def clean_up_list(self, SectionName, ListName):
                if not exists(Pattern("ClipboardTab.png").similar(0.80)):
                        click("SectionTab.png")
                        
                doubleClick("HomeSection.png")
                SectionImageName=SectionName+'Section.png'

                wait(2)
                
                if exists(Pattern(SectionImageName).similar(0.95)):
                        click(Pattern(SectionImageName).similar(0.95))
                else:
                        print("Do nothing")

                wait(2)
                click("ListsTab.png")
                ListImageName=ListName+'.png'
                doubleClick(Pattern(ListImageName).similar(0.90))
                waitVanish("Loading.png",20)
                
                if exists("ListAssertion.png"):
                        click("ListAssertion.png")
                        type(Key.DELETE)
                        
                while exists("ListAssertion.png") or exists("InboxItemSelected.png"):
                        type(Key.DELETE)

                if SectionName=="Home":
                        doubleClick(Pattern("HomeSection.png").targetOffset(19,15))

        def delete_list(self, sectionName, listName):
                ContentStudio.open_section_panel(self)
                
                SectionImageName=sectionName+'Section.png'

                if exists("HomeSection.png"):
                        click("HomeSection.png")

                if exists(Pattern(SectionImageName).similar(0.95)):
                        click(Pattern(SectionImageName).similar(0.95))
                        wait(5)
                else:
                        print("Do nothing")

                click("ListsTab.png")
                wait(2)
                
                if exists(Pattern("NewsList.png").similar(0.90)):
                        click(Pattern("NewsList.png").similar(0.90))
                        
                type(Key.DELETE)
                wait(2)
                type(Key.ENTER)

        def preview_content(self, *args):
                #if exists("PreviewButton.png"):
                #        click(Pattern("PreviewButton.png").targetOffset(40,0))
                #elif exists(Pattern("PreviewButton.png").similar(0.60)):
                #        click(Pattern("PreviewButton.png").similar(0.60))
                ContentStudio.switch_to_content_studio(self)
                click("PreviewTab.png")
                wait(2)

                if args[0] == "All":
                        type(Key.DOWN)
                        click(Pattern("PreviewAll.png").targetOffset(-30, 0))

                click(Pattern("OpenInBrowser.png"))
                #type(Key.ENTER)
                wait(5)
                #while not exists(Pattern("InboxesPagesListsTab.png").similar(0.60)):
                ContentStudio.switch_to_content_studio(self)
                if exists("EditorTab.png"):
                        click("EditorTab.png")
                else:
                        click("DeskTab.png")
                wait(2)

        def update_content(self, *args):
                ContentStudio.switch_to_content_studio(self)
                wait(2)
                if args[0] == "Article" or args[0] == "article":
                        click("ListsTab.png")
                        wait(2)
                        click("Title:")
                        
                type("a", KEY_CTRL)
                type("Updated Content Title")
                if exists("PublishButton.png"):
                        click("PublishButton.png")
                else:
                        click("SaveButton.png")
                click(Pattern("ContentUrl.png").targetOffset(12,10))
                wait(5)
                #while not exists("InboxesTab.png"):
                #        ContentStudio.switch_to_content_studio(self)

        def delete_content(self):
                ContentStudio.switch_to_content_studio(self)
                
                if exists("WorkflowButton.png"):
                        click(Pattern("WorkflowButton.png").targetOffset(35,5))
                elif exists("PublishedContent.png"):
                        click("PublishedContent.png")
                        
                wait(2)
                
                if exists("DeleteButton.png"):
                        click("DeleteButton.png")
                elif exists("DeletedButton.png"):
                        click("DeletedButton.png")
                        click("SaveButton.png")
                        
                type(Key.ENTER)
                wait(2)

        def achieve_lock(self):
                ContentStudio.switch_to_content_studio(self)
                wait(2)
                click('Title:')
                type(Key.SPACE)

        def undo(self):
                type("z", KeyModifier.CTRL)
        
        def redo(self):
                type("y", KeyModifier.CTRL)

        def undo_from_menu(self):
                 type(Key.F10 + Key.RIGHT + Key.DOWN + Key.ENTER)

        def redo_from_menu(self):
                type(Key.F10 + Key.RIGHT + Key.DOWN + Key.DOWN + Key.ENTER)

        def copy_from_menu(self):
                type(Key.F10 + Key.RIGHT + Key.DOWN + Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER)

        def paste_from_menu(self):
                type(Key.F10 + Key.RIGHT + Key.DOWN + Key.DOWN + Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER)

        def cut_from_menu(self):
                type(Key.F10 + Key.RIGHT + Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER)

        def close_browser(self):
                if exists("FirefoxStoppedWorking.png"):
                        switchApp("Firefox")
                        click(Pattern("FirefoxStoppedWorking.png").targetOffset(-100,50))
                        
                if os.environ['browser']=='firefox':
                        switchApp("Mozilla Firefox")
                        #closeApp("Mozilla Firefox")
                else:
                        switchApp("Internet Explorer")
                        #closeApp("Internet Explorer")
                wait(5)
                type(Key.F4,KEY_ALT)
                wait(5)
                while exists("CloseTabsFirefox.png"):
                        switchApp("Firefox")
                        click("CloseTabsFirefox.png")

        def check_if_exists_text(self, *args):
                region=Region(0,0,2000,2000)
                if exists(args[0]):
                        print("Awesome")
                        #raise AssertionError("Awesome")
                else:
                        ImageName=capture_CS_screenshot()
                        raise AssertionError('"'+args[0]+'" not present. Please try with one word at a time. Screenshot: '+ImageName)
