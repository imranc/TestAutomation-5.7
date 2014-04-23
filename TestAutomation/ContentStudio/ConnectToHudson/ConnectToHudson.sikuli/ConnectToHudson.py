from sikuli.Sikuli import *
wait("HudsonConnectWarning.png", 120)
if exists("HudsonConnectWarning.png"):
    click("Run.png")
elif exists("HudsonRemotingLauncher.png"):
    click("CheckBox.png")
    click("Run.png")
    
    
    
    
