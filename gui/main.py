import cPickle
import webbrowser
from feed import Feed
from Tkinter import *

_pickle_jar = "comics"

class App(Frame):

    #leave for examples of widgets
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",

        self.hi_there.pack({"side": "left"})

        self.comic = Text(self)
        self.comic.insert(INSERT, "Hello there, Dustin")

        self.comic.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def read(self):
        with open(_pickle_jar, 'r') as f:
            comics = cPickle.load(f)
        return comics

    def write(self, comic_link):
        comics = read()
        if comic_link not in comics:
            comics[comic_link] = Feed(comic_link)
            f = open(_pickle_jar, 'w')
            cPickle.dump(comics, f)
            f.close()

    def open_link(self, event, link):
        webbrowser.open_new_tab(link)

def main():
    top = Tkinter.Tk()
    top.title("Rss Comic Feed")
    #add a button for adding feeds
    #add an entry for inputing feeds
    #maybe add a listbox for selcting which comics to display and how many entries
    #maybe add a scroll bar
    #maybe add text fields for each comic
    #add a new frame for each comic feed

    top.mainloop()

root = Tk()
app = App(master = root)
app2 = App(master = root)
app.mainloop()
app2.mainloop()
root.destroy()

    
        
