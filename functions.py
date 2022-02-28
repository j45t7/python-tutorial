def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print('Welcome')


#greet("Justyna", "Marciniak")


def greet_again(name):
    print(f"Hello {name}")

# Types of functions
# 1 - perform a task
# 2 - Return a value
# By default returns None


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Justyna")
file = open("content.txt", "w")
file.write(message)
