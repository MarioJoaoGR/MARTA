
import pytest
import sys
from io import StringIO
from isort.main import main as isort_main

@pytest.mark.parametrize("argv, stdin_content, expected_output", [
    (None, "", "Error: arguments passed in without any paths or content."),  # No arguments provided
    ([], [], "Error: arguments passed in without any paths or content."),  # Empty list of file names
    (["--show-version"], None, None),  # Show version with no additional arguments
    (["--show-config", "--show-files"], None, "Error: either specify show-config or show-files not both."),  # Both show-config and show-files specified
])
def test_edge_cases(argv, stdin_content, expected_output):
    if argv is not None:
        sys.argv = argv
    else:
        del sys.argv[1:]

    stdin = StringIO(stdin_content)
    original_stdout = sys.stdout
    try:
        captured_output = StringIO()
        sys.stdout = captured_output
        isort_main(argv, stdin=stdin)
        if expected_output:
            assert captured_output.getvalue().strip() == expected_output
    finally:
        sys.stdout = original_stdout

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py FFFF       [100%]

=================================== FAILURES ===================================
_ test_edge_cases[None--Error: arguments passed in without any paths or content.] _

argv = None, stdin_content = ''
expected_output = 'Error: arguments passed in without any paths or content.'

    @pytest.mark.parametrize("argv, stdin_content, expected_output", [
        (None, "", "Error: arguments passed in without any paths or content."),  # No arguments provided
        ([], [], "Error: arguments passed in without any paths or content."),  # Empty list of file names
        (["--show-version"], None, None),  # Show version with no additional arguments
        (["--show-config", "--show-files"], None, "Error: either specify show-config or show-files not both."),  # Both show-config and show-files specified
    ])
    def test_edge_cases(argv, stdin_content, expected_output):
        if argv is not None:
            sys.argv = argv
        else:
            del sys.argv[1:]
    
        stdin = StringIO(stdin_content)
        original_stdout = sys.stdout
        try:
            captured_output = StringIO()
            sys.stdout = captured_output
            isort_main(argv, stdin=stdin)
            if expected_output:
