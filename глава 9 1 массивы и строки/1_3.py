"""
Напишите метод, заменяющий все пробелы в строке символами '%20'. Можете
считать, что длина строки позволяет сохранить дополнительные символы,
а фактическая длина строки известна заранее. (Примечание: при реализации
метода нajava для выполнения операции ~на месте» используйте символьный
массив.)
Ilpuмep:
Ввод: "Mr John Smith", 13
Вывод: "Mr%20John%20Smith"
"""


class Word:
    def __init__(self, word: str, len_word: int):
        self.word = word
        self.len_word = len_word

    def replace_letter(self):
        return self.word[:self.len_word].replace(' ', '%20')


if __name__ == '__main__':
    result = Word('Mr John Smith', 13)
    assert result.replace_letter() == 'Mr%20John%20Smith'
    