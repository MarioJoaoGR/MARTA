
from isort.deprecated.finders import ReqsBaseFinder

class TestReqsBaseFinderInit:
    def test_valid_inputs(self):
        class Config:
            pass
        
        config = Config()
        finder = ReqsBaseFinder(config=config, path="path/to/your/project")
        
        assert hasattr(finder, 'enabled')
        assert hasattr(finder, 'path')
        assert hasattr(finder, 'mapping')
        assert hasattr(finder, 'names')
        
        assert finder.path == "path/to/your/project"
        assert not hasattr(finder, '_load_mapping')
        assert not hasattr(finder, '_load_names')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder___init___0_test_valid_inputs
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder___init___0_test_valid_inputs.py:10:17: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""