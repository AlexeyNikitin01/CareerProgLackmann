"""
Для двух строк напишите метод, определяющий, является ли одна строка
перестановкой другой .
"""

from random import choice


class Word:
    def __init__(self, word: str):
        self.word = self.q_sort_word(word.lower())

    def is_replaced(self, other_word: str) -> bool:
        if len(self.word) != len(other_word):
            return False

        other_word = self.q_sort_word(other_word.lower())

        if self.word != other_word:
            return False

        return True

    def q_sort_word(self, word):
        if len(word) < 2:
            return word

        pivot = choice(word)

        pivots = [i for i in word if ord(i) == ord(pivot)]
        left = [i for i in word if ord(i) < ord(pivot)]
        right = [i for i in word if ord(i) > ord(pivot)]

        return self.q_sort_word(''.join(left)) + ''.join(pivots) + self.q_sort_word(''.join(right))


if __name__ == '__main__':
    word = 'GOd'
    other_word = 'dog'
    result = Word(word)
    print(result.is_replaced(other_word))
