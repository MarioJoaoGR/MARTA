
import pytest
from io import StringIO
from pathlib import Path
from isort.api import check_stream, Config, DEFAULT_CONFIG

@pytest.fixture
def setup():
    config = Config(py_version='3', sort_reexports=False, split_on_trailing_comma=False)
    return config

def test_valid_input(setup):
    input_stream = StringIO("import os\nimport sys")
    result = check_stream(input_stream, config=setup, file_path=Path('test.py'))
    assert result is True

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

isort/Test4DT_tests/test_isort_api_check_stream_0_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

setup = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.pants.d', '.nox', '.hg', '.venv', '.tox', '.mypy_...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)

    def test_valid_input(setup):
        input_stream = StringIO("import os\nimport sys")
>       result = check_stream(input_stream, config=setup, file_path=Path('test.py'))

isort/Test4DT_tests/test_isort_api_check_stream_0_test_valid_input.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/api.py:267: in check_stream
    changed: bool = sort_stream(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_stream = <_io.StringIO object at 0x7f4a2b3879a0>
output_stream = <isort.io._EmptyIO object at 0x7f4a2b359120>, extension = 'py'
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.pants.d', '.nox', '.hg', '.venv', '.tox', '.mypy_...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
file_path = PosixPath('test.py'), disregard_skip = False, show_diff = False
raise_on_skip = True, config_kwargs = {}, content_source = 'test.py'

    def sort_stream(
        input_stream: TextIO,
        output_stream: TextIO,
        extension: str | None = None,
        config: Config = DEFAULT_CONFIG,
        file_path: Path | None = None,
        disregard_skip: bool = False,
        show_diff: bool | TextIO = False,
        raise_on_skip: bool = True,
        **config_kwargs: Any,
    ) -> bool:
        """Sorts any imports within the provided code stream, outputs to the provided output stream.
         Returns `True` if anything is modified from the original input stream, otherwise `False`.
    
        - **input_stream**: The stream of code with imports that need to be sorted.
        - **output_stream**: The stream where sorted imports should be written to.
        - **extension**: The file extension that contains imports. Defaults to filename extension or py.
        - **config**: The config object to use when sorting imports.
        - **file_path**: The disk location where the code string was pulled from.
        - **disregard_skip**: set to `True` if you want to ignore a skip set in config for this file.
        - **show_diff**: If `True` the changes that need to be done will be printed to stdout, if a
        TextIO stream is provided results will be written to it, otherwise no diff will be computed.
        - ****config_kwargs**: Any config modifications.
        """
        extension = extension or (file_path and file_path.suffix.lstrip(".")) or "py"
        if show_diff:
            _output_stream = StringIO()
            _input_stream = StringIO(input_stream.read())
            changed = sort_stream(
                input_stream=_input_stream,
                output_stream=_output_stream,
                extension=extension,
                config=config,
                file_path=file_path,
                disregard_skip=disregard_skip,
                raise_on_skip=raise_on_skip,
                **config_kwargs,
            )
            _output_stream.seek(0)
            _input_stream.seek(0)
            show_unified_diff(
                file_input=_input_stream.read(),
                file_output=_output_stream.read(),
                file_path=file_path,
                output=output_stream if show_diff is True else show_diff,
                color_output=config.color_output,
            )
            return changed
    
        config = _config(path=file_path, config=config, **config_kwargs)
        content_source = str(file_path or "Passed in content")
        if not disregard_skip and file_path and config.is_skipped(file_path):
>           raise FileSkipSetting(content_source)
E           isort.exceptions.FileSkipSetting: test.py was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting

isort/isort/api.py:190: FileSkipSetting
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_check_stream_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.11s ===============================
"""