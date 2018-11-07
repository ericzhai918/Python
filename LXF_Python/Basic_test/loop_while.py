#1-100内奇数的和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#1-100内奇数的和
sum = 0
for x in range(0,100):
    if x % 2 == 0:
        continue
    else:
        sum = sum + x
print(sum)

#1-100的和
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

#1-10的和
n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
#1-10内奇数的和
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

