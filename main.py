def single_root_words (root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for i in other_words:
        i = i.lower()
        if root_word in i or i in root_word:
            same_words.append (i)
    return same_words

result_1 = single_root_words('Лес', 'лесник', 'переход', 'лесной', 'переезд')
result_2 = single_root_words('Сад', 'рассада', 'палисадник', 'огрод')

print (result_1)
print (result_2)



