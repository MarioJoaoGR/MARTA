
import pytest
from dataclasses_json.utils import _hasargs
from typing import List, Tuple, Set

def test_valid_input():
    assert _hasargs(List[int, str], 'int', 'str') == True
    assert _hasargs(Tuple[int, str], 'int', 'str') == True
    assert _hasargs(Set[int, str], 'int', 'str') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       assert _hasargs(List[int, str], 'int', 'str') == True

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/typing.py:312: in inner
    return func(*args, **kwds)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/typing.py:1144: in __getitem__
    _check_generic(self, params, self._nparams)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = typing.List, parameters = (<class 'int'>, <class 'str'>), elen = 1

    def _check_generic(cls, parameters, elen=_marker):
        """Check correct count for parameters of a generic cls (internal helper).
    
        This gives a nice error message in case of count mismatch.
        """
        # If substituting a single ParamSpec with multiple arguments
        # we do not check the count
        if (inspect.isclass(cls) and issubclass(cls, typing.Generic)
            and len(cls.__parameters__) == 1
            and isinstance(cls.__parameters__[0], ParamSpec)
            and parameters
            and not _is_param_expr(parameters[0])
        ):
            # Generic modifies parameters variable, but here we cannot do this
            return
    
        if not elen:
            raise TypeError(f"{cls} is not a generic class")
        if elen is _marker:
            if not hasattr(cls, "__parameters__") or not cls.__parameters__:
                raise TypeError(f"{cls} is not a generic class")
            elen = len(cls.__parameters__)
        alen = len(parameters)
        if alen != elen:
            expect_val = elen
            if hasattr(cls, "__parameters__"):
                parameters = [p for p in cls.__parameters__ if not _is_unpack(p)]
                num_tv_tuples = sum(isinstance(p, TypeVarTuple) for p in parameters)
                if (num_tv_tuples > 0) and (alen >= elen - num_tv_tuples):
                    return
    
                # deal with TypeVarLike defaults
                # required TypeVarLikes cannot appear after a defaulted one.
                if alen < elen:
                    # since we validate TypeVarLike default in _collect_type_vars
                    # or _collect_parameters we can safely check parameters[alen]
                    if (
                        getattr(parameters[alen], '__default__', NoDefault)
                        is not NoDefault
                    ):
                        return
    
                    num_default_tv = sum(getattr(p, '__default__', NoDefault)
                                         is not NoDefault for p in parameters)
    
                    elen -= num_default_tv
    
                    expect_val = f"at least {elen}"
    
            # Breakpoint: https://github.com/python/cpython/pull/27515
            things = "arguments" if sys.version_info >= (3, 10) else "parameters"
>           raise TypeError(f"Too {'many' if alen > elen else 'few'} {things}"
                            f" for {cls}; actual {alen}, expected {expect_val}")
E           TypeError: Too many arguments for typing.List; actual 2, expected 1

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/site-packages/typing_extensions.py:3100: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""