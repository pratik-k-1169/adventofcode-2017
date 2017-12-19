if __name__=='__main__':
    s = ""

    codes = s.split("\n")
    valid =0
    for code in codes:
        temp_dict = {}
        words = code.split(" ")
        for word in words:
            temp_dict[word]=temp_dict.get(word,0) + 1
        if len(temp_dict.keys()) == sum(temp_dict.values()):
            valid = valid +1

    print valid
