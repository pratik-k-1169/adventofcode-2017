if __name__=='__main__':
    l = []
    fh = open("input","r")
    for num in fh:
        l.append(int(num.strip()))
    steps = 0
    i = 0
    while(True):
        try:
            jumps = l[i]
            if jumps >= 3:
                l[i] = l[i] - 1
            else:
                l[i] = l[i] + 1
            i = i + jumps
            steps = steps + 1
        except IndexError:
            break
    # print l
    print steps
