temp=0
temp1=0
for i in range(1,11):
	if(i%2==0):
		if(temp<i):
			temp=i
	else:
		if(temp1<i):
			temp1=i


print(temp1)
print(temp)
