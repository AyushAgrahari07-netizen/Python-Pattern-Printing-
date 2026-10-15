Expected output :

for an example n = 5 :- 

       *
      * *
     * * * 
    * * * * 
   * * * * * 

Python solution :

n = int(input("enter number of rows or coloum :")

for i in range (n)：
   for j in range(n-i):
     print(" ",end="")
   for j in range (2*i -1)：
     print("*",end =〃〃)
   print()