
from isort.wrap_modes import noqa
import pytest

@pytest.mark.parametrize("interface, expected", [
    (
        {
            "imports": ["math"],
            "statement": "result = math.sqrt(9)",
            "comments": ["# This is a comment", "# Another comment"],
            "comment_prefix": "#",
            "line_length": 50
        },
        "result = math.sqrt(9) # This is a comment # Another comment"
    ),
    (
        {
            "imports": ["os"],
            "statement": "os.getcwd()",
            "comments": ["# This comment is very long and should trigger NOQA", "# Another comment"],
            "comment_prefix": "#",
            "line_length": 30
        },
        "os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment"
    ),
    (
        {
            "imports": ["math"],
            "statement": "result = math.sqrt(9)",
            "comments": [],
            "comment_prefix": "#",
            "line_length": 50
        },
        "result = math.sqrt(9)"
    ),
    (
        {
            "imports": ["math"],
            "statement": "result = math.sqrt(9)",
            "comments": ["# This is a comment", "# Another comment"],
            "comment_prefix": "#",
            "line_length": 20
        },
        "result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment"
    )
])
def test_valid_case(interface, expected):
    assert noqa(**interface) == expected

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

isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py FFFF [100%]

=================================== FAILURES ===================================
_ test_valid_case[interface0-result = math.sqrt(9) # This is a comment # Another comment] _

interface = {'comment_prefix': '#', 'comments': ['# This is a comment', '# Another comment'], 'imports': ['math'], 'line_length': 50, ...}
expected = 'result = math.sqrt(9) # This is a comment # Another comment'

    @pytest.mark.parametrize("interface, expected", [
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9) # This is a comment # Another comment"
        ),
        (
            {
                "imports": ["os"],
                "statement": "os.getcwd()",
                "comments": ["# This comment is very long and should trigger NOQA", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 30
            },
            "os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": [],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9)"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 20
            },
            "result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment"
        )
    ])
    def test_valid_case(interface, expected):
>       assert noqa(**interface) == expected
E       AssertionError: assert 'result = mat...other comment' == 'result = mat...other comment'
E         
E         - result = math.sqrt(9) # This is a comment # Another comment
E         ?                      ^
E         + result = math.sqrt(9)math# NOQA # This is a comment # Another comment
E         ?                      ^^^^ +++++++

isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py:48: AssertionError
_ test_valid_case[interface1-os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment] _

interface = {'comment_prefix': '#', 'comments': ['# This comment is very long and should trigger NOQA', '# Another comment'], 'imports': ['os'], 'line_length': 30, ...}
expected = 'os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment'

    @pytest.mark.parametrize("interface, expected", [
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9) # This is a comment # Another comment"
        ),
        (
            {
                "imports": ["os"],
                "statement": "os.getcwd()",
                "comments": ["# This comment is very long and should trigger NOQA", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 30
            },
            "os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": [],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9)"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 20
            },
            "result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment"
        )
    ])
    def test_valid_case(interface, expected):
>       assert noqa(**interface) == expected
E       AssertionError: assert 'os.getcwd()o...other comment' == 'os.getcwd() ...other comment'
E         
E         - os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment
E         ?            ^                                                    -----
E         + os.getcwd()os# NOQA # This comment is very long and should trigger NOQA # Another comment
E         ?            ^^ +++++++

isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py:48: AssertionError
______________ test_valid_case[interface2-result = math.sqrt(9)] _______________

interface = {'comment_prefix': '#', 'comments': [], 'imports': ['math'], 'line_length': 50, ...}
expected = 'result = math.sqrt(9)'

    @pytest.mark.parametrize("interface, expected", [
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9) # This is a comment # Another comment"
        ),
        (
            {
                "imports": ["os"],
                "statement": "os.getcwd()",
                "comments": ["# This comment is very long and should trigger NOQA", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 30
            },
            "os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": [],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9)"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 20
            },
            "result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment"
        )
    ])
    def test_valid_case(interface, expected):
>       assert noqa(**interface) == expected
E       AssertionError: assert 'result = math.sqrt(9)math' == 'result = math.sqrt(9)'
E         
E         - result = math.sqrt(9)
E         + result = math.sqrt(9)math
E         ?                      ++++

isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py:48: AssertionError
_ test_valid_case[interface3-result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment] _

interface = {'comment_prefix': '#', 'comments': ['# This is a comment', '# Another comment'], 'imports': ['math'], 'line_length': 20, ...}
expected = 'result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment'

    @pytest.mark.parametrize("interface, expected", [
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9) # This is a comment # Another comment"
        ),
        (
            {
                "imports": ["os"],
                "statement": "os.getcwd()",
                "comments": ["# This comment is very long and should trigger NOQA", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 30
            },
            "os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": [],
                "comment_prefix": "#",
                "line_length": 50
            },
            "result = math.sqrt(9)"
        ),
        (
            {
                "imports": ["math"],
                "statement": "result = math.sqrt(9)",
                "comments": ["# This is a comment", "# Another comment"],
                "comment_prefix": "#",
                "line_length": 20
            },
            "result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment"
        )
    ])
    def test_valid_case(interface, expected):
>       assert noqa(**interface) == expected
E       AssertionError: assert 'result = mat...other comment' == 'result = mat...other comment'
E         
E         - result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment
E         ?                                                -----
E         + result = math.sqrt(9)math# NOQA # This is a comment # Another comment
E         ?                      +++++

isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py:48: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py::test_valid_case[interface0-result = math.sqrt(9) # This is a comment # Another comment]
FAILED isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py::test_valid_case[interface1-os.getcwd() # This comment is very long and should trigger NOQA NOQA # Another comment]
FAILED isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py::test_valid_case[interface2-result = math.sqrt(9)]
FAILED isort/Test4DT_tests/test_isort_wrap_modes_noqa_0_test_valid_case.py::test_valid_case[interface3-result = math.sqrt(9) NOQA # This is a comment NOQA # Another comment]
============================== 4 failed in 0.14s ===============================
"""