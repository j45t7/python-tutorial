def increment(number, by=1):
    return number + by


print(increment(2, 3))

# default arguments added after required parameter


def multipy(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multipy(2, 3, 4, 5))


def save_user(**user):  # with double asterisk pass multiple key value pairs
    print(user['name'])


# {'id': 1, 'name': 'John', 'age': 22} python creates dictionary
save_user(id=1, name="John", age=22)
