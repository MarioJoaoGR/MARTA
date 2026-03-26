
import pytest
from flutes.multiproc import count_words_in_file
import collections

@pytest.mark.parametrize("path, expected", [
    ("/path/to/yourfile.txt", collections.Counter({'word': 10})),
    (None, collections.Counter())
])
def test_count_words_in_file(path, expected):
    result = count_words_in_file(path)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolState___return_state___0_test_none_input
flutes/Test4DT_tests/test_flutes_multiproc_PoolState___return_state___0_test_none_input.py:3:0: E0611: No name 'count_words_in_file' in module 'flutes.multiproc' (no-name-in-module)


"""