
'''
*****
*****
*****
*****
*****
'''
# t=["A","B","C","D","E"]

for i in range(5):
    for j in range(5):  
        print("*", end='')
    print()
    

print()
print("#############")
print()


'''
*
**
***
****
*****
'''

def pattern(n):
    for i in range(n):
        for j in range(i):
            print("*", end='')
        print()

pattern(6)

print()
print("#############")
print()

'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()


print()
print("#############")
print()

'''
A
BB
CCC
DDDD
EEEEE
'''
t=["A","B","C","D","E"]

for i in range(5):
    for j in range(i+1):  
        print(t[i], end='')
    print()

print()
print("#############")
print()

'''
1
22
333
4444
55555
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end='')
    print()


print()
print("#############")
print()

'''
*****
****
***
**
*
'''

def pattern(n):
    for i in range(n,1,-1):
        for j in range(i,1,-1):
            print("*", end='')
        print()

pattern(6)

print()
print("#############")
print()

'''
12345
1234
123
12
1
'''

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end='')
    print()


print()
print("#############")
print()



'''
****#****
***###***
**#####**
*#######*
#########

See this problem like split into 2
     |
****#|****
***##|#***
**###|##**
*####|###*
#####|####
     |
'''
t=0
for i in range(1,6):
    for j in range(1,5-t):   ## first set of * decreasing R to L from 5 to 1
        print("*", end='')
    for k in range(1,i+1):   ## first set of # R to L increasing from 1 to 5
        print("#", end='')   
    for l in range(1,t+1):   ## second set of # increasing L to R from 0 to 4
        print('#', end='')
    for m in range(1,5-t):   ## second set of * decreasing T to L from 5 to 1 R
        print("*", end='')     
    print()
    t+=1

print()
print("#############")
print()



'''
    *
   ***
  *****
 *******
*********
'''
t=0
for i in range(1,6):
    for j in range(1,5-t):  
        print(" ", end='')
    for k in range(1,i+1):
        print("*", end='')
    for l in range(1,t+1):
        print('*', end='')
    for m in range(1,5-t):
        print(" ", end='')
    print()
    t+=1

print()
print("#############")
print()

'''
*********
 *******
  *****
   ***
    *
'''
t=0
for i in range(1,6):
    for l in range(1,t+1):
        print(' ', end='')
    for j in range(1,6-t):  
        print("*", end='')
    for m in range(1,5-t):
        print("*", end='')
    print()
    t+=1

print()
print("#############")
print()

'''
*********
 *******
  *****
   ***
    *
'''
# t=0
for i in range(5):
    for l in range(1,i+1):
        print(' ', end='')
    for j in range(5-i):  
        print("*", end='')
    for m in range(4-i):
        print("*", end='')
    print()
    # t+=1

# First do using t and then you caan replace it using i

print()
print("#############")
print()


'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


    First divide this problem into 2 and you'll easily solve it. Then u know how to further divide it.

    *
   ***
  *****
 *******
*********
--------------
 *******
  *****
   ***
    *
'''

t=0
for i in range(1,6):
    for j in range(1,5-t):  
        print(" ", end='')
    for k in range(1,i+1):
        print("*", end='')
    for l in range(1,t+1):
        print('*', end='')
    for m in range(1,5-t):
        print(" ", end='')
    print()
    t+=1
t=0
for i in range(1,6):
    for l in range(1,t+1):
        print(' ', end='')
    for j in range(1,6-t):  
        print("*", end='')
    for m in range(1,5-t):
        print("*", end='')
    print()
    t+=1


print()
print("#############")
print()
for i in range(1, 10, 2):  # Loop for the upper half and the peak (1, 3, 5, 7, 9)
    spaces = (9 - i) // 2  # Calculate spaces before the stars
    # Print spaces
    print(" " * spaces, end="")
    # Print stars
    print("*" * i)

for i in range(7, 0, -2):  # Loop for the lower half (7, 5, 3, 1)
    spaces = (9 - i) // 2  # Calculate spaces before the stars
    # Print spaces
    print(" " * spaces, end="")
    # Print stars
    print("*" * i)


"""
Java code
int t=0;
for(int i=1; i<6; i++)
{
    for(int j=1;j<5-t; j++)
    {
        System.out.print(" ");
    }
    for(int k=1;k<=i; k++)
    {
        System.out.print("#");
    }
    for(int l=1;l<=t; l++)
    {
        System.out.print("#");
    }
    for(int m=1;m<5-t; m++)
    {
        System.out.print(" ");
    }
    t+=1;
    System.out.println();
}
"""

