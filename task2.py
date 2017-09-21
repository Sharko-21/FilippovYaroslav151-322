print('Введите первое число')
firstNum = float(input())
print('Введите второе число')
secondNum = float(input())
print('Введите "+" или "-"')
symbol = input()

symbolsStore = {'+': firstNum + secondNum, '-': firstNum - secondNum}
try:
    result = symbolsStore[symbol]
except KeyError as e:
    raise ValueError('Неправильный символ!')

print(result)