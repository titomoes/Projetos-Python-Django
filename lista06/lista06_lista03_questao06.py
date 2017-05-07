list_letter = []
list_word = []
x = int(input())
num0cor = 0
for i in range(x):
    list_word.append(str(input()))
y = int(input())
for i in range(y):
    list_letter.append(str(input()))
for i in range(y - x + 1):
    if list_word[i] == list_letter[i]:
        j = 2
        ocorre = True
        while j <= y and ocorre:
            if list_letter[j] == list_word[i + j - 1]:
                j += 1
            else:
                ocorre = False
        if ocorre:
            num0cor += 1
print(num0cor)
