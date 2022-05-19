s = "Hello World"
p = ("Hong Gil Dong", 30, 'M', [70, 175])
k = [1, 2, 3, 4]
d = {'name':'Apple'}

# 1
# "Goodbye" + s[-6] + s[6:]
print("Goodbye" + s[-6] + s[6:])

# 2
# p[3][1]
print(p[3][1])

# 3
n, a = p[:2]; print(a)

# 4
print(k[::-1])

# 5
print([3*i for i in k if i > 2])

# 6
d[1] = "Orange"; print(d)