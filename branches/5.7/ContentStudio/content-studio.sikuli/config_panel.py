########################################################################
#####TEST CASE: Configure and review RSS Feed panel
########################################################################
App.focus("Escenic Content Studio")
wait(2)
##Full screent content studio with SPACE+ALT+X
type(Key.SPACE, KeyModifier.ALT)
type('x')
type("8",KeyModifier.CTRL)
if exists("new_research_panel.png"):
    click("new_research_panel.png")

type(Key.TAB + Key.TAB + Key.TAB + Key.TAB)
paste("http://feeds.bbci.co.uk/news/technology/rss.xml")
wait(5)
#paste("abc.com/rss.xml")
click("OK_button.png")

##TEST ASSERTION
type("4", KeyModifier.CTRL)
wait(10)
if exists(Pattern("read_rss_feed.png").targetOffset(-2,3)):
    print "Test failed"
elif exists(Pattern("bbc_rss_feed_read.png").targetOffset(-15,2)): 
    print "Test passed"

type("4", KeyModifier.CTRL)

#App.focus("Internet Explorer")
#wait(5)
#type(Key.F4,KEY_ALT)