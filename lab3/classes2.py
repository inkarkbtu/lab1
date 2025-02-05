from classes1 import StringManipulator, Square, Rectangle, Point, Account, filter_prime

# Тест StringManipulator
string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()

# Тест Square и Rectangle
square = Square(4)
print("Площадь квадрата:", square.area())

rectangle = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle.area())

# Тест Point
p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()
print("Расстояние между точками:", p1.dist(p2))

# Тест Account
acc = Account("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(1500)

# Тест Prime Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 11, 13, 15, 17, 19, 23, 24, 25]
print("Простые числа:", filter_prime(numbers))