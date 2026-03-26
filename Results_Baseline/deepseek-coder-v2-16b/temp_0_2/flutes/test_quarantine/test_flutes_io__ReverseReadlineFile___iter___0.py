
# Module: flutes.io
import io
from flutes.io import _ReverseReadlineFile

def test_reverse_readline_file():
    # Test with an actual file-like object and a custom generator
    def custom_generator():
        yield b'H'
        yield b'e'
        yield b'l'
        yield b'l'
        yield b'o'

    fp = io.BytesIO(b'Hello, World!')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator)

    # Read lines in reverse order
    assert reverse_readline.readline().decode('utf-8') == 'H'
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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___0.py F [100%]

=================================== FAILURES ===================================
__________________________ test_reverse_readline_file __________________________

    def test_reverse_readline_file():
        # Test with an actual file-like object and a custom generator
        def custom_generator():
            yield b'H'
            yield b'e'
            yield b'l'
            yield b'l'
            yield b'o'
    
        fp = io.BytesIO(b'Hello, World!')
        reverse_readline = _ReverseReadlineFile(fp, custom_generator)
    
        # Read lines in reverse order
>       assert reverse_readline.readline().decode('utf-8') == 'H'

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.io._ReverseReadlineFile object at 0x7f1b3a115f90>

    def readline(self):
>       return next(self.gen)
E       TypeError: 'function' object is not an iterator

flutes/flutes/io.py:232: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___iter___0.py::test_reverse_readline_file
============================== 1 failed in 0.10s ===============================
"""