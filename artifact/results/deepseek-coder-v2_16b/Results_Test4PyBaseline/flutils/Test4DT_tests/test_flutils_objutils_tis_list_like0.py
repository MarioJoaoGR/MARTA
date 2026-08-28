# Module: flutils.objutils
import pytest
from flutils.objutils import is_list_like
from collections import deque
from itertools import chain

# Test cases for is_list_like function
def test_is_list_like_with_list():
    assert is_list_like([1, 2, 3]) == True

def test_is_list_like_with_generator():
    def generate_numbers():
        yield 1
        yield 2
        yield 3
    assert is_list_like(generate_numbers()) == True

def test_is_list_like_with_non_iterable():
    assert is_list_like('hello') == False

def test_is_list_like_with_sorted_list():
    assert is_list_like(sorted([1, 2, 3])) == True

def test_is_list_like_with_custom_object():
    assert is_list_like(deque([1, 2, 3])) == True

def test_is_list_like_with_none():
    assert is_list_like(None) == False

def test_is_list_like_with_boolean_false():
    assert is_list_like(False) == False

def test_is_list_like_with_empty_list():
    assert is_list_like([]) == True

# Additional edge cases to consider:
def test_is_list_like_with_chainmap():
    from collections import ChainMap
    chainmap = ChainMap([1, 2, 3], {})
    assert is_list_like(chainmap) == False

def test_is_list_like_with_counter():
    from collections import Counter
    counter = Counter([1, 2, 3])
    assert is_list_like(counter) == False

def test_is_list_like_with_ordereddict():
    from collections import OrderedDict
    ordered_dict = OrderedDict([('a', 1), ('b', 2)])
    assert is_list_like(ordered_dict) == False

def test_is_list_like_with_userdict():
    from collections import UserDict
    user_dict = UserDict({'a': 1, 'b': 2})
    assert is_list_like(user_dict) == False

def test_is_list_like_with_userstring():
    from collections import UserString
    user_string = UserString("hello")
    assert is_list_like(user_string) == False

def test_is_list_like_with_defaultdict():
    from collections import defaultdict
    default_dict = defaultdict(int, {'a': 1, 'b': 2})
    assert is_list_like(default_dict) == False

def test_is_list_like_with_decimal():
    from decimal import Decimal
    decimal = Decimal('12.34')
    assert is_list_like(decimal) == False

def test_is_list_like_with_dict():
    dictionary = {'a': 1, 'b': 2}
    assert is_list_like(dictionary) == False

def test_is_list_like_with_float():
    float_value = 12.34
    assert is_list_like(float_value) == False

def test_is_list_like_with_int():
    int_value = 123
    assert is_list_like(int_value) == False

def test_is_list_like_with_str():
    string = "hello"
    assert is_list_like(string) == False
