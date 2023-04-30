""""letters = ["q","c","c"]
matrix = [[0,1], [2,3], [5,6]]
print(letters)

zeros = [0] * 5
combined = zeros + letters
print(combined)

numbers = list(range(20))

chars = list("Hello World")
print(chars) """

letters = ["a", "b", "c", "d"]
print(letters)


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


def get_greeting(name):
    return f"Hi {name}"


greet("Sudip", "Sikdar")

getval = get_greeting("Pagla")

print(getval)


def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply(2, 3, 4, 5))


letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100

print(zeros)


def save_user(**user):
    print(user["name"])


save_user(id=1, name="sudip", age=41)
