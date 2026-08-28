
import pytest
from thonny import ThonnyCompletion
from thonny.jedi_utils import _tweak_completions

# Test 1: Basic Usage
def test_tweak_completions_basic():
    completions = [
        ThonnyCompletion(name="foo", complete="bar=", type="type1", description="desc1", parent="parent1", full_name="full1"),
        ThonnyCompletion(name="baz", complete="qux=", type="type2", description="desc2", parent="parent2", full_name="full2")
    ]
    
    tweaked_completions = _tweak_completions(completions)
    
    assert len(tweaked_completions) == 2
    assert all(completion.name.endswith("=") for completion in tweaked_completions)
    assert tweaked_completions[0].name == "foo="
    assert tweaked_completions[1].name == "baz="

# Test 2: No Adjustment Needed
def test_tweak_completions_no_adjustment():
    completions = [
        ThonnyCompletion(name="foo=", complete="bar=", type="type1", description="desc1", parent="parent1", full_name="full1"),
        ThonnyCompletion(name="baz=", complete="qux=", type="type2", description="desc2", parent="parent2", full_name="full2")
    ]
    
    tweaked_completions = _tweak_completions(completions)
    
    assert len(tweaked_completions) == 2
    assert all(completion.name.endswith("=") for completion in tweaked_completions)
    assert tweaked_completions[0].name == "foo="
    assert tweaked_completions[1].name == "baz="

# Test 3: Edge Case: Empty List
def test_tweak_completions_empty_list():
    completions = []
    
    tweaked_completions = _tweak_completions(completions)
    
    assert len(tweaked_completions) == 0

# Test 4: Complex Usage with Different Types
def test_tweak_completions_complex():
    completions = [
        ThonnyCompletion(name="func1", complete="arg1=", type="function", description="description1", parent="module1", full_name="module1.func1"),
        ThonnyCompletion(name="var2", complete="value2=", type="variable", description="description2", parent="namespace2", full_name="namespace2.var2")
    ]
    
    tweaked_completions = _tweak_completions(completions)
    
    assert len(tweaked_completions) == 2
    assert all(completion.name.endswith("=") for completion in tweaked_completions)
    assert tweaked_completions[0].name == "func1"
    assert tweaked_completions[1].name == "var2="

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_thonny_jedi_utils__tweak_completions_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__tweak_completions_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__tweak_completions_0.py:3: in <module>
    from thonny import ThonnyCompletion
E   ImportError: cannot import name 'ThonnyCompletion' from 'thonny' (/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__tweak_completions_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""