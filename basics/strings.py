course = 'Python for Beginners'

print(course.upper())
print(course.lower())
print(course.find('Y'))  # case sensitive
print(course.find('y'))
print(course.replace('for', '4'))
print('Python' in course)  # instead of index boolean

# multiline text
email = '''
Hello John,

Thak you,
Bye
'''

print(email)
print(course[1])
print(course[-1])
print(course[0:6])
print(course[6:])

# copy of strings
another = course[:]
print(another)
print(course[1:-1])
