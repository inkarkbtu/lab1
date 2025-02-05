#list methods


#append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)


#clear
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()


#copy
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()


#count
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

#extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)

#index
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)

#insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

#pop
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

#remove
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

#reverse
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

#sort
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)