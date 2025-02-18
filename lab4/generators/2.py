def generate_even_numbers(n):
    for i in range(0, n+1, 2): 
        yield i

n = int(input("Enter a number n: "))

even_numbers = generate_even_numbers(n)
print(", ".join(map(str, even_numbers)))