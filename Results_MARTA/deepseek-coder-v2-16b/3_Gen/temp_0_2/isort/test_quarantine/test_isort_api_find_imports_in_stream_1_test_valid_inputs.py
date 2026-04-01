
from io import StringIO
from pathlib import Path
from typing import TextIO, Iterator, Any
import pytest
from isort.api import find_imports_in_stream, Config, ImportKey, DEFAULT_CONFIG
import isort.identify as identify

@pytest.mark.parametrize("unique", [False, True, ImportKey.ALIAS, ImportKey.ATTRIBUTE, ImportKey.MODULE, ImportKey.PACKAGE])
def test_find_imports_in_stream(unique):
    code = """from module1 import thing1, thing2
from module2 import otherthing
from anothermodule import yetanotherthing"""
    
    input_stream = StringIO(code)
    config = Config()  # Assuming a default configuration is sufficient for this test.
    file_path = Path("testfile.py")

    imports = list(find_imports_in_stream(input_stream, config=config, file_path=file_path, unique=unique))
    
    expected_imports = [
        identify.Import(module="module1", attribute=None, alias=None),
        identify.Import(module="module2", attribute=None, alias=None),
        identify.Import(module="anothermodule", attribute=None, alias=None)
    ]
    
    if unique:
        seen = set()
        for imp in expected_imports:
            key = imp.statement() if isinstance(unique, bool) else getattr(imp, unique.name.lower())
            if key not in seen:
                seen.add(key)
                assert imp in imports
    else:
        assert len(expected_imports) == len(imports)
        for expected in expected_imports:
            assert any(expected == imp for imp in imports)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
______________________ test_find_imports_in_stream[False] ______________________

unique = False

    @pytest.mark.parametrize("unique", [False, True, ImportKey.ALIAS, ImportKey.ATTRIBUTE, ImportKey.MODULE, ImportKey.PACKAGE])
    def test_find_imports_in_stream(unique):
        code = """from module1 import thing1, thing2
    from module2 import otherthing
    from anothermodule import yetanotherthing"""
    
        input_stream = StringIO(code)
        config = Config()  # Assuming a default configuration is sufficient for this test.
        file_path = Path("testfile.py")
    
        imports = list(find_imports_in_stream(input_stream, config=config, file_path=file_path, unique=unique))
    
        expected_imports = [
>           identify.Import(module="module1", attribute=None, alias=None),
            identify.Import(module="module2", attribute=None, alias=None),
            identify.Import(module="anothermodule", attribute=None, alias=None)
        ]
E       TypeError: Import.__new__() missing 2 required positional arguments: 'line_number' and 'indented'

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py:22: TypeError
______________________ test_find_imports_in_stream[True] _______________________

unique = True

    @pytest.mark.parametrize("unique", [False, True, ImportKey.ALIAS, ImportKey.ATTRIBUTE, ImportKey.MODULE, ImportKey.PACKAGE])
    def test_find_imports_in_stream(unique):
        code = """from module1 import thing1, thing2
    from module2 import otherthing
    from anothermodule import yetanotherthing"""
    
        input_stream = StringIO(code)
        config = Config()  # Assuming a default configuration is sufficient for this test.
        file_path = Path("testfile.py")
    
        imports = list(find_imports_in_stream(input_stream, config=config, file_path=file_path, unique=unique))
    
        expected_imports = [
>           identify.Import(module="module1", attribute=None, alias=None),
            identify.Import(module="module2", attribute=None, alias=None),
            identify.Import(module="anothermodule", attribute=None, alias=None)
        ]
E       TypeError: Import.__new__() missing 2 required positional arguments: 'line_number' and 'indented'

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py:22: TypeError
_________________ test_find_imports_in_stream[ImportKey.ALIAS] _________________

unique = <ImportKey.ALIAS: 4>

    @pytest.mark.parametrize("unique", [False, True, ImportKey.ALIAS, ImportKey.ATTRIBUTE, ImportKey.MODULE, ImportKey.PACKAGE])
    def test_find_imports_in_stream(unique):
        code = """from module1 import thing1, thing2
    from module2 import otherthing
    from anothermodule import yetanotherthing"""
    
        input_stream = StringIO(code)
        config = Config()  # Assuming a default configuration is sufficient for this test.
        file_path = Path("testfile.py")
    
        imports = list(find_imports_in_stream(input_stream, config=config, file_path=file_path, unique=unique))
    
        expected_imports = [
>           identify.Import(module="module1", attribute=None, alias=None),
            identify.Import(module="module2", attribute=None, alias=None),
            identify.Import(module="anothermodule", attribute=None, alias=None)
        ]
