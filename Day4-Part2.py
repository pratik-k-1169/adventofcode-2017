if __name__=='__main__':
    s = ""
    codes = s.split("\n")
    valid = len(codes)
    for code in codes:
        print code
        temp_dict = {}
        words = code.split(" ")
        for word in words:
            temp_dict[''.join(sorted(word))] = temp_dict.get(''.join(sorted(word)),0) + 1
        for v in temp_dict.values():
            if v > 1 :
                valid = valid - 1
                break
    print valid
