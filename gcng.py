import random

def OpenAsCleanList(filename):
    '''Opens a file and converts into a list.
    Ignores comments preceded with "#" and blank lines
    
    >>>OpenAsCleanList("motd.txt")
    ["the first rule","is that you do not talk about fight club"]
    '''
    list = []
    with open(filename) as f:
        for line in f:
            li = line.rstrip()
            if not li.startswith("#") and li:
                list.append(li)
        return list

first = OpenAsCleanList("first.txt")
second = OpenAsCleanList("second.txt")

print(random.choice(first) + ' ' + random.choice(second))
