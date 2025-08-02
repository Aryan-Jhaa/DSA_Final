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

# division is decimal by default
print(5/2)

# to do int division, rounds down
print(5//2)

#modding is similar to most lang
print("modding 10 by 3: ")
print(10%3)

print("modding negative 10 by 3: ")
print(-10%3)

print("Fixing the negative mod by importing math and using fmod")
import math
print(math.fmod(-10, 3))

print("More math helpers: ")
print("Floor, round down of 3/2")
print(math.floor(3/2))
print("Ceil, round up of 3/2")
print(math.ceil(3/2))
print("2 power 3")
print(math.pow(2, 3))
print("sqrt of 2")
print(math.sqrt(2))

# Arrays, Lists in python:
print("Array(lists) in python: ")
arr = [1, 2, 3]
print(arr)

# can be used as an stack

arr.append(5)
print(arr)
arr.pop()
print(arr)

# array inster (index, value):
arr.insert(0, 10)
print(arr)

#sublists, slicing an array 
print("slicing an array: ")
print("Array before slicing: ")
arr2 = [7, 8, 9, 10, 12, 15, 17, 18]
print(arr2)
print("After slicing: ")
print(arr2[2:5])

# loop through arrays:
print("Printing array elements using for loop")
for i in range (len(arr2)):
    print(arr2[i])

# Reversing an array:
print("reversing an array: ")
nums = [10, 8, 6, 4, 2, 0]
print("Before reversing")
print(nums)
nums.reverse()
print("After reversing: ")
print(nums)

# Sorting an array 
sort_Array = [5, 1, 2, 10, 4, 6]
print("Before sorting: ")
print(sort_Array)

sort_Array.sort()
print("After sorting in ascending order: ")
print(sort_Array)

print("Sorting in descending order: ")
sort_Array.sort(reverse=True)
print(sort_Array)

#Strings: 
print("Strings: ")
s = "abcdef"
print(s[2:5])

#Double ended Queue 
from collections import deque

que = deque()
que.append(1)
que.append(2)
que.append(12)
print(que)

que.popleft()
print(que)

#Hash set:

mySet = set()
print("Hash sets: ")
mySet.add(4)
mySet.add(6)
print(mySet)

# Searching in hash set 
print(1 in mySet)
print(4 in mySet)

#Hash Maps or Dictionaries
city_map = {}

citiesIn = ["Delhi", "Bangalore", "Mumbai"]
city_map["India"] = []
city_map["India"] += citiesIn
citiesUS = ["New York", "Texas", "LA"]
city_map["US"] = []
city_map["US"] += citiesUS

print(city_map)

# Retrieving info from hash maps dot keys(), dot values(), dot items()

city_map = city_map.values()
print(city_map)