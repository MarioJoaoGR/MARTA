
import pytest
from flutes.io import _ReverseReadlineFile

@pytest.fixture
def setup_reverse_readline():
    # Create a mock file object with lines in reverse order
    class MockFile:
        def __init__(self, content):
            self.content = content
            self.index = len(content) - 1
        
        def readline(self):
            if self.index >= 0:
                line = self.content[self.index]
                self.index -= 1
                return line
            else:
                raise StopIteration
    
    # Create a mock generator that yields lines in reverse order
    def mock_generator(fp):
        yield from reversed(list(fp))
    
    fp = MockFile(['line3\n', 'line2\n', 'line1\n'])
    reverse_readline = _ReverseReadlineFile(fp, mock_generator)
    return reverse_readline

def test_edge_case(setup_reverse_readline):
    reverse_readline = setup_reverse_readline
    lines = []
    for line in reverse_readline:
        lines.append(line.strip())
    assert lines == ['line3', 'line2', 'line1']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile_generator_2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

setup_reverse_readline = <flutes.io._ReverseReadlineFile object at 0x7fa1eb4a4590>

    def test_edge_case(setup_reverse_readline):
        reverse_readline = setup_reverse_readline
        lines = []
>       for line in reverse_readline:

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile_generator_2_test_edge_case.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.io._ReverseReadlineFile object at 0x7fa1eb4a4590>

    def __next__(self):
>       return next(self.gen) + '\n'
E       TypeError: 'function' object is not an iterator

flutes/flutes/io.py:223: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile_generator_2_test_edge_case.py::test_edge_case
============================== 1 failed in 0.11s ===============================
"""