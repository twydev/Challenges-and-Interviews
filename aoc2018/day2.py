scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
handle = open(full_filename, "r")

### Depending of Challenge, read file accordingly ###

str_list = handle.read().split("\n")

import collections
twos = 0
threes = 0
for box_id in str_list:
    counts_map = collections.Counter(box_id)
    values = counts_map.values()
    if 2 in values:
        twos += 1
    if 3 in values:
        threes += 1
print("Twos",twos)
print("Threes",threes)
print(twos*threes)

def match(str1, str2):
    strike = False
    index = -1
    for i in xrange(len(str1)):
        if (str1[i] != str2[i]):
            if (strike):
                return False
            else:
                strike = True
                index = i
    if (strike):
        return index
    else:
        return False

parsed = []
for word in str_list:
    for each in parsed:
        i = match(word,each)
        if (i):
            print(i)
            print(word)
            print(each)
            if (len(word)-1 != i):
                print(word[0:i] + word[i+1:])
            break
    parsed.append(word)
    