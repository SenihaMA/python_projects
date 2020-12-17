print('how heavy are you')
kg = input('I am (kg): ')
kg = int(kg)
if kg > 100:
  print('uh')
elif 60 < kg < 100:
  print('ok')
elif kg < 60:
  print('wow')
else:
  print('what')
