i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

# 2
for i in range(1):
    print("#")
else:
    print("#")

# 3
print(3)
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

print(4)
var = 1
while var < 10:
    print("f")
    var = var << 1

z = 10
y = 0
x = (y < z) and (z > y) or (y > z) and (z < y)

print(x)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]

print(vals,"antes")

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals,"después")

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2,"Lista2")

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)



my_list = [i for i in range(-1, 2)]
print(my_list)


my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])