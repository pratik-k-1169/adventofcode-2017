def distribute(p,number,index):
    p[index]=0
    for i in range(0,number):
        try:
            index = index + 1
            p[index] = p[index] + 1
        except IndexError:
            index = 0
            p[index] = p[index] + 1
            continue

    return p


if __name__=='__main__':
    # l = [0,2,7,0]
    f=[]
    append=[]
    fh = open("input","r").read().strip()
    f = fh.split("\t")
    l = [int(i) for i in f]
    steps = 0
    while(True):
        l = distribute(l,max(l),l.index(max(l)))
        copy_list = l[:]

        if copy_list in append:
            f_o = copy_list[:]
            break
        elif copy_list not in append:
            append.append(copy_list)
            continue

    print len(append) - append.index(f_o)
