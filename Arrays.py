import array as arr
a=arr.array('i',[1,2,3])
for i in range(0,3):
    print(a[i],end=" ")
print("\n")

a=arr.array('d',[1.4,2.6,3.8])
for i in range(0,3):
    print(a[i],end=" ")
print("\n")

a=arr.array('i',[1,2,3,5,6])
a.insert(2,5)
for i in range(0,6):
    print(a[i],end=" ")
print("\n")

print(a.count(2))
print("\n")

print(a.index(5))
print("\n")

print()