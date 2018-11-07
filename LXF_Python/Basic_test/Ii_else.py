#if
age =20

if age >= 18:
    print('you age is:',age)
    print('adult')

#if...else
age = 3
if age >= 18:
    print('your age is:',age)
    print('adult')
else:
    print("your age is:",age)
    print('teenager')

#if..elif
age = 3
if age >=18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#加上用户输入
birth = int(input('Please input your birth year:'))
if birth < 2000:
    print('before 2000')
else:
    print('after 2000')