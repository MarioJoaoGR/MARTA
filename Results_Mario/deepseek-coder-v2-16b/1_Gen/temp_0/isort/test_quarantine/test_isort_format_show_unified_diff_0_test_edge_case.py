
from isort.format import show_unified_diff
from pathlib import Path
from datetime import datetime
from io import StringIO
import pytest

@pytest.mark.parametrize("color_output, expected", [(True, "expected_colored"), (False, "expected_plain")])
def test_show_unified_diff(color_output, expected):
    file_input = "old content"
    file_output = "new content"
    file_path = Path("example/path/to/file.txt")
    output = StringIO()
    
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=file_path, output=output, color_output=color_output)
    
    assert expected in output.getvalue()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________ test_show_unified_diff[True-expected_colored] _________________

color_output = True, expected = 'expected_colored'

    @pytest.mark.parametrize("color_output, expected", [(True, "expected_colored"), (False, "expected_plain")])
    def test_show_unified_diff(color_output, expected):
        file_input = "old content"
        file_output = "new content"
        file_path = Path("example/path/to/file.txt")
        output = StringIO()
    
>       show_unified_diff(file_input=file_input, file_output=file_output, file_path=file_path, output=output, color_output=color_output)

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/format.py:59: in show_unified_diff
    printer = create_terminal_printer(color_output, output)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

color = True, output = <_io.StringIO object at 0x7fce028d5900>, error = ''
success = ''

    def create_terminal_printer(
        color: bool, output: TextIO | None = None, error: str = "", success: str = ""
    ) -> BasicPrinter:
        if color and colorama_unavailable:
            no_colorama_message = (
                "\n"
                "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
                "Reference: https://pypi.org/project/colorama/\n\n"
                "You can either install it separately on your system or as the colors extra "
                "for isort. Ex: \n\n"
                "$ pip install isort[colors]\n"
            )
            print(no_colorama_message, file=sys.stderr)
>           sys.exit(1)
E           SystemExit: 1

isort/isort/format.py:151: SystemExit
----------------------------- Captured stderr call -----------------------------

Sorry, but to use --color (color_output) the colorama python package is required.

Reference: https://pypi.org/project/colorama/

You can either install it separately on your system or as the colors extra for isort. Ex: 

$ pip install isort[colors]

_________________ test_show_unified_diff[False-expected_plain] _________________

color_output = False, expected = 'expected_plain'

    @pytest.mark.parametrize("color_output, expected", [(True, "expected_colored"), (False, "expected_plain")])
    def test_show_unified_diff(color_output, expected):
        file_input = "old content"
        file_output = "new content"
        file_path = Path("example/path/to/file.txt")
        output = StringIO()
    
>       show_unified_diff(file_input=file_input, file_output=file_output, file_path=file_path, output=output, color_output=color_output)

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/format.py:62: in show_unified_diff
    datetime.now() if file_path is None else datetime.fromtimestamp(file_path.stat().st_mtime)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = PosixPath('example/path/to/file.txt')

    def stat(self, *, follow_symlinks=True):
        """
        Return the result of the stat() system call on this path, like
        os.stat() does.
        """
>       return os.stat(self, follow_symlinks=follow_symlinks)
E       FileNotFoundError: [Errno 2] No such file or directory: 'example/path/to/file.txt'

/usr/local/lib/python3.11/pathlib.py:1013: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case.py::test_show_unified_diff[True-expected_colored]
FAILED isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case.py::test_show_unified_diff[False-expected_plain]
============================== 2 failed in 0.26s ===============================
"""