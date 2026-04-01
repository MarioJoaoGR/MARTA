
import pytest
from typing import Dict, List, TypeVar

T = TypeVar('T')

def reverse_map(d: Dict[T, int]) -> List[T]:
    r"""Given a dictionary mapping ``item`` to ``id``, return a list where the ``id``-th element is ``item``.

    This function assumes that the ``id`` values form a permutation of indices. It sorts the items in the dictionary by their corresponding ids and returns them as a list.

    :param d: The dictionary mapping ``item`` to ``id``. The keys are the items, and the values are the corresponding ids.
    :return: A list where each element is an item from the input dictionary, ordered by its id.
    
    Examples:
        >>> words = ['a', 'aardvark', 'abandon']
        >>> word_to_id = {word: idx for idx, word in enumerate(words)}
        >>> id_to_word = reverse_map(word_to_id)
        >>> print(words == id_to_word)  # This should return True if the lists are identical
    """
    return [k for k, _ in sorted(d.items(), key=lambda xs: xs[1])]

@pytest.mark.parametrize("input_dict, expected", [
    ({'a': 0, 'b': 1, 'c': 2}, ['a', 'b', 'c']),
    ({'apple': 0, 'banana': 1, 'cherry': 2}, ['apple', 'banana', 'cherry']),
    ({'one': 0, 'two': 1, 'three': 2}, ['one', 'two', 'three'])
])
def test_valid_input(input_dict: Dict[T, int], expected: List[T]):
    assert reverse_map(input_dict) == expected
