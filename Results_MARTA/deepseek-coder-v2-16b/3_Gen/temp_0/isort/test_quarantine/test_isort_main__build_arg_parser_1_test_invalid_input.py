
import pytest
from isort.main import _build_arg_parser

def test_invalid_input():
    with pytest.raises(SystemExit):
        try:
            parser = _build_arg_parser()
            parser.parse_args(["--invalid-option"])
        except SystemExit as e:
            assert e.code == 2, "Expected SystemExit with code 2 for invalid input"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py:6: Failed
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
__main__.py: error: unrecognized arguments: --invalid-option
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""