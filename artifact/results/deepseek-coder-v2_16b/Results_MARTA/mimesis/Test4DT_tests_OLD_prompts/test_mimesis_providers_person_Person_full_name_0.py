
import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from unittest.mock import patch

# Test for valid inputs with happy path scenario
def test_valid_inputs_happy_path():
    person = Person()
    assert isinstance(person, Person)
    full_name = person.full_name()
    assert isinstance(full_name, str)

# Test for edge cases where no gender is provided
def test_edge_cases():
    person = Person()
    assert isinstance(person, Person)
    with patch('mimesis.providers.person.get_random_item') as mock_get_random_item:
        mock_get_random_item.return_value = Gender.MALE
        full_name = person.full_name()
        assert isinstance(full_name, str)

# Test for specific gender input
def test_specific_gender():
    person = Person()
    assert isinstance(person, Person)
    with patch('mimesis.providers.person.get_random_item') as mock_get_random_item:
        mock_get_random_item.return_value = Gender.FEMALE
        full_name = person.full_name(gender=Gender.FEMALE)
        assert isinstance(full_name, str)

# Test for reversed full name order
def test_reversed_full_name():
    person = Person()
    assert isinstance(person, Person)
    with patch('mimesis.providers.person.get_random_item') as mock_get_random_item:
        mock_get_random_item.return_value = Gender.MALE
        full_name = person.full_name(reverse=True)
        assert isinstance(full_name, str)
