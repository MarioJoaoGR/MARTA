
import pytest

def readable_size(size: float, n_digits: int = 2) -> str:
    r"""Represent file size in human-readable format.

    This function converts a given file size in bytes to a more understandable unit (e.g., KB, MB) and formats it with the specified number of decimal places. It dynamically adjusts the unit based on the magnitude of the size input. The conversion stops at the largest appropriate unit for the given size.

    :param size: File size in bytes. This value should be a float or an integer representing the file size in bytes.
    :param n_digits: Number of digits to display after the decimal point for the formatted output. Defaults to 2.
    :returns: A string representing the human-readable file size with appropriate units.

    Examples:
        >>> readable_size(1024 * 1024)
        "1.00M"
        >>> readable_size(500000)
        "488.28K"
        >>> readable_size(123456789)
        "117.74M"
    """
    units = ["", "K", "M", "G", "T", "P"]
    for unit in units[:-1]:
        if size < 1024:
            return f"{size:.{n_digits}f}{unit}"
        size /= 1024
    return f"{size:.{n_digits}f}{units[-1]}"

def test_edge_cases():
    # Test None value
    assert readable_size(None) is None, "Expected None to be returned for None input"
    
    # Test negative values
    with pytest.raises(ValueError):
        readable_size(-1024)
    
    # Test very large numbers
    assert readable_size(1024**5) == "1.00P", "Expected P for the largest unit"

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

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None value
>       assert readable_size(None) is None, "Expected None to be returned for None input"

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_edge_cases.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

size = None, n_digits = 2

    def readable_size(size: float, n_digits: int = 2) -> str:
        r"""Represent file size in human-readable format.
    
        This function converts a given file size in bytes to a more understandable unit (e.g., KB, MB) and formats it with the specified number of decimal places. It dynamically adjusts the unit based on the magnitude of the size input. The conversion stops at the largest appropriate unit for the given size.
    
        :param size: File size in bytes. This value should be a float or an integer representing the file size in bytes.
        :param n_digits: Number of digits to display after the decimal point for the formatted output. Defaults to 2.
        :returns: A string representing the human-readable file size with appropriate units.
    
        Examples:
            >>> readable_size(1024 * 1024)
            "1.00M"
            >>> readable_size(500000)
            "488.28K"
            >>> readable_size(123456789)
            "117.74M"
        """
        units = ["", "K", "M", "G", "T", "P"]
        for unit in units[:-1]:
>           if size < 1024:
E           TypeError: '<' not supported between instances of 'NoneType' and 'int'

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_edge_cases.py:23: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""