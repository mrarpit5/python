s1=str(input("Enter Name:- "))
ln=len(s1)
#print(ln)
if(ln<3):
	print("no changed required")
else:
	re=s1.endswith("ing")
	if(re==True):
		print(s1+"ly")
	elif(re==False):
		print(s1+"ing")
