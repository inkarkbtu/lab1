def generate_squares(N):
    for i in range(1, N+1):
        yield i ** 2

N = int(input("Enter a number N: "))
for square in generate_squares(N):
    print(square)