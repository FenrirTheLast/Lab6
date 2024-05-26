import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)

# print(a)
#
# print(b)

c = a - b

print(c)

print(b**2)

print(a)

a += b

print(a)

a -= b

print(a)
a = np.array(3)
b = np.arange(3)

print(b)

print(np.exp(b))

print(np.sqrt(b))

c = np.array([2, -1, 4.])

print(np.add(b, c))

d = a * b

print(d)

a = np.array(3)
b = np.arange(3)
print(a)
print(b)

print(a.dot(b))
print(np.dot(a, b))

c = np.array([[1, 5], [2, 6], [7, 4]])
d = np.array([[2, 5, 4], [4, 3, 1]])
print(c)
print(d)
print(np.dot(c, d))
print(np.dot(d, c))

