
import pytest
from isort.settings import _get_config_data

@pytest.mark.parametrize("file_path, sections, expected_output", [
    ("invalid_path", ("section1",), {"error": "File not found"}),
    ("./tests/test_isort_settings__get_config_data_0_test_invalid_input.py", (), {"error": "Invalid file extension"})
])
def test_invalid_input(file_path, sections, expected_output):
    with pytest.raises(FileNotFoundError) as excinfo:
        _get_config_data(file_path, sections)
    assert str(excinfo.value) == expected_output["error"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________ test_invalid_input[invalid_path-sections0-expected_output0] __________

file_path = 'invalid_path', sections = ('section1',)
expected_output = {'error': 'File not found'}

    @pytest.mark.parametrize("file_path, sections, expected_output", [
        ("invalid_path", ("section1",), {"error": "File not found"}),
        ("./tests/test_isort_settings__get_config_data_0_test_invalid_input.py", (), {"error": "Invalid file extension"})
    ])
    def test_invalid_input(file_path, sections, expected_output):
>       with pytest.raises(FileNotFoundError) as excinfo:
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_input.py:10: Failed
_ test_invalid_input[./tests/test_isort_settings__get_config_data_0_test_invalid_input.py-sections1-expected_output1] _

file_path = './tests/test_isort_settings__get_config_data_0_test_invalid_input.py'
sections = (), expected_output = {'error': 'Invalid file extension'}

    @pytest.mark.parametrize("file_path, sections, expected_output", [
        ("invalid_path", ("section1",), {"error": "File not found"}),
        ("./tests/test_isort_settings__get_config_data_0_test_invalid_input.py", (), {"error": "Invalid file extension"})
    ])
    def test_invalid_input(file_path, sections, expected_output):
        with pytest.raises(FileNotFoundError) as excinfo:
            _get_config_data(file_path, sections)
>       assert str(excinfo.value) == expected_output["error"]
E       assert "[Errno 2] No...lid_input.py'" == 'Invalid file extension'
E         
E         - Invalid file extension
E         + [Errno 2] No such file or directory: './tests/test_isort_settings__get_config_data_0_test_invalid_input.py'

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_input.py::test_invalid_input[invalid_path-sections0-expected_output0]
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_input.py::test_invalid_input[./tests/test_isort_settings__get_config_data_0_test_invalid_input.py-sections1-expected_output1]
============================== 2 failed in 0.14s ===============================
"""