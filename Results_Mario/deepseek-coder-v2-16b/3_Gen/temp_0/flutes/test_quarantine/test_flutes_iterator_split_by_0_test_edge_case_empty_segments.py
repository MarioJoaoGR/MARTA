
import pytest
from typing import List, Iterable, Callable

def always_true(x: int) -> bool:
    return True

def split_by(iterable: Iterable[A], empty_segments: bool = False, *, criterion: Callable[[A], bool]) \
        -> Iterator[List[A]]:
    segments = []
    current_segment = []
    for item in iterable:
        if criterion(item):
            if current_segment or empty_segments:
                segments.append(current_segment)
                current_segment = []
        else:
            current_segment.append(item)
    if current_segment or empty_segments:
        segments.append(current_segment)
    return iter(segments)

def test_edge_case_empty_segments():
    iterable = [1, 2, 3]
    criterion = always_true
    
    result = list(split_by(iterable, empty_segments=True, criterion=criterion))
    expected = [[1], [], [2], [], [3], []]
    
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_split_by_0_test_edge_case_empty_segments
flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case_empty_segments.py:8:32: E0602: Undefined variable 'A' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case_empty_segments.py:8:90: E0602: Undefined variable 'A' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case_empty_segments.py:9:11: E0602: Undefined variable 'Iterator' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_split_by_0_test_edge_case_empty_segments.py:9:25: E0602: Undefined variable 'A' (undefined-variable)

"""