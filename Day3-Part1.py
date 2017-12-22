import math

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

if __name__=='__main__':
    number = 368078
    points=[]
    (x,y) = ('a','b')
    points.append((x,y))
    (x,y) = (0,0)
    points.append((x,y))
    n = get_dimension(number)
    for i in range(3,int(n)+1,2):
        while(len(points) <= i**2):
            if(x < int(i/2) and y < int(i/2)):
                while(x < int(i/2)):
                    # print "Go Right"
                    (x,y)=go_right(x,y)
                    points.append((x,y))

            elif(x == int(i/2) and y < int(i/2)):
                while(y < int(i/2)):
                    # print "Go Up"
                    (x,y)=go_up(x,y)
                    points.append((x,y))

            elif(x == int(i/2) and y == int(i/2)):
                while(x > ((-1)*(int(i/2)))):
                    # print "Go left"
                    (x,y)=go_left(x,y)
                    points.append((x,y))

            elif(x == (-1*int(i/2)) and y == int(i/2)):
                while(y > ((-1)*(int(i/2)))):
                    # print "Go Down"
                    (x,y)=go_down(x,y)
                    points.append((x,y))

    # for point in points:
    #     print point,'---->',points.index(point)
    distance = abs(points[number][0]) + abs(points[number][1])
    print distance
