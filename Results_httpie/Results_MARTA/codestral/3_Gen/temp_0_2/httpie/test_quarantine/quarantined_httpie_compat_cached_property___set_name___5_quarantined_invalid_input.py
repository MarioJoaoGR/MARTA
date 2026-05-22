
import pytest
from httpie.compat import cached_property

class TestCachedProperty:
    @pytest.mark.parametrize("name", [None, "some_other_name"])
    def test_invalid_input(self, name):
        with pytest.raises(TypeError) as excinfo:
            class MyClass:
                @cached_property
                def method(self):
                    pass
                
                if name is not None:
                    method = cached_property(name=name)(method)  # This should raise TypeError
        
        assert str(excinfo.value) == "Cannot assign the same cached_property to two different names (%r and %r)." % (None, name)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___5_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________ TestCachedProperty.test_invalid_input[None] __________________

self = <Test4DT_tests_codestral.test_httpie_compat_cached_property___set_name___5_test_invalid_input.TestCachedProperty object at 0x7f3e54aac710>
name = None

    @pytest.mark.parametrize("name", [None, "some_other_name"])
    def test_invalid_input(self, name):
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___5_test_invalid_input.py:8: Failed
____________ TestCachedProperty.test_invalid_input[some_other_name] ____________

self = <Test4DT_tests_codestral.test_httpie_compat_cached_property___set_name___5_test_invalid_input.TestCachedProperty object at 0x7f3e54945890>
name = 'some_other_name'

    @pytest.mark.parametrize("name", [None, "some_other_name"])
    def test_invalid_input(self, name):
        with pytest.raises(TypeError) as excinfo:
            class MyClass:
                @cached_property
                def method(self):
                    pass
    
                if name is not None:
                    method = cached_property(name=name)(method)  # This should raise TypeError
    
>       assert str(excinfo.value) == "Cannot assign the same cached_property to two different names (%r and %r)." % (None, name)
E       assert "cached_prope...gument 'name'" == "Cannot assig...other_name')."
E         
E         - Cannot assign the same cached_property to two different names (None and 'some_other_name').
E         + cached_property.__init__() got an unexpected keyword argument 'name'

httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___5_test_invalid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___5_test_invalid_input.py::TestCachedProperty::test_invalid_input[None]
FAILED httpie/Test4DT_tests_codestral/test_httpie_compat_cached_property___set_name___5_test_invalid_input.py::TestCachedProperty::test_invalid_input[some_other_name]
============================== 2 failed in 0.12s ===============================
"""