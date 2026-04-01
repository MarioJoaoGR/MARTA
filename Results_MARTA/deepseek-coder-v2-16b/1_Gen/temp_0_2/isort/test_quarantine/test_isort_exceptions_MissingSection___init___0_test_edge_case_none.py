
from isort.exceptions import MissingSection

def test_edge_case_none():
    try:
        raise MissingSection("requests", "third_party")
    except MissingSection as e:
        assert str(e) == "Found requests import while parsing, but third_party was not included in the `sections` setting of your config. Please add it before continuing"

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

isort/Test4DT_tests/test_isort_exceptions_MissingSection___init___0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        try:
>           raise MissingSection("requests", "third_party")
E           isort.exceptions.MissingSection: Found requests import while parsing, but third_party was not included in the `sections` setting of your config. Please add it before continuing
E           See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.

isort/Test4DT_tests/test_isort_exceptions_MissingSection___init___0_test_edge_case_none.py:6: MissingSection

During handling of the above exception, another exception occurred:

    def test_edge_case_none():
        try:
            raise MissingSection("requests", "third_party")
        except MissingSection as e:
>           assert str(e) == "Found requests import while parsing, but third_party was not included in the `sections` setting of your config. Please add it before continuing"
E           AssertionError: assert 'Found reques...or more info.' == 'Found reques...re continuing'
E             
E             Skipping 132 identical leading characters in diff, use -v to show
E             -  continuing
E             +  continuing
E             ?            +
E             + See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.

isort/Test4DT_tests/test_isort_exceptions_MissingSection___init___0_test_edge_case_none.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_MissingSection___init___0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.11s ===============================
"""