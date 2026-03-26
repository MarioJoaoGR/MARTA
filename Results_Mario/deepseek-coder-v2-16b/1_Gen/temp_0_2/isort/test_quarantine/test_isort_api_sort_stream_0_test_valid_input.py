
import pytest
from isort.api import Config, DEFAULT_CONFIG

@pytest.fixture
def mock_config():
    return Config(
        py_version='py3',
        force_to_top=frozenset(),
        skip=frozenset({'build', '.nox', 'buck-out', 'dist', 'node_modules'}),
        format_success='{success}: {message}',
        sort_order='natural',
        sort_reexports=False,
        split_on_trailing_comma=False
    )

def test_valid_input(mock_config):
    # Since we cannot modify the frozen instance directly, we need to create a new instance with the desired configuration.
    modified_config = Config(**{**vars(mock_config), 'atomic': False})
    
    # Add assertions here to verify that the modified_config has the expected attributes and values.
    assert modified_config.py_version == 'py3'
    assert modified_config.force_to_top == frozenset()
    assert modified_config.skip == frozenset({'build', '.nox', 'buck-out', 'dist', 'node_modules'})
    assert modified_config.format_success == '{success}: {message}'
    assert modified_config.sort_order == 'natural'
    assert modified_config.sort_reexports is False
    assert modified_config.split_on_trailing_comma is False
    assert not modified_config.atomic

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

isort/Test4DT_tests/test_isort_api_sort_stream_0_test_valid_input.py E   [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture
    def mock_config():
>       return Config(
            py_version='py3',
            force_to_top=frozenset(),
            skip=frozenset({'build', '.nox', 'buck-out', 'dist', 'node_modules'}),
            format_success='{success}: {message}',
            sort_order='natural',
            sort_reexports=False,
            split_on_trailing_comma=False
        )

isort/Test4DT_tests/test_isort_api_sort_stream_0_test_valid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/settings.py:516: in __init__
    super().__init__(sources=tuple(sources), **combined_config)
<string>:105: in __init__
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'dist', 'node_modules', '.nox', 'build', 'buck-out'...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

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
ERROR isort/Test4DT_tests/test_isort_api_sort_stream_0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.12s ===============================
"""