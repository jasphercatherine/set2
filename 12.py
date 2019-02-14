n=int(input())
q=n
temp=0
while q!=0:
	temp=temp*10+q%10
	q=q//10
if n==temp:
	print("yes")
else:
	print("no")
