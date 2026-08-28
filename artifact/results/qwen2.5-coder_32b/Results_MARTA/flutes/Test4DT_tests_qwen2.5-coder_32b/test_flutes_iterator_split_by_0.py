
import pytest
from flutes.iterator import split_by


def test_split_by_criterion_no_empty_segments():
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]]




def test_split_by_string_criterion_no_empty_segments():
    result = list(split_by("abcde", criterion=lambda x: x in "aeiou"))
    assert result == [['b', 'c', 'd']]

def test_split_by_string_criterion_with_empty_segments():
    result = list(split_by("abcde", criterion=lambda x: x in "aeiou", empty_segments=True))
    assert result == [[], ['b', 'c', 'd'], []]