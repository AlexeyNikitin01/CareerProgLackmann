"""
Существуют три вида модифицирующих операций со строками: вставка
символа, удаление символа и замена символа. Напишите функцию, которая
проверяет, находятся ли две строки на расстоянии одной модификации (или
нуля модификаций).
Пример:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def is_letter_replace(word_1: str, word_2: str) -> bool:
    check_replace = False
    for i in range(len(word_1)):
        if word_1[i] != word_2[i] and check_replace:
            check_replace = False
            return check_replace
        elif word_1[i] != word_2[i]:
            check_replace = True
    return True


def is_letter_insert(word_1: str, word_2: str) -> bool:
    for i in range(len(word_2)):
        if word_1[i] != word_2[i]:
            return False
    return True


def is_two_modification(word_1: str, word_2: str) -> bool:
    if len(word_1) - len(word_2) > 1:
        return False

    if len(word_1) == len(word_2):
        return is_letter_replace(word_1, word_2)
    elif len(word_1) - 1 == len(word_2):
        return is_letter_insert(word_1, word_2)
    elif len(word_1) + 1 == len(word_2):
        return is_letter_insert(word_2, word_1)


if __name__ == '__main__':
    assert is_two_modification('pale', 'pal') is True
    assert is_two_modification('pales', 'bale') is False
    assert is_two_modification('pale', 'llll') is False
    assert is_two_modification('pale', 'bale') is True
