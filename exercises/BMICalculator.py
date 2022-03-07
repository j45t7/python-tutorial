height = float(input('Your height in m: '))
weight = float(input('Your weight in kg: '))

bmi = weight // height ** 2
bmi_as_int = int(bmi)
print(f'Your BMI: {bmi_as_int}')
