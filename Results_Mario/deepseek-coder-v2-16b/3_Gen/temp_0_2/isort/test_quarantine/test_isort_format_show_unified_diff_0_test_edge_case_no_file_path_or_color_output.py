
import pytest
from isort.format import show_unified_diff
from pathlib import Path
from datetime import datetime
from io import StringIO

@pytest.mark.parametrize("file_path, color_output", [
    (None, False),
    (Path('test.txt'), True)
])
def test_edge_case_no_file_path_or_color_output(file_path, color_output):
    file_input = "line1\nline2\n"
    file_output = "line1\nchanged line2\n"
    output = StringIO()
    
    show_unified_diff(
        file_input=file_input,
        file_output=file_output,
        file_path=file_path,
        output=output,
        color_output=color_output
    )
    
    expected_diff = """--- test.txt:before
+++ test.txt:after
@@ -1 +1 @@
-line2
+changed line2
"""
    assert output.getvalue().strip() == expected_diff.strip()

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

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case_no_file_path_or_color_output.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________ test_edge_case_no_file_path_or_color_output[None-False] ____________

file_path = None, color_output = False

    @pytest.mark.parametrize("file_path, color_output", [
        (None, False),
        (Path('test.txt'), True)
    ])
    def test_edge_case_no_file_path_or_color_output(file_path, color_output):
        file_input = "line1\nline2\n"
        file_output = "line1\nchanged line2\n"
        output = StringIO()
    
        show_unified_diff(
            file_input=file_input,
            file_output=file_output,
            file_path=file_path,
            output=output,
            color_output=color_output
        )
    
        expected_diff = """--- test.txt:before
    +++ test.txt:after
    @@ -1 +1 @@
    -line2
    +changed line2
    """
>       assert output.getvalue().strip() == expected_diff.strip()
E       AssertionError: assert '--- :before\...changed line2' == '--- test.txt...changed line2'
E         
E         - --- test.txt:before
E         - +++ test.txt:after
E         + --- :before	2026-03-26 02:58:15.278656
E         + +++ :after	2026-03-26 02:58:15.278672
E         - @@ -1 +1 @@
E         + @@ -1,2 +1,2 @@...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case_no_file_path_or_color_output.py:31: AssertionError
_________ test_edge_case_no_file_path_or_color_output[file_path1-True] _________

file_path = PosixPath('test.txt'), color_output = True

    @pytest.mark.parametrize("file_path, color_output", [
        (None, False),
        (Path('test.txt'), True)
    ])
    def test_edge_case_no_file_path_or_color_output(file_path, color_output):
        file_input = "line1\nline2\n"
        file_output = "line1\nchanged line2\n"
        output = StringIO()
    
>       show_unified_diff(
            file_input=file_input,
            file_output=file_output,
            file_path=file_path,
            output=output,
            color_output=color_output
        )

isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case_no_file_path_or_color_output.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/format.py:59: in show_unified_diff
    printer = create_terminal_printer(color_output, output)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

color = True, output = <_io.StringIO object at 0x7f18fd10c700>, error = ''
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

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case_no_file_path_or_color_output.py::test_edge_case_no_file_path_or_color_output[None-False]
FAILED isort/Test4DT_tests/test_isort_format_show_unified_diff_0_test_edge_case_no_file_path_or_color_output.py::test_edge_case_no_file_path_or_color_output[file_path1-True]
============================== 2 failed in 0.11s ===============================
"""