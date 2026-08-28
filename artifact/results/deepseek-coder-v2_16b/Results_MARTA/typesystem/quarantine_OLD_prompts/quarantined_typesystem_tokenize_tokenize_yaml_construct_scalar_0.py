
import pytest
from typesystem.tokenize.tokenize_yaml import construct_scalar, ScalarToken
import yaml

def test_construct_scalar():
    # Sample YAML content as a string
    yaml_content = """
    name: John Doe
    age: 30
    email: john.doe@example.com
    """
    
    # Create a custom SafeLoader instance with the YAML content
    loader = yaml.SafeLoader(yaml_content)
    
    # Get the root node of the YAML document
    node = next(loader.get_nodes())
    
    # Call the construct_scalar function to create a ScalarToken object
    scalar_token = construct_scalar(loader, node)
    
    # Assert that the extracted value matches the expected result
    assert scalar_token.value == "John Doe"
    assert scalar_token.start == 7  # Assuming start index is provided correctly by YAML library
    assert scalar_token.end == 13  # Adjusted end index to match the length of the name string

# Add more test cases if needed, following the same pattern

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_typesystem_tokenize_tokenize_yaml_construct_scalar_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_construct_scalar_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_construct_scalar_0.py:3: in <module>
    from typesystem.tokenize.tokenize_yaml import construct_scalar, ScalarToken
E   ImportError: cannot import name 'construct_scalar' from 'typesystem.tokenize.tokenize_yaml' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/tokenize/tokenize_yaml.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_construct_scalar_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.27s ===============================
"""