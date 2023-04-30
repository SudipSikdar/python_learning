"""
letters = ["a", "b", "c"]

print(letters)
zeros = [0] * 5

combined = zeros + letters
print(combined)

print(list(range(20)))

chars = list("Hello World")
print(chars)
print(len(chars))

letters = ["a", "b", "c", "d"]
print(letters[-1])
numbers = list(range(1, 10))
print(numbers[::2])

numbers = [1, 2, 3, 4, 4, 5, 6, 7]

first, second, *other = numbers

print(first)
print(other)


def multiply(*numbers):
    print(numbers)


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


multiply(1, 2, 3, 4, 5)
greet("Sudip", "Sikdar")


def get_greeting(first_name):
    print(f"Hi{first_name}")


print(get_greeting("Sudip"))

message = get_greeting("haha")
print(message)
file = open("content.txt", "w")
file.write(message)


def increment(number, by):
    return number + by


result = increment(2, 3)

print(result)


def increment(number, by=2):
    return number * by


result = increment(2)

print(result)



def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def save_user(**user):
    print(user["age"])


save_user(id=1, name="Sudip", age=45)

"""

letters = ["a", "b", "c", "d"]

for index, letter in enumerate(letters):
    print(index, letter)

# Add

letters = ["a", "b", "c", "d"]

# letters.append("e")

letters.insert(2, "k")

letters.pop()
print(letters)
