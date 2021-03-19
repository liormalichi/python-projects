numbers = {'first': 1, 'second': 2, 'third': 3, 'Fourth': 4}
t=[value for value in sorted(numbers.items(), reverse=True)]
t2=[value for (key,value) in sorted(numbers.items(), reverse=True)]
print(t)
print(t2)
