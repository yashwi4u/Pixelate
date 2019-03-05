# a = [[0 for x in range(9)] for y in range(9)]
# a[0][0] = [ 'square','yellow',0,0 ]
# a[0][1] = [ 'circle','yellow',0,1 ]
# a[0][2] = [ 'square','red',0,2 ]
# a[0][3] = [ 'triangle','red',0,3 ]
# a[0][4] = [ 'arrow',0,0,4 ]
# a[0][5] = [ 'circle','red',0,5 ]
# a[0][6] = [ 'triangle','yellow',0,6 ]
# a[0][7] = [ 'square','yellow',0,7 ]
# a[0][8] = [ 'triangle','red',0,8 ]
#  #
# a[1][0] = [ 'triangle','yellow',1,0 ]
# a[1][1] = [ 0,0,1,1 ]
# a[1][2] = [ 0,0,1,2 ]
# a[1][3] = [ 0,0,1,3 ]
# a[1][4] = [ 'triangle','yellow',1,4 ]
# a[1][5] = [ 0,0,1,5 ]
# a[1][6] = [ 0,0,1,6 ]
# a[1][7] = [ 0,0,1,7 ]
# a[1][8] = [ 'square','red',1,8 ]
# a[2][0] = [ 'circle','red',2,0 ]
# a[2][1] = [ 0,0,2,1 ]
# a[2][2] = [ 'square','red',2,2 ]
# a[2][3] = [ 'triangle','yellow',2,3 ]
# a[2][4] = [ 'square','yellow',2,4 ]
# a[2][5] = [ 'circle','yellow',2,5 ]
# a[2][6] = [ 'triangle','red',2,6 ]
# a[2][7] = [ 0,0,2,7 ]
# a[2][8] = [ 'circle','yellow',2,8 ]
#
# a[3][0] = [ 'square','red',3,0 ]
# a[3][1] = [ 0,0,3,1 ]
# a[3][2] = [ 'circle','yellow',3,2 ]
# a[3][3] = [ 0,0,3,3 ]
# a[3][4] = [ 'circle','red',3,4 ]
# a[3][5] = [ 0,0,3,5 ]
# a[3][6] = [ 'square','red',3,6 ]
# a[3][7] = [ 0,0,3,7 ]
# a[3][8] = [ 'triangle','yellow',3,8 ]
# # #
# a[4][0] = [ 'arrow',0,4,0 ]
# a[4][1] = [ 'circle','red',4,1 ]
# a[4][2] = [ 'triangle','red',4,2 ]
# a[4][3] = [ 0,0,4,3 ]
# a[4][4] = [ 1,1,4,4 ]
# a[4][5] = [ 'triangle','yellow',4,5 ]
# a[4][6] = [ 'circle','red',4,6 ]
# a[4][7] = [ 'square','red',4,7 ]
# a[4][8] = [ 'arrow',0,4,8 ]
# a[5][0] = [ 'triangle','red',5,0 ]
# a[5][1] = [ 0,0,5,1 ]
# a[5][2] = [ 'square','yellow',5,2 ]
# a[5][3] = [ 0,0,5,3 ]
# a[5][4] = [ 0,0,5,4 ]
# a[5][5] = [ 0,0,5,5 ]
# a[5][6] = [ 'triangle','red',5,6 ]
# a[5][7] = [ 0,0,5,7 ]
# a[5][8] = [ 'circle','red',5,8 ]
# # #
# a[6][0] = [ 'circle','yellow',6,0 ]
# a[6][1] = [ 0,0,6,1 ]
# a[6][2] = [ 'circle','red',6,2 ]
# a[6][3] = [ 'triangle','yellow',6,3 ]
# a[6][4] = [ 'square','red',6,4 ]
# a[6][5] = [ 'circle','yellow',6,5 ]
# a[6][6] = [ 'square','yellow',6,6 ]
# a[6][7] = [ 0,0,6,7 ]
# a[6][8] = [ 'triangle','red',6,8 ]
# # #
# a[7][0] = [ 'square','red',7,0 ]
# a[7][1] = [ 0,0,7,1 ]
# a[7][2] = [ 0,0,7,2 ]
# a[7][3] = [ 0,0,7,3 ]
# a[7][4] = [ 'triangle','red',7,4 ]
# a[7][5] = [ 0,0,7,5 ]
# a[7][6] = [ 0,0,7,6 ]
# a[7][7] = [ 0,0,7,7 ]
# a[7][8] = [ 'square','yellow',7,8 ]
# # #
# a[8][0] = [ 'triangle','yellow',8,0 ]
# a[8][1] = [ 'circle','red',8,1 ]
# a[8][2] = [ 'square','yellow',8,2 ]
# a[8][3] = [ 'triangle','red',8,3 ]
# a[8][4] = [ 'arrow',0,8,4 ]
# a[8][5] = [ 'circle','red',8,5 ]
# a[8][6] = [ 'square','red',8,6 ]
# a[8][7] = [ 'triangle','yellow',8,7 ]
# a[8][8] = [ 'circle','yellow',8,8 ]
def dest(a,z,shape,color):
    (x,y)=z
    i=0
    f=0
    if ((x==4) & (y==0) & (f==0)):
        x=x-1
        f=f+1
    if ((x==0) & (y==4) & (f==0)):
        y=y+1
        f=f+1
    if ((x==8) & (y==4) & (f==0)):
        y=y-1
        f=f+1
    if ((x==4) & (y==8) & (f==0)):
        x=x+1
        f=f+1
    def short_path(x,y,shape,color,i,f):
        def find(x,y,shape,color,i,f):
            #print (x,y)
            z=(x,y)
            # x=z[0]
            # y=z[1]
            m,n=check_quadrant(z,i)
            #print (m,n)
            if ((x<9) & (y<9) & (x>=0) & (y>=0)):
                if (a[x][y][0:4]==[0,0,x,y]):
                    #print (a[x][y][0:4])
                    b=[x,y,1000]
                    return b
                if ((a[x][y][0:4]==[shape,color,x,y]) & ((i!=0) | (f==1)) ):
                    b=[x,y,i]
                    f=f+1
                    return b
                else:
                    i=i+1
                    #if ((x<8) & (y<8) & (x>=0) & (y>=0)):
                    c=find(x+m,y,shape,color,i,f)
                    d=find(x,y+n,shape,color,i,f)
                    #    e=find(x,y-1,shape,color,i)
                        #print (d)
                    if (c[2]<d[2]):
                        return (c)
                    else:
                        return (d)
            else:
                return ([x,y,1000])
        s=find(x,y,shape,color,i,f)
        return s
    def check_quadrant(z,i):
        x=z[0]
        y=z[1]
        print (x,y)
        if ((x>=0) & (x<=4) & (y>=0) & (y<4)): #quad1
            m=-1
            n=1
            return m,n
        elif ((x>=4) & (x<=9) & (y>4) & (y<=9)): #quad 3
            m=1
            n=-1
            return m,n
        elif ((x>=0) & (x<4) & (y>=4) & (y<=9)): # quad2
            m=1
            n=1
            return m,n
        elif ((x>4) & (x<=9) & (y>=0) & (y<=4)): #quad4
            print (4)
            m=-1
            n=-1
            return m,n
        else:
            return (-1,-1)

    return (short_path(x,y,shape,color,0,f))
#z=(6,4)
#print (dest(a,z,'square','red'))
