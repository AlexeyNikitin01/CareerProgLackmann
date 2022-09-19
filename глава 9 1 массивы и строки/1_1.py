"""
Реализуйте алгоритм, определяющий, все ли символы в строке встречаются
только один раз. А если при этом запрещено использование дополнительных
структур данных?
"""

from random import choice


def q_sort_str(word: str) -> str:
    if len(word) < 2:
        return word

    random_letter = choice(word)

    left = [j for j in word if ord(j) < ord(random_letter)]
    right = [j for j in word if ord(j) > ord(random_letter)]
    pivots = [j for j in word if ord(j) == ord(random_letter)]

    sort_word = q_sort_str(''.join(left)) + ''.join(pivots) + q_sort_str(''.join(right))

    return sort_word


def is_duplicate_letter(word: str) -> bool:
    if len(word) < 2:
        return False
    """
    for i in word:
        count = 0
        for j in word:
            if i == j:
                count += 1
        if count > 1:
            return False
    """
    """
    for i in range(len(word)):
        if word[i] in word[:i] + word[i+1:]:
            return False
    """
    """
    check_letter = {}
    for i in word:
        if check_letter.get(i):
            return False
        else:
            check_letter[i] = True
    """
    word = q_sort_str(word)

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            return False

    return True


if __name__ == '__main__':
    assert is_duplicate_letter('asdf') is True
    assert is_duplicate_letter('aaaf') is False
