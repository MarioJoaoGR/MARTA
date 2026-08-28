
import pytest
from blib2to3.pgen2.tokenize import _get_normal_name

@pytest.mark.parametrize("orig_enc, expected", [
    ("UTF-8", "utf-8"),
    ("latin-1", "iso-8859-1"),
    ("ISO-Latin-1", "iso-8859-1"),
    ("utf-8-variant", "utf-8-variant"),
    ("", ""),
    (None, None),
])
def test_get_normal_name(orig_enc, expected):
    assert _get_normal_name(orig_enc) == expected

@pytest.mark.parametrize("orig_enc, expected", [
    ("UTF-8", "utf-8"),
    ("latin-1", "iso-8859-1"),
    ("ISO-Latin-1", "iso-8859-1"),
    ("utf-8-variant", "utf-8-variant"),
    ("", ""),
    (None, None),
])
def test_get_normal_name_with_none(orig_enc, expected):
    assert _get_normal_name(orig_enc) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 12 items

../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py . [  8%]
..F.F...F.F                                                              [100%]

=================================== FAILURES ===================================
______________ test_get_normal_name[utf-8-variant-utf-8-variant] _______________

orig_enc = 'utf-8-variant', expected = 'utf-8-variant'

    @pytest.mark.parametrize("orig_enc, expected", [
        ("UTF-8", "utf-8"),
        ("latin-1", "iso-8859-1"),
        ("ISO-Latin-1", "iso-8859-1"),
        ("utf-8-variant", "utf-8-variant"),
        ("", ""),
        (None, None),
    ])
    def test_get_normal_name(orig_enc, expected):
>       assert _get_normal_name(orig_enc) == expected
E       AssertionError: assert 'utf-8' == 'utf-8-variant'
E         
E         - utf-8-variant
E         + utf-8

/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py:14: AssertionError
_______________________ test_get_normal_name[None-None] ________________________

orig_enc = None, expected = None

    @pytest.mark.parametrize("orig_enc, expected", [
        ("UTF-8", "utf-8"),
        ("latin-1", "iso-8859-1"),
        ("ISO-Latin-1", "iso-8859-1"),
        ("utf-8-variant", "utf-8-variant"),
        ("", ""),
        (None, None),
    ])
    def test_get_normal_name(orig_enc, expected):
>       assert _get_normal_name(orig_enc) == expected

/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

orig_enc = None

    def _get_normal_name(orig_enc: str) -> str:
        """Imitates get_normal_name in tokenizer.c."""
        # Only care about the first 12 characters.
>       enc = orig_enc[:12].lower().replace("_", "-")
E       TypeError: 'NoneType' object is not subscriptable

/opt/marta/baselines/codamosa/replication/test-apps/black/src/blib2to3/pgen2/tokenize.py:295: TypeError
_________ test_get_normal_name_with_none[utf-8-variant-utf-8-variant] __________

orig_enc = 'utf-8-variant', expected = 'utf-8-variant'

    @pytest.mark.parametrize("orig_enc, expected", [
        ("UTF-8", "utf-8"),
        ("latin-1", "iso-8859-1"),
        ("ISO-Latin-1", "iso-8859-1"),
        ("utf-8-variant", "utf-8-variant"),
        ("", ""),
        (None, None),
    ])
    def test_get_normal_name_with_none(orig_enc, expected):
>       assert _get_normal_name(orig_enc) == expected
E       AssertionError: assert 'utf-8' == 'utf-8-variant'
E         
E         - utf-8-variant
E         + utf-8

/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py:25: AssertionError
__________________ test_get_normal_name_with_none[None-None] ___________________

orig_enc = None, expected = None

    @pytest.mark.parametrize("orig_enc, expected", [
        ("UTF-8", "utf-8"),
        ("latin-1", "iso-8859-1"),
        ("ISO-Latin-1", "iso-8859-1"),
        ("utf-8-variant", "utf-8-variant"),
        ("", ""),
        (None, None),
    ])
    def test_get_normal_name_with_none(orig_enc, expected):
>       assert _get_normal_name(orig_enc) == expected

/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

orig_enc = None

    def _get_normal_name(orig_enc: str) -> str:
        """Imitates get_normal_name in tokenizer.c."""
        # Only care about the first 12 characters.
>       enc = orig_enc[:12].lower().replace("_", "-")
E       TypeError: 'NoneType' object is not subscriptable

/opt/marta/baselines/codamosa/replication/test-apps/black/src/blib2to3/pgen2/tokenize.py:295: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py::test_get_normal_name[utf-8-variant-utf-8-variant]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py::test_get_normal_name[None-None]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py::test_get_normal_name_with_none[utf-8-variant-utf-8-variant]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize__get_normal_name_0.py::test_get_normal_name_with_none[None-None]
========================= 4 failed, 8 passed in 0.10s ==========================
"""