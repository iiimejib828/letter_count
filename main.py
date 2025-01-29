def count_vowels(text):
    VOWELS = set("aeiouаеёиоуыэюя")  # Используем set для быстрого поиска
    return sum(1 for letter in text if letter.lower() in VOWELS)
