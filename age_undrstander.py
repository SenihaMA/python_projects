print('How old are you?')
old = input('My age is: ') 
old = int(old)
if 0 < old < 5:
  print('baby')
elif 5 < old < 10:
  print('child')
elif 10 < old < 20:
  print('teen')
elif 20 < old < 40: 
  print('yung')
elif 40 < old < 65:
  print('middle age')
elif 65 < old < 100:
  print('old')
elif old > 100:
  print('very old')
else:
  print('please write your age')
