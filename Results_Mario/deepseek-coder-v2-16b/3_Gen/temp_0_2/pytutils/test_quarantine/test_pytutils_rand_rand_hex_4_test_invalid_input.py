
import pytest
from pytutils.rand import rand_hex

@pytest.mark.parametrize("invalid_input", ["string", 123.45, [], {}])
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
collected 4 items

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_4_test_invalid_input.py . [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_input[123.45] __________________________

invalid_input = 123.45

    @pytest.mark.parametrize("invalid_input", ["string", 123.45, [], {}])
    def test_invalid_input(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_4_test_invalid_input.py:7: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_pytutils_rand_rand_hex_4_test_invalid_input.py::test_invalid_input[123.45]
  /projects/F202407648IACDCF2/mario/pytutils/pytutils/rand.py:11: DeprecationWarning: non-integer arguments to randrange() have been deprecated since Python 3.10 and will be removed in a subsequent version
    return '%0{}x'.format(length) % random.randrange(16**length)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_4_test_invalid_input.py::test_invalid_input[123.45]
==================== 1 failed, 3 passed, 1 warning in 0.06s ====================
"""