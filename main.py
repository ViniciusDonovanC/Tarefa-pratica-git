
def fatorial(num):
    i = num
    while i > 1:

        i -= 1
        num *= i

    return num

x = input()

print 'fatorial: ', fatorial(x)

