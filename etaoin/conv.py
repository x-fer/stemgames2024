import string, random
s = string.ascii_lowercase
sl = list(s)
random.shuffle(sl)
s1 = "".join(sl)
random.shuffle(sl)
s2 = "".join(sl)

tbl = str.maketrans(s1, s2)

with open("original.txt") as f:
    orig = f.read()
print(orig)

tr = orig.translate(tbl)
print(tr)

with open("message.txt", "w") as f:
    f.write(tr)
