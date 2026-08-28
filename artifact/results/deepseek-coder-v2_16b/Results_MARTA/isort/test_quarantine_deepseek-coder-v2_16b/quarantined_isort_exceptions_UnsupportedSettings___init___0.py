
import pytest
from isort.exceptions import UnsupportedSettings


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_UnsupportedSettings___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        unsupported_settings = {"foo": {"value": "bar", "source": "config"}}
        with pytest.raises(UnsupportedSettings) as exc_info:
            raise UnsupportedSettings(unsupported_settings)
>       assert str(exc_info.value) == (
            "isort was provided settings that it doesn't support:\n\n"
            "- foo = bar  (source: 'config')\n\n"
            "For a complete and up-to-date listing of supported settings see: https://pycqa.github.io/isort/docs/configuration/options/."
        )
E       AssertionError: assert 'isort was pr...n/options/.\n' == 'isort was pr...ion/options/.'
E         
E         Skipping 44 identical leading characters in diff, use -v to show
E           support:
E           
E         - - foo = bar  (source: 'config')
E         + 	- foo = bar  (source: 'config')
E         ? +...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_UnsupportedSettings___init___0.py:9: AssertionError
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(UnsupportedSettings) as exc_info:
>           raise UnsupportedSettings(None)

/opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_UnsupportedSettings___init___0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = UnsupportedSettings(None), unsupported_settings = None

    def __init__(self, unsupported_settings: Dict[str, Dict[str, str]]):
        errors = "\n".join(
>           self._format_option(name, **option) for name, option in unsupported_settings.items()
        )
E       AttributeError: 'NoneType' object has no attribute 'items'

/opt/marta/baselines/codamosa/replication/test-apps/isort/isort/exceptions.py:151: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_UnsupportedSettings___init___0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/isort/Test4DT_tests_deepseek-coder-v2_16b/test_isort_exceptions_UnsupportedSettings___init___0.py::test_none_input
============================== 2 failed in 0.08s ===============================
"""