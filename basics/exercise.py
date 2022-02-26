weight = float(input('What is your weight? '))
metric = input('(K)g or (L)bs: ')

if metric.upper() == 'K':
  converted = weight / 0.45
  print('Weight in Kg: ' + str(converted))
else:
  converted = weight * 0.45
  print('Weight in L: ' + str(converted))
