c,d =map(int,input().split())
for y in range(c + 1,d):
   if y > 1:
       for i in range(2,y):
           if (y% i) == 0:
               break
       else:
            print(y,end=" ")
