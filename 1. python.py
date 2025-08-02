#variable 
n = 10
print(n)

n = 'abc'
print(n)

#multiple assignment
z,x = 10, 12
print(z)
print(x)

#if 
if z > 9:
    print("Z is larger than 9")

# parenthesis needed for multi-line conditions

# and = &&
# or = ||

if((x>10 and x!=0) or (z<10)):
    x += 1 
    z=5
print(x)
print(z)

#while

a = 0
while a<=5:
    print(a)
    a+=1

# Looping from i = 0 to i = 10
print("Loop from 0 to 10")
for i in range(11):
    print(i)

# Looping from i = 2 to 5
print("Loop with range: ")
for i in range(2,5):
    print(i)

# Looping from i = 5 to i =1
print("Reverse loop: ")
for i in range(5,0,-1):
    print(i)