
import pytest
from flutes.iterator import split_by

def test_invalid_input_none():
    with pytest.raises(TypeError):
        list(split_by(None))  # This should raise a TypeError since None is not an iterable

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_split_by_1_test_invalid_input_none.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        with pytest.raises(TypeError):
>           list(split_by(None))  # This should raise a TypeError since None is not an iterable

flutes/Test4DT_tests/test_flutes_iterator_split_by_1_test_invalid_input_none.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iterable = None, empty_segments = False

    def split_by(iterable: Iterable[A], empty_segments: bool = False, *, criterion=None, separator=None) \
            -> Iterator[List[A]]:
        r"""Split a list into sub-lists by dropping certain elements. Exactly one of ``criterion`` and ``separator`` must be
        specified. For example:
    
        .. code:: python
    
            >>> list(split_by(range(10), criterion=lambda x: x % 3 == 0))
            [[1, 2], [4, 5], [7, 8]]
    
            >>> list(split_by(" Split by: ", empty_segments=True, separator='.'))
            [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    
        :param iterable: The list to split.
        :param empty_segments: If ``True``, include an empty list in cases where two adjacent elements satisfy
            the criterion.
        :param criterion: The criterion to decide whether to drop an element.
        :param separator: The separator for sub-lists. An element is dropped if it is equal to ``parameter``.
        :return: List of sub-lists.
        """
        if not ((criterion is None) ^ (separator is None)):
>           raise ValueError("Exactly one of `criterion` and `separator` should be specified")
E           ValueError: Exactly one of `criterion` and `separator` should be specified

flutes/flutes/iterator.py:145: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_split_by_1_test_invalid_input_none.py::test_invalid_input_none
============================== 1 failed in 0.11s ===============================
"""