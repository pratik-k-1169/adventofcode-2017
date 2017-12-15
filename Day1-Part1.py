
if __name__=='__main__':
    s=""""""          # string of the numbers
    l = [int(n) for n in s]
    add = []
    for i in range(len(l)):
        try:
            if l[i] == l[i+1]:
                add.append(l[i])
        except IndexError:
            if l[i] == l[0]:
                add.append(l[i])
        else:
            continue
    print sum(add)
