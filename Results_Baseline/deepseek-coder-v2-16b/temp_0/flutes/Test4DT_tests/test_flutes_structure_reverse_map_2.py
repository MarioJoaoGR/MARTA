
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
    assert words == id_to_word, f"Expected {words}, but got {id_to_word}"

def test_reverse_map_empty():
    empty_dict = {}
    id_to_word = reverse_map(empty_dict)
    assert [] == id_to_word, f"Expected [], but got {id_to_word}"

def test_reverse_map_single_element():
    single_dict = {'a': 0}
    id_to_word = reverse_map(single_dict)
    assert ['a'] == id_to_word, f"Expected ['a'], but got {id_to_word}"

def test_reverse_map_negative_ids():
    words = ['a', 'b', 'c']
    word_to_id = {word: -idx for idx, word in enumerate(words)}
    id_to_word = reverse_map(word_to_id)
    assert ['c', 'b', 'a'] == id_to_word, f"Expected ['c', 'b', 'a'], but got {id_to_word}"

def test_reverse_map_mixed_ids():
    words = ['a', 'b', 'c']
    word_to_id = {'a': 2, 'b': 0, 'c': 1}
    id_to_word = reverse_map(word_to_id)
    assert ['b', 'c', 'a'] == id_to_word, f"Expected ['b', 'c', 'a'], but got {id_to_word}"

def test_reverse_map_large_ids():
    words = ['a', 'b', 'c']
    word_to_id = {'a': 100, 'b': -1, 'c': 2}
    id_to_word = reverse_map(word_to_id)
    assert ['b', 'c', 'a'] == id_to_word, f"Expected ['b', 'c', 'a'], but got {id_to_word}"
