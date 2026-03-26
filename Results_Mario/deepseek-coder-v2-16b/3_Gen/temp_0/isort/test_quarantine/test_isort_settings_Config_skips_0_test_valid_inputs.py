
import pytest
from isort.settings import Config

def test_valid_inputs():
    valid_config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'buck-out', '.direnv', '.bzr', 'venv', '.pytype'}), format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
    assert isinstance(valid_config, Config)
    assert hasattr(valid_config, 'quiet')
    assert callable(getattr(valid_config, 'skips', None))

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

isort/Test4DT_tests/test_isort_settings_Config_skips_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
>       valid_config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'buck-out', '.direnv', '.bzr', 'venv', '.pytype'}), format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

isort/Test4DT_tests/test_isort_settings_Config_skips_0_test_valid_inputs.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:516: in __init__
    super().__init__(sources=tuple(sources), **combined_config)
<string>:105: in __init__
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.bzr', 'venv', '.pytype', '.direnv', 'buck-out'}),...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

    def __post_init__(self) -> None:
        py_version = self.py_version
        if py_version == "auto":  # pragma: no cover
            py_version = f"{sys.version_info.major}{sys.version_info.minor}"
    
        if py_version not in VALID_PY_TARGETS:
>           raise ValueError(
                f"The python version {py_version} is not supported. "
                "You can set a python version with the -py or --python-version flag. "
                f"The following versions are supported: {VALID_PY_TARGETS}"
            )
E           ValueError: The python version py3 is not supported. You can set a python version with the -py or --python-version flag. The following versions are supported: ('all', '2', '27', '3', '310', '311', '312', '313', '314', '36', '37', '38', '39')

isort/isort/settings.py:248: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_skips_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.15s ===============================
"""