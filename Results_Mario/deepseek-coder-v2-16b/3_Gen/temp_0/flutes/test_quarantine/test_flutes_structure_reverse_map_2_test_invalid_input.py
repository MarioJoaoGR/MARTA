
import pytest
from typing import Dict, List, TypeVar

T = TypeVar('T')

def reverse_map(d: Dict[T, int]) -> List[T]:
    r"""Given a dictionary mapping ``item`` to ``id``, return a list where the ``id``-th element is ``item``.

    This function assumes that the ``id`` values form a permutation of indices. It sorts the items in the dictionary by their corresponding ids and returns them as a list.

    :param d: The dictionary mapping ``item`` to ``id``. The keys are the items, and the values are the corresponding ids.
    :return: A list where each element is an item from the input dictionary, ordered by its id.
    
    Examples:
        >>> words = ['a', 'aardvark', 'abandon', ...]
        >>> word_to_id = {word: idx for idx, word in enumerate(words)}
        >>> id_to_word = reverse_map(word_to_id)
        >>> print(words == id_to_word)  # This should return True if the lists are identical
    """
    return [k for k, _ in sorted(d.items(), key=lambda xs: xs[1])]

def test_invalid_input():
    none_input = None
    with pytest.raises(TypeError):
        reverse_map(none_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_reverse_map_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        none_input = None
        with pytest.raises(TypeError):
>           reverse_map(none_input)

flutes/Test4DT_tests/test_flutes_structure_reverse_map_2_test_invalid_input.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

d = None

    def reverse_map(d: Dict[T, int]) -> List[T]:
        r"""Given a dictionary mapping ``item`` to ``id``, return a list where the ``id``-th element is ``item``.
    
        This function assumes that the ``id`` values form a permutation of indices. It sorts the items in the dictionary by their corresponding ids and returns them as a list.
    
        :param d: The dictionary mapping ``item`` to ``id``. The keys are the items, and the values are the corresponding ids.
        :return: A list where each element is an item from the input dictionary, ordered by its id.
    
        Examples:
            >>> words = ['a', 'aardvark', 'abandon', ...]
            >>> word_to_id = {word: idx for idx, word in enumerate(words)}
            >>> id_to_word = reverse_map(word_to_id)
            >>> print(words == id_to_word)  # This should return True if the lists are identical
        """
>       return [k for k, _ in sorted(d.items(), key=lambda xs: xs[1])]
E       AttributeError: 'NoneType' object has no attribute 'items'

flutes/Test4DT_tests/test_flutes_structure_reverse_map_2_test_invalid_input.py:21: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_reverse_map_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""