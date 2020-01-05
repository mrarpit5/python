l=["a","b","c","d","e","f"]
print(l)
print(l[0])
print(l[-1])
print(l[2:5])
print(l[:4])
print(l[2:])
print(l[-4:-1])
for x in l:
    print(x)
if "a" in l:
    print("yes")
else:
    print("no")
print(len(l))
l.append("g")
print(l)
l.insert(0,"abc")
print(l)
l.remove("abc")
print(l)
l.pop()
print(l)
