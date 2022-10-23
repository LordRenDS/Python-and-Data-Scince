import string

zen = input()
abc = list(string.ascii_lowercase)
zen = zen.casefold()
count = 0
result = {}

for x in abc:
    for y in zen:
        if x is y:
            count += 1
    if count != 0:
        result.update({x: count})
    count = 0

print(result)
