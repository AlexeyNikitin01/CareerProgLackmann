"""
Для двух строк напишите метод, определяющий, является ли одна строка
перестановкой другой .
"""


class Word:
    def __init__(self, word: str):
        self.word = word

    def is_replaced(self, other_word: str) -> bool:
        if len(self.word) != len(other_word):
            return False

        if ''.join(sorted([i for i in self.word.lower()])) != \
                ''.join(sorted([i for i in other_word.lower()])):
            return False
        return True


if __name__ == '__main__':
    result = Word('DOG')
    assert result.is_replaced('god') is True
    assert result.is_replaced('jon') is False
