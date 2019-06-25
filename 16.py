r,s =map(int,input().split())
for y in range(r + 1,s):
   if y > 1:
       for i in range(2,y):
           if (y% i) == 0:
               break
       else:
            print(y,end=" ")
