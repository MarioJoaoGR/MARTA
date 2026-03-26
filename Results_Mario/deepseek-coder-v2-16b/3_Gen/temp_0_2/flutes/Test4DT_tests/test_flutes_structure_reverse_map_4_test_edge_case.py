
import pytest
from typing import Dict, List, TypeVar

T = TypeVar('T')

def reverse_map(d: Dict[T, int]) -> List[T]:
    r"""Given a dictionary mapping ``item`` to ``id``, return a list where the ``id``-th element is ``item``.

    This function assumes that the ``id`` values form a permutation of indices. It sorts the items in the dictionary by their corresponding ids and returns them as a list.

    :param d: The dictionary mapping ``item`` to ``id``. The keys (items) should be unique, and the values (ids) should be integers representing positions or indices.
    :return: A list of items sorted by their corresponding ids.

    Examples:
        >>> words = ['a', 'aardvark', 'abandon', ...]
        >>> word_to_id = {word: idx for idx, word in enumerate(words)}
        >>> id_to_word = reverse_map(word_to_id)
        >>> print(id_to_word == words)  # This will output True if the lists are identical.
    """
    return [k for k, _ in sorted(d.items(), key=lambda xs: xs[1])]

def test_edge_case():
    empty_dict = {}
    assert reverse_map(empty_dict) == []
