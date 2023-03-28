import re
text = input()
list_of_words = {}
list_of_matches = []
pattern = r'(?P<delimiter>@|#)(?P<first_word>[A-Za-z]{3,})\1{2}(?P<second_word>[A-Za-z]{3,})\1'
compiled_pattern = re.compile(pattern)
result = compiled_pattern.finditer(text)
if result:
    for el in result:
        first_word = el['first_word']
        second_word = el['second_word']
        list_of_words[first_word] = second_word
if list_of_words:
    print(f"{len(list_of_words)} word pairs found!")
else:
    print(f'No word pairs found!')
for key, value in list_of_words.items():
    if value[::-1] == key:
        list_of_matches.append(f'{key} <=> {value}')
if not list_of_matches:
    print("No mirror words!")
else:
    print(f'The mirror words are:')
    print(', '.join(list_of_matches))
