
import pytest
from pytutils.rand import rand_hex

@pytest.mark.parametrize("invalid_input", [None, "string", -5])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        rand_hex(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_2_test_invalid_input.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_input[-5] ____________________________

self = <random.Random object at 0x5627f12d0e50>, start = 9.5367431640625e-07
stop = None, step = 1

    def randrange(self, start, stop=None, step=_ONE):
        """Choose a random item from range(stop) or range(start, stop[, step]).
    
        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.
    
        """
    
        # This code is a bit messy to make it fast for the
        # common case while still doing adequate error checking.
        try:
>           istart = _index(start)
E           TypeError: 'float' object cannot be interpreted as an integer

/usr/local/lib/python3.11/random.py:295: TypeError

During handling of the above exception, another exception occurred:

invalid_input = -5

    @pytest.mark.parametrize("invalid_input", [None, "string", -5])
    def test_invalid_input(invalid_input):
        with pytest.raises(TypeError):
>           rand_hex(invalid_input)

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_2_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/rand.py:11: in rand_hex
    return '%0{}x'.format(length) % random.randrange(16**length)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <random.Random object at 0x5627f12d0e50>, start = 9.5367431640625e-07
stop = None, step = 1

    def randrange(self, start, stop=None, step=_ONE):
        """Choose a random item from range(stop) or range(start, stop[, step]).
    
        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.
    
        """
    
        # This code is a bit messy to make it fast for the
        # common case while still doing adequate error checking.
        try:
            istart = _index(start)
        except TypeError:
            istart = int(start)
            if istart != start:
                _warn('randrange() will raise TypeError in the future',
                      DeprecationWarning, 2)
>               raise ValueError("non-integer arg 1 for randrange()")
E               ValueError: non-integer arg 1 for randrange()

/usr/local/lib/python3.11/random.py:301: ValueError
=============================== warnings summary ===============================
Test4DT_tests/test_pytutils_rand_rand_hex_2_test_invalid_input.py::test_invalid_input[-5]
  /projects/F202407648IACDCF2/mario/pytutils/pytutils/rand.py:11: DeprecationWarning: randrange() will raise TypeError in the future
    return '%0{}x'.format(length) % random.randrange(16**length)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_2_test_invalid_input.py::test_invalid_input[-5]
==================== 1 failed, 2 passed, 1 warning in 0.07s ====================
"""