>               assert captured_output.getvalue().strip() == expected_output
E               AssertionError: assert '_           ...to use isort.' == 'Error: argum...s or content.'
E                 
E                 - Error: arguments passed in without any paths or content.
E                 + _                 _
E                 +                 (_) ___  ___  _ __| |_
E                 +                 | |/ _/ / _ \/ '__  _/
E                 +                 | |\__ \/\_\/| |  | |_
E                 +                 |_|\___/\___/\_/   \_/...
E                 
E                 ...Full output truncated (16 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py:26: AssertionError
_ test_edge_cases[argv1-stdin_content1-Error: arguments passed in without any paths or content.] _

argv = [], stdin_content = []
expected_output = 'Error: arguments passed in without any paths or content.'

    @pytest.mark.parametrize("argv, stdin_content, expected_output", [
        (None, "", "Error: arguments passed in without any paths or content."),  # No arguments provided
        ([], [], "Error: arguments passed in without any paths or content."),  # Empty list of file names
        (["--show-version"], None, None),  # Show version with no additional arguments
        (["--show-config", "--show-files"], None, "Error: either specify show-config or show-files not both."),  # Both show-config and show-files specified
    ])
    def test_edge_cases(argv, stdin_content, expected_output):
        if argv is not None:
            sys.argv = argv
        else:
            del sys.argv[1:]
    
>       stdin = StringIO(stdin_content)
E       TypeError: initial_value must be str or None, not list

isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py:19: TypeError
_______________________ test_edge_cases[argv2-None-None] _______________________

argv = ['--show-version'], stdin_content = None, expected_output = None

    @pytest.mark.parametrize("argv, stdin_content, expected_output", [
        (None, "", "Error: arguments passed in without any paths or content."),  # No arguments provided
        ([], [], "Error: arguments passed in without any paths or content."),  # Empty list of file names
        (["--show-version"], None, None),  # Show version with no additional arguments
        (["--show-config", "--show-files"], None, "Error: either specify show-config or show-files not both."),  # Both show-config and show-files specified
    ])
    def test_edge_cases(argv, stdin_content, expected_output):
        if argv is not None:
            sys.argv = argv
        else:
            del sys.argv[1:]
    
        stdin = StringIO(stdin_content)
        original_stdout = sys.stdout
        try:
            captured_output = StringIO()
            sys.stdout = captured_output
>           isort_main(argv, stdin=stdin)

isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/main.py:1062: in main
    arguments = parse_args(argv)
isort/isort/main.py:937: in parse_args
    arguments = {key: value for key, value in vars(parser.parse_args(argv)).items() if value}
/usr/local/lib/python3.11/argparse.py:1877: in parse_args
    self.error(msg % ' '.join(argv))
/usr/local/lib/python3.11/argparse.py:2640: in error
    self.exit(2, _('%(prog)s: error: %(message)s\n') % args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='--show-version', usage=None, description="Sort Python import definitions alphabetically within lo...upgrade_guides/5.0.0.html", formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=False)
status = 2
message = '--show-version: error: unrecognized arguments: --show-version\n'

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
>       _sys.exit(status)
E       SystemExit: 2

/usr/local/lib/python3.11/argparse.py:2627: SystemExit
----------------------------- Captured stderr call -----------------------------
usage: --show-version [-h] [-V] [--vn] [-v] [--only-modified]
                      [--dedup-headings] [-q] [-d] [--overwrite-in-place]
                      [--show-config] [--show-files] [--df] [-c] [--ws]
                      [--sp SETTINGS_PATH] [--cr CONFIG_ROOT]
                      [--resolve-all-configs] [--profile PROFILE]
                      [--old-finders] [-j [JOBS]] [--ac] [--interactive]
                      [--format-error FORMAT_ERROR]
                      [--format-success FORMAT_SUCCESS] [--srx]
                      [--filter-files] [-s SKIP] [--extend-skip EXTEND_SKIP]
                      [--sg SKIP_GLOB] [--extend-skip-glob EXTEND_SKIP_GLOB]
                      [--gitignore] [--ext SUPPORTED_EXTENSIONS]
                      [--blocked-extension BLOCKED_EXTENSIONS]
                      [--dont-follow-links] [--filename FILENAME]
                      [--allow-root] [-a ADD_IMPORTS] [--append] [--af]
                      [--rm REMOVE_IMPORTS] [--float-to-top]
                      [--dont-float-to-top] [--ca] [--cs] [-e] [--ff]
                      [--fgw [FORCE_GRID_WRAP]] [-i INDENT]
                      [--lbi LINES_BEFORE_IMPORTS] [--lai LINES_AFTER_IMPORTS]
                      [--lbt LINES_BETWEEN_TYPES] [--le LINE_ENDING] [--ls]
                      [--lss]
                      [-m {GRID,VERTICAL,HANGING_INDENT,VERTICAL_HANGING_INDENT,VERTICAL_GRID,VERTICAL_GRID_GROUPED,VERTICAL_GRID_GROUPED_NO_COMMA,NOQA,VERTICAL_HANGING_INDENT_BRACKET,VERTICAL_PREFIX_FROM_MODULE_IMPORT,HANGING_INDENT_WITH_PARENTHESES,BACKSLASH_GRID,0,1,2,3,4,5,6,7,8,9,10,11}]
                      [-n] [--nis] [--ot] [--dt] [--rr] [--reverse-sort]
                      [--sort-order SORT_ORDER] [--sl]
                      [--nsl SINGLE_LINE_EXCLUSIONS] [--tc] [--up]
                      [-l LINE_LENGTH] [--wl WRAP_LENGTH] [--case-sensitive]
                      [--remove-redundant-aliases] [--honor-noqa]
                      [--treat-comment-as-code TREAT_COMMENTS_AS_CODE]
                      [--treat-all-comment-as-code] [--formatter FORMATTER]
                      [--color] [--ext-format EXT_FORMAT] [--star-first]
                      [--split-on-trailing-comma] [--sd DEFAULT_SECTION]
                      [--only-sections] [--ds] [--fas] [--fss] [--hcss]
                      [--srss] [--fass] [-t FORCE_TO_TOP]
                      [--combine-straight-imports] [--nlb NO_LINES_BEFORE]
                      [--src SRC_PATHS] [-b KNOWN_STANDARD_LIBRARY]
                      [--extra-builtin EXTRA_STANDARD_LIBRARY]
                      [-f KNOWN_FUTURE_LIBRARY] [-o KNOWN_THIRD_PARTY]
                      [-p KNOWN_FIRST_PARTY]
                      [--known-local-folder KNOWN_LOCAL_FOLDER]
                      [--virtual-env VIRTUAL_ENV] [--conda-env CONDA_ENV]
                      [--py {all,2,27,3,310,311,312,313,314,36,37,38,39,auto}]
                      [files ...]
--show-version: error: unrecognized arguments: --show-version
_ test_edge_cases[argv3-None-Error: either specify show-config or show-files not both.] _

argv = ['--show-config', '--show-files'], stdin_content = None
expected_output = 'Error: either specify show-config or show-files not both.'

    @pytest.mark.parametrize("argv, stdin_content, expected_output", [
        (None, "", "Error: arguments passed in without any paths or content."),  # No arguments provided
        ([], [], "Error: arguments passed in without any paths or content."),  # Empty list of file names
        (["--show-version"], None, None),  # Show version with no additional arguments
        (["--show-config", "--show-files"], None, "Error: either specify show-config or show-files not both."),  # Both show-config and show-files specified
    ])
    def test_edge_cases(argv, stdin_content, expected_output):
        if argv is not None:
            sys.argv = argv
        else:
            del sys.argv[1:]
    
        stdin = StringIO(stdin_content)
        original_stdout = sys.stdout
        try:
            captured_output = StringIO()
            sys.stdout = captured_output
>           isort_main(argv, stdin=stdin)

isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

argv = ['--show-config', '--show-files']
stdin = <_io.StringIO object at 0x7f0e7831feb0>

    def main(argv: Sequence[str] | None = None, stdin: TextIOWrapper | None = None) -> None:
        arguments = parse_args(argv)
        if arguments.get("show_version"):
            print(ASCII_ART)
            return
    
        show_config: bool = arguments.pop("show_config", False)
        show_files: bool = arguments.pop("show_files", False)
        if show_config and show_files:
>           sys.exit("Error: either specify show-config or show-files not both.")
E           SystemExit: Error: either specify show-config or show-files not both.

isort/isort/main.py:1070: SystemExit
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py::test_edge_cases[None--Error: arguments passed in without any paths or content.]
FAILED isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py::test_edge_cases[argv1-stdin_content1-Error: arguments passed in without any paths or content.]
FAILED isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py::test_edge_cases[argv2-None-None]
FAILED isort/Test4DT_tests/test_isort_main_main_0_test_edge_cases.py::test_edge_cases[argv3-None-Error: either specify show-config or show-files not both.]
============================== 4 failed in 0.22s ===============================
"""