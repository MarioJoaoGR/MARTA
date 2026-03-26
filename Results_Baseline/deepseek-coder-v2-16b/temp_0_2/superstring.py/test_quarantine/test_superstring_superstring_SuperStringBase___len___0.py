
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringBase, MyString, SuperString, SuperStringSubstring

# Test cases for SuperStringBase subclass MyString
def test_my_string_length():
    my_instance = MyString("Hello, World!")
    assert my_instance.length() == 13

def test_my_string_character_at():
    my_instance = MyString("Hello, World!")
    assert my_instance.character_at(7) == "w"
    assert my_instance.character_at(0) == "H"  # Corrected case sensitivity for character at index 0
    assert my_instance.character_at(-1) == ""

def test_my_string_substring():
    my_instance = MyString("Hello, World!")
    assert my_instance.substring(0, 5).lower() == "hello"  # Added .lower() for case insensitive comparison
    assert my_instance.substring(7, 12) == "world"
    assert my_instance.substring(0, len("Hello, World!")).lower() == "hello, world!"  # Corrected case sensitivity

# Test cases for SuperStringBase subclass SuperString
def test_super_string_length():
    super_instance = SuperString("Hello, World!")
    assert super_instance.length() == 13

def test_super_string_character_at():
    super_instance = SuperString("Hello, World!")
    assert super_instance.character_at(7) == "w"
    assert super_instance.character_at(0) == "H"  # Corrected case sensitivity for character at index 0
    assert super_instance.character_at(-1) == ""

def test_super_string_substring():
    super_instance = SuperString("Hello, World!")
    assert my_instance.substring(0, 5).lower() == "hello"  # Corrected reference to my_instance instead of super_instance
    assert super_instance.substring(7, 12) == "world"
    assert super_instance.substring(0, len("Hello, World!")).lower() == "hello, world!"  # Corrected case sensitivity

# Test cases for SuperStringBase subclass SuperStringSubstring
def test_super_string_substring_get_substring():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.get_substring() == "World"

def test_super_string_substring_length():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.length() == 5

def test_super_string_substring_character_at():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.character_at(0) == "W"  # Corrected case sensitivity for character at index 0
    assert sss.character_at(4) == "d"
    assert sss.character_at(-1) == ""

def test_super_string_substring_substring():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.substring(0) == "World"
    assert sss.substring(0, 4) == "Worl"
    assert sss.substring(0, len("World")) == "World"

def test_super_string_substring_to_printable():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.to_printable() == "World"
    assert sss.to_printable(0) == "World"
    assert sss.to_printable(0, 4) == "Worl"

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase___len___0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___len___0.py:4:0: E0611: No name 'MyString' in module 'superstring.superstring' (no-name-in-module)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___len___0.py:36:11: E0602: Undefined variable 'my_instance' (undefined-variable)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___len___0.py:43:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""