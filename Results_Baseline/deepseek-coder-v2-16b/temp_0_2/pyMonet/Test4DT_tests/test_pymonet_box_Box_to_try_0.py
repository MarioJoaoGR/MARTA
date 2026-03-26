
import pytest
from pymonet.box import Box

# Test initialization of the Box class with different types of values
@pytest.mark.parametrize("value, expected", [
    (123, 123),
    ("Hello, World!", "Hello, World!"),
    ([1, 2, 3], [1, 2, 3]),
    ({'key': 'value'}, {'key': 'value'})
])
def test_box_initialization(value, expected):
    box = Box(value)
    assert box.value == expected

# Test the map method of the Box class
@pytest.mark.parametrize("value, mapper, expected", [
    (123, lambda x: str(x), "123"),
    ("Hello, World!", lambda s: s + "!", "Hello, World!!"),
    ([1, 2, 3], lambda lst: lst.append(None) or lst, [1, 2, 3, None])
])
def test_box_map(value, mapper, expected):
    box = Box(value)
    mapped_box = box.map(mapper)
    assert mapped_box.value == expected

# Test the equality method of the Box class
@pytest.mark.parametrize("value1, value2", [
    (Box(123), Box(123)),
    (Box("Hello, World!"), Box("Hello, World!")),
    (Box([1, 2, 3]), Box([1, 2, 3]))
])
def test_box_equality(value1, value2):
    assert value1 == value2

# Test the to_try method of the Box class
@pytest.mark.parametrize("value", [
    42,
    "example",
    {'key': 'value'}
])
def test_box_to_try(value):
    box = Box(value)
    try_monad = box.to_try()
    assert try_monad.value == value
