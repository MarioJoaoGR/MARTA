
import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_yaml_constructor_AnsibleConstructor_construct_mapping_0.py F [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_input_non_mapping_node ______________________

    def test_invalid_input_non_mapping_node():
        constructor = AnsibleConstructor()
        with pytest.raises(Exception) as excinfo:
            non_mapping_node = "not a mapping node"
            constructor.construct_mapping(non_mapping_node)
>       assert str(excinfo.value).startswith("expected a mapping node, but found")
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7f7d6a4440f0>('expected a mapping node, but found')
E        +    where <built-in method startswith of str object at 0x7f7d6a4440f0> = "'str' object has no attribute 'id'".startswith
E        +      where "'str' object has no attribute 'id'" = str(AttributeError("'str' object has no attribute 'id'"))
E        +        where AttributeError("'str' object has no attribute 'id'") = <ExceptionInfo AttributeError("'str' object has no attribute 'id'") tblen=2>.value

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_yaml_constructor_AnsibleConstructor_construct_mapping_0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_yaml_constructor_AnsibleConstructor_construct_mapping_0.py::test_invalid_input_non_mapping_node
============================== 1 failed in 0.56s ===============================
"""