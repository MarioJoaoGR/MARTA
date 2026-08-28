
import pytest
from typing import Dict, List, TypeVar

T = TypeVar('T')

def reverse_map(d: Dict[T, int]) -> List[T]:
    r"""Given a dict containing pairs of ``(item, id)``, return a list where the ``id``-th element is ``item``.

    .. note::
        It is assumed that the ``id``\ s form a permutation.

    .. code:: python

        >>> words = ['a', 'aardvark', 'abandon', ...]
        >>> word_to_id = {word: idx for idx, word in enumerate(words)}
        >>> id_to_word = reverse_map(word_to_id)
        >>> (words == id_to_word)
        True

    :param d: The dictionary mapping ``item`` to ``id``.
    """
    return [k for k, _ in sorted(d.items(), key=lambda xs: xs[1])]

# Test cases
def test_valid_input():
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {'a': 0, 'aardvark': 1, 'abandon': 2}
    id_to_word = reverse_map(word_to_id)
    assert words == id_to_word

def test_empty_input():
    empty_dict = {}
    id_to_word = reverse_map(empty_dict)
    assert id_to_word == []

def test_invalid_input():
    invalid_dict = {'a': 0, 'b': 'not an int', 'c': 2}
    with pytest.raises(TypeError):
        reverse_map(invalid_dict)
