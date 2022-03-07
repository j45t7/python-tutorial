age = int(input('What is your current age? '))

years_left = 90 - age

days = years_left * 365
weeks = years_left * 52
months = years_left * 12

message = f"You have {days} days, {weeks} weeks, {months} months left."
print(message)
