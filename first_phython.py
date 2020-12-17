variable_1 = 1 #the value is an integer
variable_2 = 2.30 # the value is a float
variable_3 = 'Hello World!' # the variable is string

hw = 23
hi = 24
ho = hw 

aaa = 444
aab = aaa
abb = aab
bbb = abb
print(bbb)

variable_4 = ""

print(type(variable_1))
print(type(variable_2))
print(type(variable_3))
print(type(variable_4))

my_string = 'My name is "Mary"!'
print(my_string)

def abc_123_(q):
  """
  this is a docstring to make an exemle 
  """
  print(q * 2)
abc_123_(6)
abc_123_(3.3)
abc_123_('aabb ccdd ')
print(abc_123_.__doc__)
print(type(abc_123_)) 

def mult_2(x):
  '''
  This function gives the multiples of the number 2.
  It takes an integer or a float as an argument and returns the result of multiplying
  that number by 2.
  It returns error if the argument is anything but int and float data types.
  Enjoy your calculus
  '''
  if type(x) is int or type(x) is float: print(x * 2)
  else: print('This is not a valid number!')
# print(mult_2.__doc__)
mult_2(6)
mult_2(3.3)
mult_2('AABB CCDD ')
print(mult_2.__doc__)
