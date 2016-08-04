print('welcome to ubuntu calculator')

number_one = input('what is your first number? ')
a = str(number_one)
operation = input('which operation would you like to use? ')

if operation == "addition":
  add_num = input('what is your second number? ')
  b = str(add_num)
  c = float(a) + float(b)
  abc = str(c)
  print('your output is ' + abc)

elif operation == "subtraction":
  sub_num = input('what is your second number? ')
  d = str(sub_num)
  e = float(a) - float(d)
  ade = str(e)
  print('your output is ' + ade)

elif operation == "multiplication":
  mul_num = input('what is your second number? ')
  f = str(mul_num)
  g = float(a) * float(f)
  afg = str(g)
  print('your output is ' + afg)

elif operation == "division":
  div_num = input('what is your second number? ')
  h = str(div_num)
  i = float(a) / float(h)
  ahi = str(i)
  print('your output is ' + ahi)

print('thank you for using ubuntu calculator')
print('have a nice day ^.^')

input('please press enter to exit')
