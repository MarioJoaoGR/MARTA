
import pytest
from typing import Dict, List, TypeVar

T = TypeVar('T')

def reverse_map(d: Dict[T, int]) -> List[T]:
    r"""Given a dict containing pairs of ``(item, id)``, return a list where the ``id``-th element is ``item``.

    .. note::
        It is assumed that the ``id``\ s form a permutation.

    .. code:: python

        >>> words = ['a', 'aardvark', 'abandon']
        >>> word_to_id = {word: idx for idx, word in enumerate(words)}
        >>> id_to_word = reverse_map(word_to_id)
        >>> (words == id_to_word)
        True

    :param d: The dictionary mapping ``item`` to ``id``.
    """
    return [k for k, _ in sorted(d.items(), key=lambda xs: xs[1])]

# Test cases
def test_reverse_map_basic():
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {word: idx for idx, word in enumerate(words)}
    id_to_word = reverse_map(word_to_id)
    assert words == id_to_word

def test_reverse_map_empty():
    empty_dict = {}
    reversed_empty_list = reverse_map(empty_dict)
    assert reversed_empty_list == []

def test_reverse_map_large():
    large_words = [f'word{i}' for i in range(1000)]
    large_dict = {word: idx for idx, word in enumerate(large_words)}
    reversed_large_list = reverse_map(large_dict)
    assert len(reversed_large_list) == len(large_words)

def test_reverse_map_single_element():
    single_element_dict = {'a': 0}
    id_to_word = reverse_map(single_element_dict)
    assert id_to_word == ['a']

def test_reverse_map_multiple_elements():
    multiple_elements_dict = {'a': 1, 'b': 2, 'c': 0}
    id_to_word = reverse_map(multiple_elements_dict)