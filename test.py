import pytest
from main import count_vowels

@pytest.mark.parametrize("test_input,expected", [
    ('ААААооооЯЯЯЯииии', 16),                       # только гласные
    ('БББсссшвввв', 0),                             # только согласные
    ('ТEСТОВAЯ строка дЛя ПР0ВЕРКu', 9),            # смешанная строка
    ('', 0),                                        # пустая строка
])
def test_all(test_input, expected):
    assert count_vowels(test_input) == expected

