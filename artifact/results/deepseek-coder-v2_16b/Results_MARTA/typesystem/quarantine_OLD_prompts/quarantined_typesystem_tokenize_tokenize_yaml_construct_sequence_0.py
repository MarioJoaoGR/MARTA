
import pytest
from typesystem.tokenize.tokenize_yaml import construct_sequence, ListToken
import yaml
from unittest.mock import patch

def test_construct_sequence():
    # Define a mock YAML content for testing
    yaml_content = """
    sequence:
      - item1
      - item2
      - item3
    """
    
    # Load the YAML content using PyYAML loader
    data = yaml.load(yaml_content, Loader=yaml.Loader)
    
    # Access the constructed ListToken object
    list_token = data['sequence']
    
    # Assert that the ListToken contains the expected values and indices
    assert list_token.value == ['item1', 'item2', 'item3']
    assert list_token.start == 14  # Assuming start index is provided correctly by PyYAML
    assert list_token.end == 30   # Assuming end index is calculated correctly

@pytest.mark.parametrize("yaml_content, expected_value, expected_start, expected_end", [
    (
        """sequence:
          - item1
          - item2
          - item3""",
        ['item1', 'item2', 'item3'],
        14,  # Assuming start index is provided correctly by PyYAML
        30   # Assuming end index is calculated correctly
    ),
    (
        """sequence:
          - value1
          - value2""",
        ['value1', 'value2'],
        14,  # Assuming start index is provided correctly by PyYAML
        26   # Assuming end index is calculated correctly
    )
])
def test_construct_sequence_parametrized(yaml_content, expected_value, expected_start, expected_end):
    data = yaml.load(yaml_content, Loader=yaml.Loader)
    list_token = data['sequence']
    
    # Assert that the ListToken contains the expected values and indices
    assert list_token.value == expected_value
    assert list_token.start == expected_start
    assert list_token.end == expected_end

def test_construct_sequence_with_custom_loader():
    class CustomSafeLoader(yaml.SafeLoader):
        pass
    
    # Define a mock YAML content for testing
    yaml_content = """
    sequence:
      - item1
      - item2
      - item3
    """
    
    # Load the YAML content using custom loader
    data = yaml.load(yaml_content, Loader=CustomSafeLoader)
    
    # Access the constructed ListToken object
    list_token = data['sequence']
    
    # Assert that the ListToken contains the expected values and indices
    assert list_token.value == ['item1', 'item2', 'item3']
    assert list_token.start == 14  # Assuming start index is provided correctly by PyYAML
    assert list_token.end == 30   # Assuming end index is calculated correctly

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
_ ERROR collecting test_typesystem_tokenize_tokenize_yaml_construct_sequence_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_construct_sequence_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_construct_sequence_0.py:3: in <module>
    from typesystem.tokenize.tokenize_yaml import construct_sequence, ListToken
E   ImportError: cannot import name 'construct_sequence' from 'typesystem.tokenize.tokenize_yaml' (/opt/marta/baselines/codamosa/replication/test-apps/typesystem/typesystem/tokenize/tokenize_yaml.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_tokenize_tokenize_yaml_construct_sequence_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.19s ===============================
"""