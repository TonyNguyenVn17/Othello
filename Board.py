from graphics import *
from Button import*
from Piece import*

class Board():

    def __init__(self, win):

        self.win = win

        self.cells =[]
        #board condition (-1,no piece)(0,white)(1,black)
        self.bList=[]
        self.pList=[]
        
        for i in range(8):
            columns = []
            columns1=[]
            columns2=[]
            for j in range(8):
                columns.append(Button(win, "green", "", Point(i*50 + 100, j*50 + 100), 25))
                columns1.append(-1)
                columns2.append(None)
            self.cells.append(columns)
            self.bList.append(columns1)
            self.pList.append(columns2)

        #determine black or white
        self.Turn = 0

        self.pieces = []
        

    def default(self, win):

        p0 = Piece(self.win, 3, 3, 0)
        p1 = Piece(self.win, 4, 4, 0)
        p2 = Piece(self.win, 3, 4, 0)
        p3 = Piece(self.win, 4, 3, 0)

        p2.change(win)
        p3.change(win)
        
        self.pieces = [p0,p1,p2,p3]
        
        self.bList [3][3]= p0.getCount()
        self.bList [4][4]= p1.getCount()
        self.bList [3][4]= p2.getCount()
        self.bList [4][3]= p3.getCount()

        self.pList [3][3]= p0
        self.pList [4][4]= p1
        self.pList [3][4]= p2
        self.pList [4][3]= p3


    def MinFlip(self,win):

        Minflip=1000
        r=0
        c=0
        for i in range(2,6):
            for j in range(2,6):
                if self.bList[i][j]==-1:
                    if int(self.iflegal(0,0,win,0)) != 0:
                        Minflip=int(self.iflegal(0,0,win,0))
                        r=0
                        c=0
                    elif int(self.iflegal(0,7,win,0)) != 0:
                        Minflip=int(self.iflegal(0,7,win,0))
                        r=0
                        c=7
                    elif int(self.iflegal(7,7,win,0)) != 0:
                        Minflip=int(self.iflegal(7,7,win,0))
                        r=7
                        c=7
                    elif int(self.iflegal(7,0,win,0)) != 0:
                        Minflip=int(self.iflegal(7,0,win,0))
                        r=7
                        c=0
                    elif int(self.iflegal(i,j,win,0))<Minflip and int(self.iflegal(i,j,win,0)) != 0:
                        Minflip=int(self.iflegal(i,j,win,0))
                        r=i
                        c=j
        if Minflip==1000:
            for i in range(8):
                for j in range(8):
                    if (i==1 and j ==1)or(i==6 and j ==6)or(i==1 and j ==6)or(i==6 and j ==1):
                        continue
                    else:
                        if self.bList[i][j]==-1:
                            #corner high prority 
                            if (i==0 and j==0)or(i==0 and j==7)or(i==7 and j==0)or(i==7 and j==7):
                                if int(self.iflegal(i,j,win,0)) != 0:
                                    Minflip=int(self.iflegal(i,j,win,0))
                                    r=i
                                    c=j
                            #edge from 2-5 second priority
                            elif (i==0 and (j==2 or j==3 or j==4 or j==5))or((i==2 or i==3 or i==4 or i==5) and j==0)or(i==7 and (j==2 or j==3 or j==4 or j==5))or(j==7 and (i==2 or i==3 or i==4 or i==5)):
                                if int(self.iflegal(i,j,win,0)) != 0:
                                    Minflip=int(self.iflegal(i,j,win,0))
                                    r=i
                                    c=j
                            elif (int(self.iflegal(i,j,win,0))<Minflip)and(int(self.iflegal(i,j,win,0)) != 0):
                                Minflip=int(self.iflegal(i,j,win,0))
                                r=i
                                c=j
            if Minflip ==1000:
                if int(self.iflegal(1,1,win,0)) != 0 and self.bList[1][1]==-1:
                    Minflip=int(self.iflegal(1,1,win,0))
                    r=1
                    c=1
                if int(self.iflegal(1,6,win,0)) != 0 and self.bList[1][6]==-1:
                    Minflip=int(self.iflegal(1,6,win,0))
                    r=1
                    c=6
                if int(self.iflegal(6,1,win,0)) != 0 and self.bList[6][1]==-1:
                    Minflip=int(self.iflegal(6,1,win,0))
                    r=6
                    c=1
                if int(self.iflegal(6,6,win,0)) != 0 and self.bList[6][6]==-1:
                    Minflip=int(self.iflegal(6,6,win,0))
                    r=6
                    c=6
                
        if Minflip==1000:
            Move=[-1,-1]
        Move=[r,c]
        return Move

    def MaxFlip(self,win):

        Maxflip=0
        r=0
        c=0
        for i in range(2,6):
            for j in range(2,6):
                if self.bList[i][j]==-1:
                    if int(self.iflegal(0,0,win,0)) != 0:
                        Maxflip=int(self.iflegal(0,0,win,0))
                        r=0
                        c=0
                    elif int(self.iflegal(0,7,win,0)) != 0:
                        Maxflip=int(self.iflegal(0,7,win,0))
                        r=0
                        c=7
                    elif int(self.iflegal(7,7,win,0)) != 0:
                        Maxflip=int(self.iflegal(7,7,win,0))
                        r=7
                        c=7
                    elif int(self.iflegal(7,0,win,0)) != 0:
                        Maxflip=int(self.iflegal(7,0,win,0))
                        r=7
                        c=0
                    elif (int(self.iflegal(i,j,win,0))>Maxflip) and (int(self.iflegal(i,j,win,0))!= 0):
                        Maxflip=int(self.iflegal(i,j,win,0))
                        r=i
                        c=j
                    
        for i in range(8):
            for j in range(8):
                if (i==1 and j==1)or(i==6 and j==6)or(i==1 and j==6)or(i==6 and j==1)or(i==1 and j==0)or(i==0 and j==1)or(i==0 and j==6)or(i==6 and j==0)or(i==1 and j==7)or(i==7 and j==1)or(i==7 and j==6)or(i==6 and j==7):
                    continue
                else:
                    if self.bList[i][j]==-1:
                        #corner high prority 
                        if (i==0 and j==0)or(i==0 and j==7)or(i==7 and j==0)or(i==7 and j==7):
                            if int(self.iflegal(i,j,win,0)) != 0:
                                Maxflip=int(self.iflegal(i,j,win,0))
                                r=i
                                c=j
                        #edge from 2-5 second priority
                        elif (i==0 and (j==2 or j==3 or j==4 or j==5)) or ((i==2 or i==3 or i==4 or i==5) and j==0) or (i==7 and (j==2 or j==3 or j==4 or j==5)) or (j==7 and (i==2 or i==3 or i==4 or i==5)):
                            if int(self.iflegal(i,j,win,0)) != 0:
                                Maxflip=int(self.iflegal(i,j,win,0))
                                r=i
                                c=j
                        elif int(self.iflegal(i,j,win,0))>Maxflip and int(self.iflegal(i,j,win,0)) != 0:
                            Maxflip=int(self.iflegal(i,j,win,0))
                            r=i
                            c=j
        if Maxflip==0:
            #the edge right next to the corner we wanna avoid as possible
            if int(self.iflegal(1,0,win,0)) != 0 and self.bList[1][0]==-1:
                Maxflip=int(self.iflegal(1,0,win,0))
                r=1
                c=0
            elif int(self.iflegal(0,1,win,0)) != 0 and self.bList[0][1]==-1:
                Maxflip=int(self.iflegal(0,1,win,0))
                r=0
                c=1
            elif int(self.iflegal(6,0,win,0)) != 0 and self.bList[6][0]==-1:
                Maxflip=int(self.iflegal(6,0,win,0))
                r=6
                c=0
            elif int(self.iflegal(0,6,win,0)) != 0 and self.bList[0][6]==-1:
                Maxflip=int(self.iflegal(0,6,win,0))
                r=0
                c=6
            elif int(self.iflegal(6,7,win,0)) != 0 and self.bList[6][7]==-1:
                Maxflip=int(self.iflegal(6,7,win,0)) 
                r=6
                c=7
            elif int(self.iflegal(7,6,win,0)) != 0 and self.bList[7][6]==-1:
                Maxflip=int(self.iflegal(7,6,win,0))
                r=7
                c=6
            elif int(self.iflegal(1,7,win,0)) != 0 and self.bList[1][7]==-1:
                Maxflip=int(self.iflegal(1,7,win,0))
                r=1
                c=7
            elif int(self.iflegal(7,1,win,0)) != 0 and self.bList[7][1]==-1:
                Maxflip=int(self.iflegal(7,1,win,0))
                r=7
                c=1

            #diagonal spot right next to the corner is the last choice we wanna choose
            elif int(self.iflegal(1,1,win,0)) != 0 and self.bList[1][1]==-1:
                Maxflip=int(self.iflegal(1,1,win,0))
                r=1
                c=1
            elif int(self.iflegal(1,6,win,0)) != 0 and self.bList[1][6]==-1:
                Maxflip=int(self.iflegal(1,6,win,0))
                r=1
                c=6
            elif int(self.iflegal(6,1,win,0)) != 0 and self.bList[6][1]==-1:
                Maxflip=int(self.iflegal(6,1,win,0))
                r=6
                c=1
            elif int(self.iflegal(6,6,win,0)) != 0 and self.bList[6][6]==-1:
                Maxflip=int(self.iflegal(6,6,win,0))
                r=6
                c=6
        if Maxflip==0:
            Move=[-1,-1]
        Move=[r,c]
        return Move 

    def WhScore(self):
        x=0
        for i in range(8):
            for j in range(8):
                if self.bList[i][j] == 0:
                    x=x+1
        return x
    
    def BlScore(self):
        x=0
        for i in range(8):
            for j in range(8):
                if self.bList[i][j] == 1:
                    x=x+1
        return x
    
    def skip(self):
        self.Turn +=1

    def play(self, r, c, win,t):
        valid = True
        
        for piece in self.pieces:
            
            if piece.getPos() == [r, c]:
                valid = False
        
        if valid and self.iflegal(r,c,win,t)>0:
            
            p = Piece(self.win, r, c, 0)
            
            if self.Turn%2 == 0:
                p.change(win)
                
            self.pieces.append(p)
            self.bList[r][c]=p.getCount()
            self.pList[r][c]=p
            self.Turn += 1
        
    def ifvalid(self,r,c):
        
        if r >= 0 and c >= 0 and r <= 7 and c <= 7:
            return True
        else:
            return False 


    def Check(self, r, c, win):
        x=r
        y=c
        #CHECK IF IT GETS FLIPPED =2, IF NOT=0
        PosL=[]
        L=[]
        
        for i in range (8):
            L=[]
            for j in range(8):
                L.append(None)
            PosL.append(L)

        #check top left     
        for i in range (8):
            for j in range(8):
                PosL[i][j]=0  
        
        while x > 0 and y > 0 and x <= 7 and y <= 7 and self.bList[x-1][y-1]!=self.bList[r][c] and self.bList[x-1][y-1]!=-1:
            x=x-1
            y=y-1
            PosL[x][y]=1
            
 
        x=x-1
        y=y-1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
                        
        #check top mid
        x=r
        y=c 
        
        while x >= 0 and y > 0 and x <= 7 and y <= 7 and self.bList[x][y-1]!=self.bList[r][c] and self.bList[x][y-1]!=-1:
            x=x
            y=y-1
            PosL[x][y]=1
            
 
        x=x
        y=y-1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
                        
        #check top right
        x=r
        y=c 
        
        while x >= 0 and y > 0 and x < 7 and y <= 7 and self.bList[x+1][y-1]!=self.bList[r][c] and self.bList[x+1][y-1]!=-1:
            x=x+1
            y=y-1
            PosL[x][y]=1
        x=x+1
        y=y-1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0

 
        #check mid left
        x=r
        y=c 
        
        while x > 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x-1][y]!=self.bList[r][c] and self.bList[x-1][y]!=-1:
            x=x-1
            y=y
            PosL[x][y]=1
        x=x-1
        y=y
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check bottom left
        x=r
        y=c 

        while x > 0 and y >= 0 and x <= 7 and y < 7 and self.bList[x-1][y+1]!=self.bList[r][c] and self.bList[x-1][y+1]!=-1:
            x=x-1
            y=y+1
            PosL[x][y]=1
 
        x=x-1
        y=y+1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check bottom mid
        x=r
        y=c

        while x >= 0 and y >= 0 and x <= 7 and y < 7 and self.bList[x][y+1]!=self.bList[r][c] and self.bList[x][y+1]!=-1:
            x=x
            y=y+1
            PosL[x][y]=1
 
        x=x
        y=y+1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check bottom right
        x=r
        y=c
 
        
        while x >= 0 and y >= 0 and x < 7 and y < 7 and self.bList[x+1][y+1]!=self.bList[r][c] and self.bList[x+1][y+1]!=-1:
            x=x+1
            y=y+1
            PosL[x][y]=1
 
        x=x+1
        y=y+1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check mid right
        x=r
        y=c
 
        
        while x >= 0 and y >= 0 and x < 7 and y <= 7 and self.bList[x+1][y]!=self.bList[r][c] and self.bList[x+1][y]!=-1:
            x=x+1
            y=y
            PosL[x][y]=1
 
        x=x+1
        y=y
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0        
        flip=0
       
        for i in range(8):
            for j in range(8):
                if PosL[i][j]==2:
                    flip=flip+1
        if flip>0:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==2:
                        self.bList[i][j]=self.bList[r][c]
                        self.pList[i][j].change(win)
        else:
            return 0
        
                   
    def iflegal(self, r, c, win,t):
        temp=self.bList[r][c]
        x=r
        y=c
        #CHECK IF IT GETS FLIPPED =2, IF NOT=0
        PosL=[]
        L=[]

        if t%2==0:
            self.bList[r][c]= 0
        else:
            self.bList[r][c]= 1
        
        for i in range (8):
            L=[]
            for j in range(8):
                L.append(None)
            PosL.append(L)

        #check top left     
        for i in range (8):
            for j in range(8):
                PosL[i][j]=0  
        
        while x > 0 and y > 0 and x <= 7 and y <= 7 and self.bList[x-1][y-1]!=self.bList[r][c] and self.bList[x-1][y-1]!=-1:
            x=x-1
            y=y-1
            PosL[x][y]=1
            
 
        x=x-1
        y=y-1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
                        
        #check top mid
        x=r
        y=c 
        
        while x >= 0 and y > 0 and x <= 7 and y <= 7 and self.bList[x][y-1]!=self.bList[r][c] and self.bList[x][y-1]!=-1:
            x=x
            y=y-1
            PosL[x][y]=1
            
 
        x=x
        y=y-1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
                        
        #check top right
        x=r
        y=c 
        
        while x >= 0 and y > 0 and x < 7 and y <= 7 and self.bList[x+1][y-1]!=self.bList[r][c] and self.bList[x+1][y-1]!=-1:
            x=x+1
            y=y-1
            PosL[x][y]=1
        x=x+1
        y=y-1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0

 
        #check mid left
        x=r
        y=c 
        
        while x > 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x-1][y]!=self.bList[r][c] and self.bList[x-1][y]!=-1:
            x=x-1
            y=y
            PosL[x][y]=1
        x=x-1
        y=y
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check bottom left
        x=r
        y=c 

        while x > 0 and y >= 0 and x <= 7 and y < 7 and self.bList[x-1][y+1]!=self.bList[r][c] and self.bList[x-1][y+1]!=-1:
            x=x-1
            y=y+1
            PosL[x][y]=1
 
        x=x-1
        y=y+1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check bottom mid
        x=r
        y=c

        while x >= 0 and y >= 0 and x <= 7 and y < 7 and self.bList[x][y+1]!=self.bList[r][c] and self.bList[x][y+1]!=-1:
            x=x
            y=y+1
            PosL[x][y]=1
 
        x=x
        y=y+1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check bottom right
        x=r
        y=c
 
        
        while x >= 0 and y >= 0 and x < 7 and y < 7 and self.bList[x+1][y+1]!=self.bList[r][c] and self.bList[x+1][y+1]!=-1:
            x=x+1
            y=y+1
            PosL[x][y]=1
 
        x=x+1
        y=y+1
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        #check mid right
        x=r
        y=c

        
        
        while x >= 0 and y >= 0 and x < 7 and y <= 7 and self.bList[x+1][y]!=self.bList[r][c] and self.bList[x+1][y]!=-1:
            x=x+1
            y=y
            PosL[x][y]=1
 
        x=x+1
        y=y
                       
        if x >= 0 and y >= 0 and x <= 7 and y <= 7 and self.bList[x][y] == self.bList[r][c]:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                       PosL[i][j]=2
                        #self.bList[i][j]=self.bList[r][c]
                        #self.pList[i][j].change(win)
        else:
            for i in range(8):
                for j in range(8):
                    if PosL[i][j]==1:
                        PosL[i][j]=0
        
        flip=0
        
       
        for i in range(8):
            for j in range(8):
                if PosL[i][j]==2:
                    flip=flip+1
        
        if flip<=0:  
            self.bList[r][c]=temp
            return flip
        else:
            self.bList[r][c]=temp
            return flip



        
      
                
            
                
            











        
        
            
            
    
