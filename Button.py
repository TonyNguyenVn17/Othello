from graphics import*

class Button():

    def __init__(self, win, color, text, center, size):

        self.p1 = Point(center.x - size, center.y - size)
        self.p2 = Point(center.x + size, center.y + size)
        self.r = Rectangle(self.p1, self.p2)
        self.r.draw(win)
        self.r.setFill(color)
        self.t = Text(center, text)
        self.t.setSize(18)
        self.t.draw(win)

    def changeColor(self, newColor):
        self.r.setFill(newColor)

    def isClicked(self, p):
        minX = self.p1.x
        maxX = self.p2.x
        minY = self.p1.y
        maxY = self.p2.y

        if p.x > minX:
            if p.x < maxX:
                if p.y > minY:
                    if p.y < maxY:
                        return True
                    
        return False
    



