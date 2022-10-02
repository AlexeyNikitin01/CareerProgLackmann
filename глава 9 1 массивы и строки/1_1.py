"""
Реализуйте алгоритм, определяющий, все ли символы в строке встречаются
только один раз. А если при этом запрещено использование дополнительных
структур данных?
"""


# O(n)
def is_duplicate_letter(word: str) -> bool:
    if len(word) < 2:
        return False

    check_letter = {}
    for i in word:
        if check_letter.get(i):
            return False
        else:
            check_letter[i] = True
    return True


# O(nlogn)
def is_duplicate_letter_2(word: str) -> bool:
    if len(word) < 2:
        return False
    sorted_word = ''.join(sorted([i for i in word]))
    for i in range(1, len(word)):
        if sorted_word[i] == sorted_word[i-1]:
            return False
    return True


# O(n^2)
def is_duplicate_letter_3(word: str) -> bool:
    if len(word) < 2:
        return False

    for i in range(len(word)):
        if word[i] in word[:i] + word[i+1:]:
            return False
    return True


# O(n)
def is_duplicate_letter_4(word: str) -> bool:
    if len(word) < 2:
        return False

    if len(set(word)) == len(word):
        return False
    return True


if __name__ == '__main__':
    assert is_duplicate_letter('asdf') is True
    assert is_duplicate_letter('aaaf') is False
    assert is_duplicate_letter_2('asdf') is True
    assert is_duplicate_letter_2('aaaf') is False
    assert is_duplicate_letter_3('asdf') is True
    assert is_duplicate_letter_3('aaaf') is False
    assert is_duplicate_letter_4('asdf') is True
    assert is_duplicate_letter_4('aaaf') is False
