
from string_utils import words_count

def test_words_count_mixed_alphanumeric_characters_and_punctuation():
    assert words_count('example,string,with,punctuation123') == 4
