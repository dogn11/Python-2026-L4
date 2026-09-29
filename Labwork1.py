#1
n = int(input("enter the radius"))
area = 3.14*n*n
print(area)
#2
m = int(input("enter the temperature in celcius"))
f = float(m * 1.8 + 32)
print(f)
#3
p = int(input("enter the number:"))
for i in range(2,n):
    if n % i == 0:
        print("not a prime")
        break
    else: 
        print("prime")
#4
c = int(input("enter the number:"))
sum = 0 
for i in range(1,c//2 + 1):
    if c % i == 0:
        sum = sum + i
if sum == c:
    print("is perfect")
else: 
    print("is not perfect")

#5
n = ["red","blue","green"]
m = (input("enter the fav color")).strip()
if m in n: 
    print(f"your color is at index {n.index(m)} in my list")
else:
    print("there no color in my list")
#6
nums = range(0,7)
print(list(nums))
nums1 = range(1,11,3)
print(list(nums1))
nums2 = range(5,0,-1)
print(list(nums2))
nums3 = range(6,-2,-2)
print(list(nums3))
#7
def remove_dol_string(s):
    return s.replace("$","s")
n = input("enter the string")
result = remove_dol_string(n)
print(result)
#8
def extract_even_number(s):
    n = s.copy()
    for i in (s):
        if i % 2 != 0:
            n.remove(i)
    return n
l = [1,4,5,-1,10]
result = extract_even_number(l)
print(result)
#9 
def factorial_of_number(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    return s
n = 3
result = factorial_of_number(n)
print(result)
#10
def get_out_divisors(d):
    n = []
    for i in range(1,d+1):
        if d % i == 0:
            n.append(i)
    return n
d = 6 
result = get_out_divisors(d)
print(result)
#11
import math
x1 = int(input("enter x1: "))
y1 = int(input("enter y1: "))
x2 = int(input("enter x2: "))
y2 = int(input("enter y2"))
distance = math.sqrt((x1-x2)**2 -(y1-y2)**2)
print(f"the distance is: {distance:.2f}")
#12 
def print_out(m,n):
    for i in range(n):
        if i == 0 or i == n -1:
            print("*" * m)
        else:
            print("*" + " "*(m-2) + "*")
x = 4 
y = 3 
result = print_out(x,y)
print(result)