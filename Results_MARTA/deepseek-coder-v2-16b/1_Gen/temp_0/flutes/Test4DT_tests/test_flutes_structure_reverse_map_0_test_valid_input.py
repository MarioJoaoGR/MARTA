
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

@pytest.mark.parametrize("input_dict, expected", [
    ({'a': 0, 'b': 1, 'c': 2}, ['a', 'b', 'c']),
    ({'apple': 3, 'banana': 2, 'cherry': 1, 'date': 0}, ['date', 'cherry', 'banana', 'apple']),
    ({'one': 0, 'two': 1, 'three': 2}, ['one', 'two', 'three'])
])
def test_valid_input(input_dict: Dict[T, int], expected: List[T]):
    assert reverse_map(input_dict) == expected
