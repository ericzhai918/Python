#计算a2 + b2 + c2...
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2,3]))
print(calc([1,3,5,7,9]))

#利用可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))
print(calc(1,2,3,4,5))