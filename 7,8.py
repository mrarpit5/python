import string
a=input ("Enter String: ")
kk=[]
d=0
cc=[]
s=string.punctuation
for i in range(0,len(a)):
    kk.append(a[i])
while(True):
    if(d<=len(kk)):
        for i in range(0,len(s)):
            if s[i] in kk:
                cc.append(s[i])
                kk.remove(s[i])
    if(d>len(kk)):
        break
    d=d+1
for i in range(0,len(cc)):
    print("Element ",cc[i]," found ",cc.count(cc[i])," times.")
