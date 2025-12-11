multi = lambda number1,number2: number1 * number2
sum = lambda number1,number2: number1 + number2

def calc(func,n1,n2):
    result = func(n1,n2)
    return result
result1 = calc(multi,3,6)
result2 = calc(sum,3,6)

print(result1,result2)