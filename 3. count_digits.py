# Count the number of digits

count = 0
n = input()

num = int(n)

while num > 0:
    count += 1
    num = num//10

print(count)