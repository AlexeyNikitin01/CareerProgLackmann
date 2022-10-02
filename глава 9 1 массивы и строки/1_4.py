"""
Напишите функцию, которая проверяет, является ли заданная строка переста­
новкой палиндрома. (Палиндром -
слово или фраза, одинаково читающиеся
в прямом и обратном направлении; перестановка -
строка, содержащая те
же символы в другом порядке.) Палиндром не ограничивается словами из
словаря.
Ilpuмep:
Ввод: Tact Соа
Вывод: True (перестановки: "taco cat", "atco cta", и т. д.)
"""
from collections import Counter


# O(n)
def palindrome(word: str) -> bool:
    if len(word) < 2:
        return True

    word = word.lower().replace(' ', '')

    if len(list(filter(lambda x: x % 2 == 1, Counter(word).values()))) > 1:
        return False
    return True


if __name__ == '__main__':
    assert palindrome('Tact Coa') is True
    assert palindrome('аааа') is True
    assert palindrome('abaa') is False
