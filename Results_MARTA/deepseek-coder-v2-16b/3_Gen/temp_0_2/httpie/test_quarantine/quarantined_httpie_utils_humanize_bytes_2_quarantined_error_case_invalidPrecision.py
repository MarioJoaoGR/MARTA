
import pytest
from httpie.utils import humanize_bytes

def test_error_case_invalidPrecision():
    with pytest.raises(TypeError):
        humanize_bytes(1024, precision="invalid")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_2_test_error_case_invalidPrecision.py F [100%]

=================================== FAILURES ===================================
_______________________ test_error_case_invalidPrecision _______________________

    def test_error_case_invalidPrecision():
        with pytest.raises(TypeError):
>           humanize_bytes(1024, precision="invalid")

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_2_test_error_case_invalidPrecision.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 1024, precision = 'invalid'

    def humanize_bytes(n, precision=2):
        # Author: Doug Latornell
        # Licence: MIT
        # URL: https://code.activestate.com/recipes/577081/
        """Return a humanized string representation of a number of bytes.
    
        >>> humanize_bytes(1)
        '1 B'
        >>> humanize_bytes(1024, precision=1)
        '1.0 kB'
        >>> humanize_bytes(1024 * 123, precision=1)
        '123.0 kB'
        >>> humanize_bytes(1024 * 12342, precision=1)
        '12.1 MB'
        >>> humanize_bytes(1024 * 12342, precision=2)
        '12.05 MB'
        >>> humanize_bytes(1024 * 1234, precision=2)
        '1.21 MB'
        >>> humanize_bytes(1024 * 1234 * 1111, precision=2)
        '1.31 GB'
        >>> humanize_bytes(1024 * 1234 * 1111, precision=1)
        '1.3 GB'
    
        """
        abbrevs = [
            (1 << 50, 'PB'),
            (1 << 40, 'TB'),
            (1 << 30, 'GB'),
            (1 << 20, 'MB'),
            (1 << 10, 'kB'),
            (1, 'B')
        ]
    
        if n == 1:
            return '1 B'
    
        for factor, suffix in abbrevs:
            if n >= factor:
                break
    
        # noinspection PyUnboundLocalVariable
>       return f'{n / factor:.{precision}f} {suffix}'
E       ValueError: Format specifier missing precision

httpie/httpie/utils.py:121: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_2_test_error_case_invalidPrecision.py::test_error_case_invalidPrecision
============================== 1 failed in 0.13s ===============================
"""