list_a = list(range(1, 30))
list_b = 30 * [6]
x = int(input())
print(list_a.index(x))
print(list_b[list_a.index(x)])
