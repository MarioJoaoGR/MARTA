
import pytest
from isort.exceptions import UnsupportedSettings

def test_valid_input():
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings({
            "settings_name": {"value": "setting_value", "source": "config_file"}
        })
    
    assert str(exc_info.value) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- settings_name = setting_value  (source: 'config_file')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options."
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings__format_option_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with pytest.raises(UnsupportedSettings) as exc_info:
            raise UnsupportedSettings({
                "settings_name": {"value": "setting_value", "source": "config_file"}
            })
    
>       assert str(exc_info.value) == (
            "isort was provided settings that it doesn't support:\n\n"
            "\t- settings_name = setting_value  (source: 'config_file')\n\n"
            "For a complete and up-to-date listing of supported settings see: "
            "https://pycqa.github.io/isort/docs/configuration/options."
        )
E       AssertionError: assert 'isort was pr...on/options.\n' == 'isort was pr...tion/options.'
E         
E         Skipping 224 identical leading characters in diff, use -v to show
E         - on/options.
E         + on/options.
E         ?            +

isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings__format_option_0_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings__format_option_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""