StringInput = input ('Введите предложение: ')
lst = StringInput.split(' ')
a = []

a = [i for i in lst if 'абв' not in i]

print (*a)