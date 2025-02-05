#Dictionary Methods

#clear
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)

#copy
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)

#fromkeys
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)

#get()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)
print(x)

#items
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018
print(x)

#keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"
print(x)

#pop
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print(car)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")
print(x)

#popitem
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")
print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()
print(x)

#setdefault
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print(x)

#update

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print(car)


#values

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018
print(x)