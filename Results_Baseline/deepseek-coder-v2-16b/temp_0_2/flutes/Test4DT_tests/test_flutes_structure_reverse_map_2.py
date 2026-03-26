
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
    word_to_id = {'a': 0, 'aardvark': 1, 'abandon': 2}
    id_to_word = reverse_map(word_to_id)
    assert id_to_word == ['a', 'aardvark', 'abandon']

def test_reverse_map_list():
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {word: idx for idx, word in enumerate(words)}
    id_to_word = reverse_map(word_to_id)
    assert id_to_word == ['a', 'aardvark', 'abandon']

def test_reverse_map_empty():
    empty_dict = {}
    empty_list = reverse_map(empty_dict)
    assert empty_list == []

def test_reverse_map_large():
    large_words = [f'word{i}' for i in range(10000)]
    large_word_to_id = {word: idx for idx, word in enumerate(large_words)}
    large_id_to_word = reverse_map(large_word_to_id)