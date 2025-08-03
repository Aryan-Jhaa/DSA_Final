# check palindrome
n = input()

num = int(n)
result = 0

while num>0:
    ld = num%10
    result = (result*10)+ld
    num = num//10
print("original num: " + str(n))

print("result: " + str(result))

if result == int(n):
    print("It is a palindrome")

else:
    print("It is not a palindrome")
    