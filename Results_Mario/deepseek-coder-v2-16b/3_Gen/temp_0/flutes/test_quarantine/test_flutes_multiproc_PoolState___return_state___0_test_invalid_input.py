
import pytest
from flutes.multiproc import count_words_in_file
import collections

@pytest.mark.parametrize("invalid_path", [None, 123, True, [], {}])
def test_invalid_input(invalid_path):
    with pytest.raises(TypeError) as excinfo:
        count_words_in_file(invalid_path)
    assert "expected str, bytes or os.PathLike object" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolState___return_state___0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_PoolState___return_state___0_test_invalid_input.py:3:0: E0611: No name 'count_words_in_file' in module 'flutes.multiproc' (no-name-in-module)


"""