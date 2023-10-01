from graphics import *
from Button import *
from Piece import*
from Board import*
import time
import math

def main():
    win = GraphWin("Othello", 1000, 600)

    ws=0
    bs=0

    b= Board(win)
    b.default(win)

    A=Text(Point(650,220),"It has already been taken")
    A.setSize(24)
    A.draw(win)
    A.undraw()
    
    quitB = Button(win, "red", "Quit", Point(920,200), 40)
    skip = Button(win, "grey", "Skip", Point(920,300), 40)

    skipt = Text(Point(800,380),"Please use skip when one of the palyers\n cannot place any pieces")
    skipt.setSize(20)
    skipt.draw(win)

    WPiece=Circle(Point(600,100), 23)
    WPiece.color="white"
    WPiece.setFill("white")
    BPiece=Circle(Point(650,100), 23)
    BPiece.color="black"
    BPiece.setFill("black")

    WPiece.draw(win)
    BPiece.draw(win)

    t=1
    turn=Text(Point(600,300),"Black's Turn")
    
    turn.setSize(24)
    turn.draw(win)

    B=Text(Point(650,330),"You cannot place it here!")
    B.setSize(24)
    B.setTextColor('red')

    WScore=Text(Point(600,140),str(b.WhScore()))
    BScore=Text(Point(650,140),str(b.BlScore()))
    WScore.setSize(24)
    BScore.setSize(24)
    WScore.draw(win)
    BScore.draw(win)

    while True:
        m = win.getMouse()
        if quitB.isClicked(m):
            win.close()
            break
        
        if skip.isClicked(m):
            t=t+1
            b.skip()
            if t <17:
                Move=b.MinFlip(win)
            else:
                Move=b.MaxFlip(win)
            time.sleep(0.3)
            b.play(Move[0],Move[1],win,t)
            b.Check(Move[0],Move[1],win)
        
        for i in range(8):
            for j in range(8):
                if b.cells[i][j].isClicked(m):
                    #check if the spot is empty or not
                    if b.bList[i][j]==-1:
                        #it stops the move being made before it is placed
                        if b.iflegal(i,j,win,t)>0:
                            #if the move is legal, undraw the warnings that are made.
                            #undraw the count, so it can get recalculated.
                            WScore.undraw()
                            BScore.undraw()
                            A.undraw()
                            B.undraw()
                            #simply play and check how many pieces need to get flipped
                            b.play(i,j,win,1)
                            b.Check(i,j,win)
                            #recalculating the total pieces (points) owned by both players
                            WScore=Text(Point(600,140),str(b.WhScore()))
                            BScore=Text(Point(650,140),str(b.BlScore()))
                            WScore.setSize(24)
                            BScore.setSize(24)
                            WScore.draw(win)
                            BScore.draw(win)
                        else:
                            t=t-1
                            B.undraw()
                            B.draw(win)
                            continue
                    else:
                        A.undraw()
                        A.draw(win)
                        t=t-1
                        continue
                    if t <17:
                        t=t+1
                        Move=b.MinFlip(win)
                        if Move[0]==-1:
                            t=t+1
                            b.skip()
                        else:
                            time.sleep(0.3)
                            b.play(Move[0],Move[1],win,t)
                            b.Check(Move[0],Move[1],win)   
                    else:
                        t=t+1
                        Move=b.MaxFlip(win)
                        if Move[0]==-1:
                            t=t+1
                            b.skip()
                        else:
                            time.sleep(0.3)
                            b.play(Move[0],Move[1],win,t)
                            b.Check(Move[0],Move[1],win)

                    WScore.undraw()
                    BScore.undraw()
                    WScore=Text(Point(600,140),str(b.WhScore()))
                    BScore=Text(Point(650,140),str(b.BlScore()))
                    WScore.setSize(24)
                    BScore.setSize(24)
                    WScore.draw(win)
                    BScore.draw(win)
                    
        if t%2==0:
            turn.undraw()
            turn=Text(Point(600,300),"Black's Turn")
            turn.setSize(24)
            turn.draw(win)
            t=t+1
        elif t%2==1:
            turn.undraw()
            turn=Text(Point(600,300),"White's Turn")
            turn.setSize(24)
            turn.draw(win)
            t=t+1   
        
if __name__ == "__main__":
    main()
