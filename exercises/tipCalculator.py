print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip woul you like to give? 10, 12 or 15? '))
total_with_tip = bill + bill * (tip / 100)
num_of_people = int(input('How many people to split the bill? '))
split_total = total_with_tip / num_of_people
rounded = round(split_total, 2)
rounded = "{:.2f}".format(split_total)
final_message = f'Each person shoul pay: ${rounded}'
print(final_message)