E       TypeError: Import.__new__() missing 2 required positional arguments: 'line_number' and 'indented'

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py:22: TypeError
_______________ test_find_imports_in_stream[ImportKey.ATTRIBUTE] _______________

unique = <ImportKey.ATTRIBUTE: 3>

    @pytest.mark.parametrize("unique", [False, True, ImportKey.ALIAS, ImportKey.ATTRIBUTE, ImportKey.MODULE, ImportKey.PACKAGE])
    def test_find_imports_in_stream(unique):
        code = """from module1 import thing1, thing2
    from module2 import otherthing
    from anothermodule import yetanotherthing"""
    
        input_stream = StringIO(code)
        config = Config()  # Assuming a default configuration is sufficient for this test.
        file_path = Path("testfile.py")
    
        imports = list(find_imports_in_stream(input_stream, config=config, file_path=file_path, unique=unique))
    
        expected_imports = [
>           identify.Import(module="module1", attribute=None, alias=None),
            identify.Import(module="module2", attribute=None, alias=None),
            identify.Import(module="anothermodule", attribute=None, alias=None)
        ]
E       TypeError: Import.__new__() missing 2 required positional arguments: 'line_number' and 'indented'

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py:22: TypeError
________________ test_find_imports_in_stream[ImportKey.MODULE] _________________

unique = <ImportKey.MODULE: 2>

    @pytest.mark.parametrize("unique", [False, True, ImportKey.ALIAS, ImportKey.ATTRIBUTE, ImportKey.MODULE, ImportKey.PACKAGE])
    def test_find_imports_in_stream(unique):
        code = """from module1 import thing1, thing2
    from module2 import otherthing
    from anothermodule import yetanotherthing"""
    
        input_stream = StringIO(code)
        config = Config()  # Assuming a default configuration is sufficient for this test.
        file_path = Path("testfile.py")
    
        imports = list(find_imports_in_stream(input_stream, config=config, file_path=file_path, unique=unique))
    
        expected_imports = [
>           identify.Import(module="module1", attribute=None, alias=None),
            identify.Import(module="module2", attribute=None, alias=None),
            identify.Import(module="anothermodule", attribute=None, alias=None)
        ]
E       TypeError: Import.__new__() missing 2 required positional arguments: 'line_number' and 'indented'

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py:22: TypeError
________________ test_find_imports_in_stream[ImportKey.PACKAGE] ________________

unique = <ImportKey.PACKAGE: 1>

    @pytest.mark.parametrize("unique", [False, True, ImportKey.ALIAS, ImportKey.ATTRIBUTE, ImportKey.MODULE, ImportKey.PACKAGE])
    def test_find_imports_in_stream(unique):
        code = """from module1 import thing1, thing2
    from module2 import otherthing
    from anothermodule import yetanotherthing"""
    
        input_stream = StringIO(code)
        config = Config()  # Assuming a default configuration is sufficient for this test.
        file_path = Path("testfile.py")
    
        imports = list(find_imports_in_stream(input_stream, config=config, file_path=file_path, unique=unique))
    
        expected_imports = [
>           identify.Import(module="module1", attribute=None, alias=None),
            identify.Import(module="module2", attribute=None, alias=None),
            identify.Import(module="anothermodule", attribute=None, alias=None)
        ]
E       TypeError: Import.__new__() missing 2 required positional arguments: 'line_number' and 'indented'

isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py:22: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py::test_find_imports_in_stream[False]
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py::test_find_imports_in_stream[True]
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py::test_find_imports_in_stream[ImportKey.ALIAS]
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py::test_find_imports_in_stream[ImportKey.ATTRIBUTE]
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py::test_find_imports_in_stream[ImportKey.MODULE]
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_stream_1_test_valid_inputs.py::test_find_imports_in_stream[ImportKey.PACKAGE]
============================== 6 failed in 0.15s ===============================
"""