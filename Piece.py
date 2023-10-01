from graphics import *

class Piece():

    def __init__(self, win, r, c, Count):
        self.win = win
        self.pos = [r, c]
        self.row = r
        self.column = c
        
        self.im = Circle(Point(r*50 + 100, c*50 + 100), 23)
        self.im.draw(win)
        
        self.color = "white"
        self.im.setFill("white")
        self.Count=0


    def change(self, win):
        if self.color == "white":
            self.im.undraw()
            self.color = "black"
            self.im.setFill("black")
            self.im.draw(win)
            self.Count=1
        else:
            self.im.undraw()
            self.color = "white"
            self.im.setFill("white")
            self.im.draw(win)
            self.Count=0


    def getPos(self):
        return self.pos

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column
 
    def getColor(self):
        return self.color

    def getCount(self):
        return self.Count

    
        
