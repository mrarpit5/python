s1=str(input("Enter Name:- "))
ln=len(s1)
print(ln)
if(ln<2):
	print("error")
else:
	s2=s1[0:2]
	s3=s1[-2:]
	print(s2+s3)
