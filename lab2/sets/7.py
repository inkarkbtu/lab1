#set methods

#add
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)


#clear
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#copy
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)


a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
myset = a - b
print(myset)


a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
myset = a.difference(b, c)
print(myset)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)

#difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#Use -= as a shortcut instead of difference_update():

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
a -= b
print(a)

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
a.difference_update(b, c)
print(a)

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
a -= b | c
print(myset)

#discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x & y
print(z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x & y & z
print(result)

#isdisjoint

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

#issubset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#issuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x >= y
print(z)


x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)


fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)

#remove
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x ^ y
print(z)

#symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x ^= y
print(x)

#union method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x | y
print(z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x | y | z
print(result)

#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x |= y
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x.update(y, z)
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x |= y | z
print(x)