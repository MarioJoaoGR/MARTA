
from pathlib import Path
from typing import TextIO
from imports_parser import imports, Config, DEFAULT_CONFIG
import pytest

@pytest.mark.parametrize("file_content", [
    ("import os\nimport sys"),  # A simple valid case with two imports
    ("from math import pi\nimport os"),  # A case with a from and an import statement
    ("cimport numpy\nimport os")  # A case with cimport and import statements
])
def test_valid_case(file_content):
    """Test that the imports function correctly parses valid Python files."""
    file = TextIO(file_content)
    config = Config()
    result = list(imports(file, config=config))
    
    # Check if the number of results matches the expected number of import statements
    assert len(result) == file_content.count('\n') + 1  # Each line plus one for EOF

    # Check each import statement
    lines = file_content.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("import ") or line.startswith("from "):
            expected_import = line.strip().replace("\n", "")
            assert result[i].line == 1 + sum(line.count('\n') for j in range(i))
            assert result[i].raw == lines[i]
            if line.startswith("from "):
                parts = line.split()
                assert result[i].type == 'from'
                assert result[i].module == parts[1]
                if len(parts) > 2:
                    assert result[i].attribute == parts[2]
            else:
                assert result[i].type == 'straight'
                assert result[i].module == line.split()[1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_identify_imports_0_test_valid_case
isort/Test4DT_tests/test_isort_identify_imports_0_test_valid_case.py:4:0: E0401: Unable to import 'imports_parser' (import-error)


"""