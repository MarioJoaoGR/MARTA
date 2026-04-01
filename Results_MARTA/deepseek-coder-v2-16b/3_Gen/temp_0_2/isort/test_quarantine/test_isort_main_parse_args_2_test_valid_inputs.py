
import pytest
import sys
from isort.main import parse_args

# Define a mock for _build_arg_parser since it's not defined in this snippet
def _build_arg_parser():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Sort Python import definitions alphabetically within logic...upgrade_guides/5.0.0.html")
    return parser

@pytest.mark.parametrize("argv, expected", [
    (["--float-to-top"], {"float_to_top": True}),
    (["--order-by-type"], {"order_by_type": True}),
    (["--float-to-top", "--order-by-type"], {"float_to_top": True, "order_by_type": True}),
    (["--dont-follow-links"], {"follow_links": False}),
    (["--dont-float-to-top"], {"float_to_top": False}),
    (["--multi-line-output", "20"], {"multi_line_output": 20}),
    (["--multi-line-output", "10"], {"multi_line_output": 10}),
])
def test_valid_inputs(argv, expected):
    sys.argv[1:] = argv
    parsed_args = parse_args()
    assert parsed_args == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

isort/Test4DT_tests/test_isort_main_parse_args_2_test_valid_inputs.py .. [ 28%]
...FF                                                                    [100%]

=================================== FAILURES ===================================
______________________ test_valid_inputs[argv5-expected5] ______________________

argv = ['--multi-line-output', '20'], expected = {'multi_line_output': 20}

    @pytest.mark.parametrize("argv, expected", [
        (["--float-to-top"], {"float_to_top": True}),
        (["--order-by-type"], {"order_by_type": True}),
        (["--float-to-top", "--order-by-type"], {"float_to_top": True, "order_by_type": True}),
        (["--dont-follow-links"], {"follow_links": False}),
        (["--dont-float-to-top"], {"float_to_top": False}),
        (["--multi-line-output", "20"], {"multi_line_output": 20}),
        (["--multi-line-output", "10"], {"multi_line_output": 10}),
    ])
    def test_valid_inputs(argv, expected):
        sys.argv[1:] = argv
>       parsed_args = parse_args()

isort/Test4DT_tests/test_isort_main_parse_args_2_test_valid_inputs.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/main.py:937: in parse_args
    arguments = {key: value for key, value in vars(parser.parse_args(argv)).items() if value}
/usr/local/lib/python3.11/argparse.py:1877: in parse_args
    self.error(msg % ' '.join(argv))
/usr/local/lib/python3.11/argparse.py:2640: in error
    self.exit(2, _('%(prog)s: error: %(message)s\n') % args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description="Sort Python import definitions alphabetically within logic...upgrade_guides/5.0.0.html", formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=False)
status = 2
message = '__main__.py: error: unrecognized arguments: --multi-line-output\n'

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
>       _sys.exit(status)
E       SystemExit: 2

/usr/local/lib/python3.11/argparse.py:2627: SystemExit
----------------------------- Captured stderr call -----------------------------
usage: __main__.py [-h] [-V] [--vn] [-v] [--only-modified] [--dedup-headings]
                   [-q] [-d] [--overwrite-in-place] [--show-config]
                   [--show-files] [--df] [-c] [--ws] [--sp SETTINGS_PATH]
                   [--cr CONFIG_ROOT] [--resolve-all-configs]
                   [--profile PROFILE] [--old-finders] [-j [JOBS]] [--ac]
                   [--interactive] [--format-error FORMAT_ERROR]
                   [--format-success FORMAT_SUCCESS] [--srx] [--filter-files]
                   [-s SKIP] [--extend-skip EXTEND_SKIP] [--sg SKIP_GLOB]
                   [--extend-skip-glob EXTEND_SKIP_GLOB] [--gitignore]
                   [--ext SUPPORTED_EXTENSIONS]
                   [--blocked-extension BLOCKED_EXTENSIONS]
                   [--dont-follow-links] [--filename FILENAME] [--allow-root]
                   [-a ADD_IMPORTS] [--append] [--af] [--rm REMOVE_IMPORTS]
                   [--float-to-top] [--dont-float-to-top] [--ca] [--cs] [-e]
                   [--ff] [--fgw [FORCE_GRID_WRAP]] [-i INDENT]
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
                   [--only-sections] [--ds] [--fas] [--fss] [--hcss] [--srss]
                   [--fass] [-t FORCE_TO_TOP] [--combine-straight-imports]
                   [--nlb NO_LINES_BEFORE] [--src SRC_PATHS]
                   [-b KNOWN_STANDARD_LIBRARY]
                   [--extra-builtin EXTRA_STANDARD_LIBRARY]
                   [-f KNOWN_FUTURE_LIBRARY] [-o KNOWN_THIRD_PARTY]
                   [-p KNOWN_FIRST_PARTY]
                   [--known-local-folder KNOWN_LOCAL_FOLDER]
                   [--virtual-env VIRTUAL_ENV] [--conda-env CONDA_ENV]
                   [--py {all,2,27,3,310,311,312,313,314,36,37,38,39,auto}]
                   [files ...]
