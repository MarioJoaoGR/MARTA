# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringBase

# Test cases for SuperStringBase class
def test_superstringbase_length():
    """Test the length method of SuperStringBase."""
    class MyString(SuperStringBase):
        def __init__(self, string):
            self._content = string

        def length(self):
            return len(self._content)

    my_instance = MyString("Hello, World!")
    assert my_instance.length() == 13

def test_superstringbase_default_length():
    """Test the default length method of SuperStringBase."""
    class MyStringDefault(SuperStringBase):
        def __init__(self, string=""):
            self._content = string

        def length(self):
            return len(self._content)

    my_instance_default = MyStringDefault()
    assert my_instance_default.length() == 0

def test_superstringbase_len_method():
    """Test the __len__ method of SuperStringBase."""
    class SuperStringLen(SuperStringBase):
        def __init__(self, content=""):
            self._content = content

        def length(self):
            return len(self._content)

    my_instance_len = SuperStringLen("Hello, World!")
    assert my_instance_len.__len__() == 13

def test_superstringbase_character_at():
    """Test the character_at method of SuperStringBase."""
    class MyString(SuperStringBase):
        def __init__(self, string):
            self._content = string

        def length(self):
            return len(self._content)

        def character_at(self, index):
            if 0 <= index < self.length():
                return self._content[index].lower()
            return ""

    my_instance = MyString("Hello, World!")
    assert my_instance.character_at(7) == "w"

def test_superstringbase_substring():
    """Test the substring method of SuperStringBase."""
    class MyString(SuperStringBase):
        def __init__(self, string):
            self._content = string

        def length(self):
            return len(self._content)

        def character_at(self, index):
            if 0 <= index < self.length():
                return self._content[index].lower()
            return ""

        def substring(self, start_index, end_index=None):
            if end_index is None:
                end_index = self.length()
            return self._content[start_index:end_index].lower()

    my_instance = MyString("Hello, World!")
    assert my_instance.substring(0, 5) == "hello"

def test_superstringbase_to_printable():
    """Test the to_printable method of SuperStringBase."""
    class SuperStringSubstring(SuperStringBase):
        def __init__(self, base, start_index, end_index):
            self._base = base
            self._start_index = start_index
            self._end_index = end_index

        def get_substring(self):
            return self._base[self._start_index:self._end_index]

        def length(self):
            return len(self.get_substring())

        def character_at(self, index):
            if 0 <= index < self.length():
                return self.get_substring()[index].lower()
            return ""

        def substring(self, start_index, end_index=None):
            if end_index is None:
                end_index = self.length()
            return self.get_substring()[start_index:end_index]

        def to_printable(self, start_index=None, end_index=None):
            if start_index is None:
                start_index = 0
            if end_index is None:
                end_index = self.length()
            return self.get_substring()[start_index:end_index]

    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.to_printable() == "World"
