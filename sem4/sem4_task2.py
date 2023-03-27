# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.

in_string = input("Введите строку: ").lower()

strings = in_string.split()

print(strings)

my_dict = set()
for i in range(len(strings)):
    print(strings[i])
    if strings[i] not in my_dict:
        my_dict.add(strings[i])

print(my_dict)
print(len(my_dict))