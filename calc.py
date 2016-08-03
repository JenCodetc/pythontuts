print('welcome to ubuntu calculator')

operation = input('which operation would you like to use? ')
number_one = input('what is your first number? ')
a = str(number_one)
number_two = input('what is your second number? ')
b = str(number_two)

if operation == "addition":
  c = float(a) + float(b)
  abc = str(c)
  print('your output is ' + abc)

elif operation == "subtraction":
  d = float(a) - float(b)
  abd = str(d)
  print('your output is ' + abd)

elif operation == "multiplication":
  e = float(a) * float(b)
  abe = str(e)
  print('your output is ' + abe)

elif operation == "division":
  f = float(a) / float(b)
  abf = str(f)
  print('your output is ' + abf)

print('thank you for using ubuntu calculator')
print('have a nice day ^.^')

input('please press enter to exit')
