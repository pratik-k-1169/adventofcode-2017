
if __name__=='__main__':
    s=""""""
    l = [int(n) for n in s]
    add = []
    orig_length = len(l)
    jumps = len(l)/2
    l = l + l[:jumps]
    for i in range(orig_length):
        if l[i] == l[i+jumps]:
            add.append(l[i])
        else:
            continue
    print sum(add)
