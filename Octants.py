def octOne(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = x1-x0
    d = 2A+B
    while x <= x1:
        plot(x,y)
        if d>0:
            y++
            d+=2B
        x++
        d+=2A

#
def octTwo(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = x1-x0
    d = A+2B
    while y <= y1:
        plot(x,y)
        if d>0:
            x++
            d+=2A
        y++
        d+=2B

def octThree(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = x1-x0
    d = 2A+B
    while x <= x1:
        plot(x,y)
        if d>0:
            y++
            d+=2B
        x++
        d+=2A

def octFour(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = x1-x0
    d = 2A+B
    while x <= x1:
        plot(x,y)
        if d>0:
            y++
            d+=2B
        x++
        d+=2A

def octFive(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = x1-x0
    d = 2A+B
    while x <= x1:
        plot(x,y)
        if d>0:
            y++
            d+=2B
        x++
        d+=2A

def octSix(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = x1-x0
    d = 2A+B
    while x <= x1:
        plot(x,y)
        if d>0:
            y++
            d+=2B
        x++
        d+=2A

def octSeven(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = x1-x0
    d = 2A+B
    while x <= x1:
        plot(x,y)
        if d>0:
            y++
            d+=2B
        x++
        d+=2A

#
def octEight(x0, y0, x1, y1):
    x = x0
    y = y0
    
    A = y1-y0
    B = x1-x0
    d = 2A+B
    while x <= x1:
        plot(x,y)
        if d<0:
            y--
            d-=2B
        x++
        d+=2A
