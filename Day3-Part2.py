import math
points={}

def go_right(x,y):
    return (x+1,y+0)

def go_left(x,y):
    return (x-1,y+0)

def go_up(x,y):
    return (x+0,y+1)

def go_down(x,y):
    return (x+0,y-1)

def get_dimension(number):
    n = math.ceil(number**0.5)
    if (n%2 == 0):
        n = n+1
    return n

def calculate_value(x,y):
    l = [(x-1,y+1),(x-1,y),(x-1,y-1),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y),(x+1,y-1)]
    s = 0
    for p in l:
        try:
            s = s + points[p]
        except KeyError:
            continue
    return s

if __name__=='__main__':
    number = 50
    (x,y) = ('a','b')
    points[(x,y)] = 0
    (x,y) = (0,0)
    points[(x,y)] = 1
    n = get_dimension(number)
    for i in range(3,int(n)+1,2):
        while(len(points.keys()) <= i**2):
            if(x < int(i/2) and y < int(i/2)):
                while(x < int(i/2)):
                    # print "Go Right"
                    (x,y)=go_right(x,y)
                    points[(x,y)] = calculate_value(x,y)

            elif(x == int(i/2) and y < int(i/2)):
                while(y < int(i/2)):
                    # print "Go Up"
                    (x,y)=go_up(x,y)
                    points[(x,y)] = calculate_value(x,y)

            elif(x == int(i/2) and y == int(i/2)):
                while(x > ((-1)*(int(i/2)))):
                    # print "Go left"
                    (x,y)=go_left(x,y)
                    points[(x,y)] = calculate_value(x,y)

            elif(x == (-1*int(i/2)) and y == int(i/2)):
                while(y > ((-1)*(int(i/2)))):
                    # print "Go Down"
                    (x,y)=go_down(x,y)
                    points[(x,y)] = calculate_value(x,y)
    fd = {}
    for k,v in points.iteritems():
        if v > 368078:
            fd[v]=k

    for k,v in fd.iteritems():
        if k == min(fd.keys()) :
            print k,v
    # distance = abs(points[number][0]) + abs(points[number][1])
    # print distance
