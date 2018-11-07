L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10) )
print(g)
print(next(g))
print(next(g))
print(next(g))


g = (x*x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

def odd():
    print('step 1')
    yield(1)
    print('step 2')
    yield(3)
    print('step3')
    yield(5)

o=odd()
print(next(o))
print(next(o))
print(next(o))
print(next(o))