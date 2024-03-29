#1
def generate_squares(N):
    for i in range(N):
        yield i ** 2

try:
    N = int(input("Enter a number (N) to generate squares up to N: "))
    square_generator = generate_squares(N)
    print("Generated squares: ")
    for square in square_generator:
        print(square)
except ValueError:
        print("Invalid input")


#2
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input("Enter the value for n: "))
        if n < 0:
            print("Please enter a positive number.")
            return

        even_numbers = even_generator(n)
        result = ",".join(map(str, even_numbers))
        print("Even numbers between 0 and ", n, " :", result)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


#3
def generate(c):
    for i in range(c + 1):
            if i % 3 == 0 and i % 4 == 0:
                yield i
                
c = int(input("Enter a number c: "))
print("Numbers between 0 and ", c, " divisible by both 4 and 3 : ")
for num in generate(c):
    print(num)

#4
def squares(a, b):
    for i in range(a, b + 1 ):
        yield i ** 2
        
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
print("Squares from ", a, " to ", b)
for square in squares(a, b):
    print(square)
#ex5
def generate(j):
    while j >= 0:
        yield j
        j -= 1
j = int(input("Enter a number(j): "))
print("Counting down from ", j, " to 0 :")
for number in generate(j):
    print(number)