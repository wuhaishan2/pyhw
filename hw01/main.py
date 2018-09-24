for i in range(1,10):
     for k in range(1,10-i):
         print(end="       ")
     for j in range(1,i+1):
         product=i*j
         print("%d*%d=%2d" % (i,j,product),end=" ")
     print ()
