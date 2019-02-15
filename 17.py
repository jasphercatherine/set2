n=int(input())
s=0
t=n
while t>0:
	x=t%10
	s+=x**3
	t=t//10
if (n==s):
	print("yes")
else:
	print("no")
