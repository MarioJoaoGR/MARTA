
import unittest
from httpie.output.models import ProcessingOptions

class TestProcessingOptionsShowTraceback(unittest.TestCase):
    def test_show_traceback_default(self):
        options = ProcessingOptions()
        self.assertFalse(options.show_traceback())

    def test_show_traceback_with_debug(self):
        options = ProcessingOptions(debug=True)
        self.assertTrue(options.show_traceback())

    def test_show_traceback_with_traceback(self):
        options = ProcessingOptions(traceback=True)
        self.assertTrue(options.show_traceback())

    def test_show_traceback_with_both(self):
        options = ProcessingOptions(debug=True, traceback=True)
        self.assertTrue(options.show_traceback())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_models_ProcessingOptions_show_traceback_1_test_invalid_inputs
httpie/Test4DT_tests_codestral/test_httpie_output_models_ProcessingOptions_show_traceback_1_test_invalid_inputs.py:8:25: E1102: options.show_traceback is not callable (not-callable)
httpie/Test4DT_tests_codestral/test_httpie_output_models_ProcessingOptions_show_traceback_1_test_invalid_inputs.py:12:24: E1102: options.show_traceback is not callable (not-callable)
httpie/Test4DT_tests_codestral/test_httpie_output_models_ProcessingOptions_show_traceback_1_test_invalid_inputs.py:16:24: E1102: options.show_traceback is not callable (not-callable)
httpie/Test4DT_tests_codestral/test_httpie_output_models_ProcessingOptions_show_traceback_1_test_invalid_inputs.py:20:24: E1102: options.show_traceback is not callable (not-callable)


"""