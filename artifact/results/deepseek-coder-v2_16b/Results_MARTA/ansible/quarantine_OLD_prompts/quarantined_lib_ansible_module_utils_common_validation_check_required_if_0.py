
import pytest
from ansible.module_utils.common.validation import check_required_if




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________ test_check_required_if_all_requirements_present ________________

    def test_check_required_if_all_requirements_present():
        requirements = [['state', 'present', ('path',)], ['someint', 99, ('bool_param', 'string_param')]]
        parameters = {'state': 'present', 'someint': 99}
>       assert check_required_if(requirements, parameters) == []

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

requirements = ('bool_param', 'string_param')
parameters = {'someint': 99, 'state': 'present'}, options_context = None

    def check_required_if(requirements, parameters, options_context=None):
        """Check parameters that are conditionally required
    
        Raises :class:`TypeError` if the check fails
    
        :arg requirements: List of lists specifying a parameter, value, parameters
            required when the given parameter is the specified value, and optionally
            a boolean indicating any or all parameters are required.
    
        :Example:
    
        .. code-block:: python
    
            required_if=[
                ['state', 'present', ('path',), True],
                ['someint', 99, ('bool_param', 'string_param')],
            ]
    
        :arg parameters: Dictionary of parameters
    
        :returns: Empty list or raises :class:`TypeError` if the check fails.
            The results attribute of the exception contains a list of dictionaries.
            Each dictionary is the result of evaluating each item in requirements.
            Each return dictionary contains the following keys:
    
                :key missing: List of parameters that are required but missing
                :key requires: 'any' or 'all'
                :key parameter: Parameter name that has the requirement
                :key value: Original value of the parameter
                :key requirements: Original required parameters
    
            :Example:
    
            .. code-block:: python
    
                [
                    {
                        'parameter': 'someint',
                        'value': 99
                        'requirements': ('bool_param', 'string_param'),
                        'missing': ['string_param'],
                        'requires': 'all',
                    }
                ]
    
        :kwarg options_context: List of strings of parent key names if ``requirements`` are
            in a sub spec.
        """
        results = []
        if requirements is None:
            return results
    
        for req in requirements:
            missing = {}
            missing['missing'] = []
            max_missing_count = 0
            is_one_of = False
            if len(req) == 4:
                key, val, requirements, is_one_of = req
            else:
                key, val, requirements = req
    
            # is_one_of is True at least one requirement should be
            # present, else all requirements should be present.
            if is_one_of:
                max_missing_count = len(requirements)
                missing['requires'] = 'any'
            else:
                missing['requires'] = 'all'
    
            if key in parameters and parameters[key] == val:
                for check in requirements:
                    count = count_terms(check, parameters)
                    if count == 0:
                        missing['missing'].append(check)
            if len(missing['missing']) and len(missing['missing']) >= max_missing_count:
                missing['parameter'] = key
                missing['value'] = val
                missing['requirements'] = requirements
                results.append(missing)
    
        if results:
            for missing in results:
                msg = "%s is %s but %s of the following are missing: %s" % (
                    missing['parameter'], missing['value'], missing['requires'], ', '.join(missing['missing']))
                if options_context:
                    msg = "{0} found in {1}".format(msg, " -> ".join(options_context))
>               raise TypeError(to_native(msg))
E               TypeError: state is present but all of the following are missing: path

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/common/validation.py:333: TypeError
________________ test_check_required_if_missing_one_requirement ________________

    def test_check_required_if_missing_one_requirement():
        requirements = [['state', 'present', ('path',)], ['someint', 99, ('bool_param', 'string_param')]]
        parameters = {'state': 'present'}
        with pytest.raises(TypeError) as excinfo:
            check_required_if(requirements, parameters)
>       assert str(excinfo.value) == "state is present but all of the following are missing: path, bool_param"
E       AssertionError: assert 'state is pre...missing: path' == 'state is pre...h, bool_param'
E         
E         Skipping 48 identical leading characters in diff, use -v to show
E         - ssing: path, bool_param
E         + ssing: path

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py:15: AssertionError
_______________ test_check_required_if_missing_all_requirements ________________

    def test_check_required_if_missing_all_requirements():
        requirements = [['state', 'present', ('path',)], ['someint', 99, ('bool_param', 'string_param')]]
        parameters = {'state': 'absent'}
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py:20: Failed
__________________ test_check_required_if_one_of_requirements __________________

    def test_check_required_if_one_of_requirements():
        requirements = [['state', 'present', ('path',)], ['someint', 99, ('bool_param', 'string_param')]]
        parameters = {'state': 'present', 'someint': 100}
        with pytest.raises(TypeError) as excinfo:
            check_required_if(requirements, parameters)
>       assert str(excinfo.value) == "state is present but any of the following are missing: path, bool_param"
E       AssertionError: assert 'state is pre...missing: path' == 'state is pre...h, bool_param'
E         
E         - state is present but any of the following are missing: path, bool_param
E         ?                       ^^                                   ------------
E         + state is present but all of the following are missing: path
E         ?                       ^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py::test_check_required_if_all_requirements_present
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py::test_check_required_if_missing_one_requirement
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py::test_check_required_if_missing_all_requirements
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_if_0.py::test_check_required_if_one_of_requirements
============================== 4 failed in 0.31s ===============================
"""