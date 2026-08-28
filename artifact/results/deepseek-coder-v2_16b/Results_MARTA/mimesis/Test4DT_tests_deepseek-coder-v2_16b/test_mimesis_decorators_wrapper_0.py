
import pytest
from mimesis.decorators import UnsupportedLocale
from mimesis import data
from string import ascii_letters, digits, punctuation

def wrapper(*args, **kwargs):
    try:
        # Cyrillic string can contain ascii symbols, digits and punctuation.
        alphabet = {s: s for s in ascii_letters + digits + punctuation}
        alphabet.update({**data.ROMANIZATION_DICT[kwargs['locale']], **data.COMMON_LETTERS})
    except KeyError:
        raise UnsupportedLocale(kwargs['locale'])

    result = kwargs['func'](*args)
    txt = ''.join([alphabet[i] for i in result if i in alphabet])
    return txt

def test_valid_input_ru():
    def func(s):
        return s
    
    input_string = "Привет мир"
    result = wrapper(input_string, func=func, locale='ru')
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert len(result) > 0, "Resulting string is empty"


def test_invalid_locale():
    def func(s):
        return s
    
    input_string = "Invalid locale string"
    with pytest.raises(UnsupportedLocale):
        wrapper(input_string, func=func, locale='unsupported_locale')