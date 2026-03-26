
import toml
from isort._vendored.tomli._parser import NestedDict, Key

def test_valid_input_happy_path():
    nd = NestedDict()
    toml_content = '''
    [section1]
    key1 = "value1"
    [section2]
    key2 = "value2"
    '''
    nd.dict = toml.loads(toml_content)

    # Test getting an existing nested dictionary
    assert nd.get_or_create_nest(['section1']) == {'key1': 'value1'}

    # Test creating a new nested dictionary
    assert nd.get_or_create_nest(['new_section']) == {}

    # Test accessing an existing key in the nested structure
    assert nd.get_or_create_nest(['section2', 'key2']) == 'value2'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        nd = NestedDict()
        toml_content = '''
        [section1]
        key1 = "value1"
        [section2]
        key2 = "value2"
        '''
        nd.dict = toml.loads(toml_content)
    
        # Test getting an existing nested dictionary
        assert nd.get_or_create_nest(['section1']) == {'key1': 'value1'}
    
        # Test creating a new nested dictionary
        assert nd.get_or_create_nest(['new_section']) == {}
    
        # Test accessing an existing key in the nested structure
>       assert nd.get_or_create_nest(['section2', 'key2']) == 'value2'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_valid_input_happy_path.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <isort._vendored.tomli._parser.NestedDict object at 0x7ff6a14daa90>
key = ['section2', 'key2']

    def get_or_create_nest(
        self,
        key: Key,
        *,
        access_lists: bool = True,
    ) -> dict:
        cont: Any = self.dict
        for k in key:
            if k not in cont:
                cont[k] = {}
            cont = cont[k]
            if access_lists and isinstance(cont, list):
                cont = cont[-1]
            if not isinstance(cont, dict):
>               raise KeyError("There is no nest behind this key")
E               KeyError: 'There is no nest behind this key'

isort/isort/_vendored/tomli/_parser.py:212: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.11s ===============================
"""