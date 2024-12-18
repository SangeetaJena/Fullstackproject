#WAP to search particular element in list
fruits = ["apple", "banana", "cherry", "date"]
target = "banana"
for fruit in fruits:
 if fruit == target:
  print("Found it!")
  break

# 0 1 1 2 3 5 8.....fibanacci series
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(1,6):
    sum1=a+b
    print(sum1,end=" ")
    a=b
    b=sum1