__main__.py: error: unrecognized arguments: --multi-line-output
______________________ test_valid_inputs[argv6-expected6] ______________________

argv = ['--multi-line-output', '10'], expected = {'multi_line_output': 10}

    @pytest.mark.parametrize("argv, expected", [
        (["--float-to-top"], {"float_to_top": True}),
        (["--order-by-type"], {"order_by_type": True}),
        (["--float-to-top", "--order-by-type"], {"float_to_top": True, "order_by_type": True}),
        (["--dont-follow-links"], {"follow_links": False}),
        (["--dont-float-to-top"], {"float_to_top": False}),
        (["--multi-line-output", "20"], {"multi_line_output": 20}),
        (["--multi-line-output", "10"], {"multi_line_output": 10}),
    ])
    def test_valid_inputs(argv, expected):
        sys.argv[1:] = argv
>       parsed_args = parse_args()

isort/Test4DT_tests/test_isort_main_parse_args_2_test_valid_inputs.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/main.py:937: in parse_args
    arguments = {key: value for key, value in vars(parser.parse_args(argv)).items() if value}
/usr/local/lib/python3.11/argparse.py:1877: in parse_args
    self.error(msg % ' '.join(argv))
/usr/local/lib/python3.11/argparse.py:2640: in error
    self.exit(2, _('%(prog)s: error: %(message)s\n') % args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description="Sort Python import definitions alphabetically within logic...upgrade_guides/5.0.0.html", formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=False)
status = 2
message = '__main__.py: error: unrecognized arguments: --multi-line-output\n'

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
>       _sys.exit(status)
E       SystemExit: 2

/usr/local/lib/python3.11/argparse.py:2627: SystemExit
----------------------------- Captured stderr call -----------------------------
usage: __main__.py [-h] [-V] [--vn] [-v] [--only-modified] [--dedup-headings]
                   [-q] [-d] [--overwrite-in-place] [--show-config]
                   [--show-files] [--df] [-c] [--ws] [--sp SETTINGS_PATH]
                   [--cr CONFIG_ROOT] [--resolve-all-configs]
                   [--profile PROFILE] [--old-finders] [-j [JOBS]] [--ac]
                   [--interactive] [--format-error FORMAT_ERROR]
                   [--format-success FORMAT_SUCCESS] [--srx] [--filter-files]
                   [-s SKIP] [--extend-skip EXTEND_SKIP] [--sg SKIP_GLOB]
                   [--extend-skip-glob EXTEND_SKIP_GLOB] [--gitignore]
                   [--ext SUPPORTED_EXTENSIONS]
                   [--blocked-extension BLOCKED_EXTENSIONS]
                   [--dont-follow-links] [--filename FILENAME] [--allow-root]
                   [-a ADD_IMPORTS] [--append] [--af] [--rm REMOVE_IMPORTS]
                   [--float-to-top] [--dont-float-to-top] [--ca] [--cs] [-e]
                   [--ff] [--fgw [FORCE_GRID_WRAP]] [-i INDENT]
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
                   [--only-sections] [--ds] [--fas] [--fss] [--hcss] [--srss]
                   [--fass] [-t FORCE_TO_TOP] [--combine-straight-imports]
                   [--nlb NO_LINES_BEFORE] [--src SRC_PATHS]
                   [-b KNOWN_STANDARD_LIBRARY]
                   [--extra-builtin EXTRA_STANDARD_LIBRARY]
                   [-f KNOWN_FUTURE_LIBRARY] [-o KNOWN_THIRD_PARTY]
                   [-p KNOWN_FIRST_PARTY]
                   [--known-local-folder KNOWN_LOCAL_FOLDER]
                   [--virtual-env VIRTUAL_ENV] [--conda-env CONDA_ENV]
                   [--py {all,2,27,3,310,311,312,313,314,36,37,38,39,auto}]
                   [files ...]
__main__.py: error: unrecognized arguments: --multi-line-output
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main_parse_args_2_test_valid_inputs.py::test_valid_inputs[argv5-expected5]
FAILED isort/Test4DT_tests/test_isort_main_parse_args_2_test_valid_inputs.py::test_valid_inputs[argv6-expected6]
========================= 2 failed, 5 passed in 0.24s ==========================
"""