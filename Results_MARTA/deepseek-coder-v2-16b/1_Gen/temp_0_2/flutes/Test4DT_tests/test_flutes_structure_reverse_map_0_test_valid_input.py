
import pytest
from typing import Dict, List, TypeVar

T = TypeVar('T')

def reverse_map(d: Dict[T, int]) -> List[T]:
    r"""Given a dictionary mapping ``item`` to ``id``, return a list where the ``id``-th element is ``item``.

    This function assumes that the ``id`` values form a permutation of the items in the dictionary. It sorts the items by their corresponding ``id`` and returns them as a list.

    :param d: The dictionary mapping ``item`` to ``id``. Each key (item) should be unique, and each value (id) should be an integer representing its position in the resulting list.
    :return: A list of items sorted by their corresponding ``id``.

    Examples:
        >>> words = ['a', 'aardvark', 'abandon', ...]
        >>> word_to_id = {word: idx for idx, word in enumerate(words)}
        >>> id_to_word = reverse_map(word_to_id)
        >>> print(words == id_to_word)  # This should output True if the ids form a permutation of the words.
    """
    return [k for k, _ in sorted(d.items(), key=lambda xs: xs[1])]

def test_valid_input():
    word_to_id = {'a': 0, 'b': 1, 'c': 2}
    expected_output = ['a', 'b', 'c']
    assert reverse_map(word_to_id) == expected_output
