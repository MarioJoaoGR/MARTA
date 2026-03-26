
from isort.exceptions import FileSkipped

class TestIsortExceptions(unittest.TestCase):
    def test_file_skipped_exception(self):
        try:
            raise FileSkipped("File is corrupted", "documents/report.xlsx")
        except FileSkipped as e:
            self.assertEqual(e.message, "File is corrupted")
            self.assertEqual(e.file_path, "documents/report.xlsx")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_FileSkipped___init___1_test_edge_cases
isort/Test4DT_tests/test_isort_exceptions_FileSkipped___init___1_test_edge_cases.py:4:26: E0602: Undefined variable 'unittest' (undefined-variable)


"""