
import pytest
from typing import Dict
import html.entities

def _build_unicode_map() -> Dict[str, str]:
    """
    Builds a mapping from HTML entity names to their corresponding Unicode characters.

    This function iterates over the `html.entities.name2codepoint` dictionary, which contains mappings of HTML entity names (e.g., 'nbsp', 'copy') to their respective Unicode code points. It converts these code points to characters and constructs a dictionary where keys are the entity names and values are the corresponding Unicode characters.

    Returns:
        Dict[str, str]: A dictionary with HTML entity names as keys and their corresponding Unicode characters as values.

    Example:
        >>> unicode_map = _build_unicode_map()
        >>> print(unicode_map['nbsp'])  # Outputs the Unicode character for the 'nbsp' entity
        '\u00a0'
        >>> print(unicode_map['copy'])  # Outputs the Unicode character for the 'copy' entity
        '\u00a9'
    """
    unicode_map = {}
    for name, value in html.entities.name2codepoint.items():
        unicode_map[name] = chr(value)
    return unicode_map

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape__build_unicode_map_0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_empty_dict_handling ___________________________

    def test_empty_dict_handling():
        unicode_map = {}
        with pytest.raises(KeyError):
>           unicode_map[next(iter(unicode_map))]
E           StopIteration

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape__build_unicode_map_0.py:30: StopIteration
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape__build_unicode_map_0.py::test_empty_dict_handling
============================== 1 failed in 0.09s ===============================
"""