"""
Реализуйте метод для выполнения простейшего сжатия строк с использованием
счетчика повторяющихся символов. Например, строка ааЬсссссааа превра­
щается в а2Ыс5а3. Если «сжатая» строка не становится короче исходной,
то метод возвращает исходную строку. Предполагается, что строка состоит
только из букв верхнего и нижнего регистра (a-z).
"""


def string_compression(text: str) -> str:
    if len(text) <= 2:
        return text

    compression_text = ''
    count = 0
    for i in range(len(text)):
        count += 1
        if i+1 >= len(text) or text[i] != text[i+1]:
            compression_text += text[i] + str(count)
            count = 0

    if len(compression_text) >= len(text):
        return text
    return compression_text


if __name__ == '__main__':
    assert string_compression('aabbcccaaa') == 'a2b2c3a3'
    assert string_compression('') == ''
    assert string_compression('aa') == 'aa'
    assert string_compression('aabb') == 'aabb'
    assert string_compression('aab') == 'aab'
