def open_as_clean_list(filename):
    '''Opens a file and converts into a list.
    Ignores comments preceded with "#" and blank lines
    
    >>>open_as_clean_list("motd.txt")
    ["the first rule","is that you do not talk about fight club"]
    '''
    list = []
    with open(filename) as f:
        for line in f:
            li = line.rstrip()
            if not li.startswith("#") and li:
                list.append(li)
        return list

if __name__ == '__main__':
    import random
    
    first = open_as_clean_list("first.txt")
    second = open_as_clean_list("second.txt")
    print(random.choice(first) + ' ' + random.choice(second))
