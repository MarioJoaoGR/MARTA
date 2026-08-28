# Module: ansible.module_utils.urls
# test_missing_module_error.py
from ansible.module_utils.errors import MissingModuleError
import pytest
import sys
import traceback

def test_missing_module_error_basic():
    try:
        # Attempting to import a non-existent module
        import non_existent_module
    except MissingModuleError as e:
        assert str(e) == "Failed to import 3rd party module required by the caller: 'non_existent_module'"
        assert isinstance(e.import_traceback, str)
        assert len(e.import_traceback) > 0
    else:
        pytest.fail("Expected MissingModuleError but no exception was raised")

def test_missing_module_error_in_module_context():
    from ansible.module_utils.errors import MissingModuleError
    
    class FakeAnsibleModule:
        def __init__(self, argument_spec):
            self.argument_spec = argument_spec
        
        def exit_json(self, changed=False, msg=""):
            assert changed == True
            assert msg == "All required modules imported successfully."
        
        def fail_json(self, msg=""):
            assert False, f"Expected to pass but failed with message: {msg}"
    
    argument_spec = {'required_module': {'type': 'str', 'required': True}}
    module = FakeAnsibleModule(argument_spec)
    
    try:
        import required_module  # This will raise MissingModuleError if not found
    except MissingModuleError as e:
        module.fail_json(msg=f"Failed to import a required module: {e}")
    else:
        pytest.fail("Expected MissingModuleError but no exception was raised")

if __name__ == '__main__':
    sys.exit(pytest.main())
