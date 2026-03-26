
import io
from flutes.io import reverse_open, PathType

def test_reverse_open():
    with open('example.txt', 'w') as f:
        f.write("Line 3\nLine 2\nLine 1")
    
    gen = reverse_open(Path('example.txt'), encoding='utf-8', allow_empty_lines=True, buffer_size=io.DEFAULT_BUFFER_SIZE)
    lines = list(gen)
    
    expected_lines = ["Line 3", "Line 2", "Line 1"]
    
    assert lines == expected_lines

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io_reverse_open_0_test_edge_case
flutes/Test4DT_tests/test_flutes_io_reverse_open_0_test_edge_case.py:9:23: E0602: Undefined variable 'Path' (undefined-variable)


"""