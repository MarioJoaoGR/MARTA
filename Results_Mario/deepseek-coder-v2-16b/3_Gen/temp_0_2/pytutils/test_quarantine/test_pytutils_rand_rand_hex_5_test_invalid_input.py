
import pytest
from pytutils.rand import rand_hex
import random

@pytest.mark.parametrize("invalid_input", ["string", True, [], {}, None])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        rand_hex(length=invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_5_test_invalid_input.py . [ 20%]
F...                                                                     [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input[True] ___________________________

invalid_input = True

    @pytest.mark.parametrize("invalid_input", ["string", True, [], {}, None])
    def test_invalid_input(invalid_input):
        with pytest.raises(TypeError):
>           rand_hex(length=invalid_input)

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_5_test_invalid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

length = True

    def rand_hex(length=8):
        """
        Create a random hex string of a specific length performantly.
    
        :param int length: length of hex string to generate
        :return: random hex string
        """
>       return '%0{}x'.format(length) % random.randrange(16**length)
E       ValueError: unsupported format character 'T' (0x54) at index 2

pytutils/pytutils/rand.py:11: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_5_test_invalid_input.py::test_invalid_input[True]
========================= 1 failed, 4 passed in 0.08s ==========================
"""