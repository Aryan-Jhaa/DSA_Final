# Armstrong number check

n = input("Enter a number: ")
num = int(n)
no_d = len(n)
total = 0

temp = num
while temp > 0:
    ld = temp % 10
    total += ld ** no_d
    temp //= 10

print("Original Number: " + str(num))
print("After calculation: " + str(total))

if num == total:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
