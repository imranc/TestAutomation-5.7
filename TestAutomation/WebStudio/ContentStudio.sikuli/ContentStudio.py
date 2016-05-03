import os
from time import gmtime, strftime
import datetime
from robotremoteserver import RobotRemoteServer
from org.sikuli.script.natives import Vision
from sikuli.Sikuli import *


addImagePath("ContentStudio.sikuli/gfx")

class ContentStudio(object):
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

        def drag_and_drop_with_sikuli(self, *args):
                dragSource = args[0]
                dragSourceImageName = dragSource+'.png'
                dragDestination = args[1]
                dragDestinationImageName = dragDestination+'.png'
                if len(args) == 2:
                    if exists(Pattern(dragSourceImageName).similar(0.80)) and exists(Pattern(dragDestinationImageName).similar(0.80)):
                            drop_point = find(Pattern(dragDestinationImageName).similar(0.80))
                            dragDrop(dragSourceImageName, drop_point)
                    elif exists(Pattern(dragSourceImageName).similar(0.80)):
                            raise AssertionError("Destination Problem")
                    elif exists(Pattern(dragDestinationImageName).similar(0.80)):
                            raise AssertionError("Source Problem")
                    else:
                            raise AssertionError("Either drag source or drop destination images showing some problems..")
                elif len(args) == 4:
                        offset_x = int(args[2])
                        offset_y = int(args[3])
                        if exists(Pattern(dragSourceImageName).similar(0.80)) and exists(Pattern(dragDestinationImageName).similar(0.80)):
                                corner=find(Pattern(dragSourceImageName).targetOffset(0,0))
                                drop_point = find(Pattern(dragDestinationImageName).targetOffset(offset_x,offset_y))
                                dragDrop(corner, drop_point)                         
                else:
                        ScreenShot=capture_CS_screenshot()
                        raise AssertionError("Check number of arguments")

        def switch_to_cue(self, *args):
                #***This Keyword switches focus to Escenic Content Studio***#
                #Vision.setParameter("MinTargetSize", 6)
                
                ScreenHighlighter.closeAll()
		if args[0]=='firefox':
			eceAppName='/Applications/Firefox.app'
                elif args[0]=='GoogleChrome':
			eceAppName='/Applications/Google Chrome.app'
                switchApp(eceAppName)


	def close_existing_browser_window(self, *args):
		if args[0]=='firefox':
                        closeApp('/Applications/Firefox.app')
                elif args[0]=='GoogleChrome':
                        closeApp('/Applications/Google Chrome.app')
  
if __name__ == '__main__':  
    SRL = ContentStudio()  
    RobotRemoteServer(SRL, *sys.argv[1:])
