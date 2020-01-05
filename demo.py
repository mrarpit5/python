l=["A","b"]
print(l)
print(l[1])
l[1]="abc"
print(l)
for c in l:
    print(c)
if "abc" in l:
    print("yes")
print(len(l))
l.append("apppend")
l.remove("apppend")
print(l)
listcopy=list(l)
print(listcopy)
l.sort()
print(l)
l.reverse()
print(l)
