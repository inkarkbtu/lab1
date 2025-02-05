print(10 + 5)

x = 5
y = 3
print(x + y)

x = 5
y = 3
print(x * y)

x = 5
y = 2
print(x % y)

x = 15
y = 2
print(x // y)

x = 5
x += 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x ^= 3
print(x)

x = 5
x <<= 3
print(x)

x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x <= y)

x = 5
print(x > 3 and x < 10)

x = 5
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
print("pineapple" not in x)

print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 ^ 3)



"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(6 ^ 2 + 1)

"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5

More explanation:
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(5 == 4 + 1)
"""
The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 5 == 5 = True
"""

print(not 5 == 5)

"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""