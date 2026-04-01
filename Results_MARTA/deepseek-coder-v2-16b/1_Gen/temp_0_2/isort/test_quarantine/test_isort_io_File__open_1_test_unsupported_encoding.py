
import pytest
from pathlib import Path
from io import TextIOWrapper
from isort.io import File

@pytest.fixture
def file_path():
    return Path("example_file.txt")

def test_unsupported_encoding(tmp_path, monkeypatch):
    # Create a dummy file with an unsupported encoding
    content = "This is a test file."
    dummy_file = tmp_path / "dummy_file.txt"
    dummy_file.write_text(content, encoding="ascii")  # ASCII is supported, UTF-8 is not

    monkeypatch.setattr('builtins.open', lambda *args, **kwargs: open(dummy_file, 'rb'))

    with pytest.raises(Exception) as excinfo:
        File._open(dummy_file)
    
    assert "Unsupported" in str(excinfo.value)

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

isort/Test4DT_tests/test_isort_io_File__open_1_test_unsupported_encoding.py F [100%]

=================================== FAILURES ===================================
__________________________ test_unsupported_encoding ___________________________

tmp_path = PosixPath('/tmp/pytest-of-joaovitorino/pytest-7/test_unsupported_encoding0')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f5330903ad0>

    def test_unsupported_encoding(tmp_path, monkeypatch):
        # Create a dummy file with an unsupported encoding
        content = "This is a test file."
        dummy_file = tmp_path / "dummy_file.txt"
        dummy_file.write_text(content, encoding="ascii")  # ASCII is supported, UTF-8 is not
    
        monkeypatch.setattr('builtins.open', lambda *args, **kwargs: open(dummy_file, 'rb'))
    
        with pytest.raises(Exception) as excinfo:
            File._open(dummy_file)
    
>       assert "Unsupported" in str(excinfo.value)
E       AssertionError: assert 'Unsupported' in 'maximum recursion depth exceeded'
E        +  where 'maximum recursion depth exceeded' = str(RecursionError('maximum recursion depth exceeded'))
E        +    where RecursionError('maximum recursion depth exceeded') = <ExceptionInfo RecursionError('maximum recursion depth exceeded') tblen=962>.value

isort/Test4DT_tests/test_isort_io_File__open_1_test_unsupported_encoding.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_io_File__open_1_test_unsupported_encoding.py::test_unsupported_encoding
============================== 1 failed in 0.12s ===============================
"""