
import pytest
from unittest.mock import patch
import datetime
from decimal import Decimal
from pypara.dcc import dcfc_30_360_isda, Date

@pytest.mark.parametrize("start, asof, end, expected", [
    (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28), Decimal('0.16666666666667')),
    (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29), Decimal('0.16944444444444')),
    (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30), Decimal('1.08333333333333')),
    (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), datetime.date(2009, 5, 31), Decimal('1.33333333333333'))
])
def test_valid_inputs(start, asof, end, expected):
    with patch('pypara.dcc.datetime', autospec=True) as mock_datetime:
        result = dcfc_30_360_isda(start=start, asof=asof, end=end)
        assert round(result, 14) == expected, f"Test failed for start={start}, asof={asof}, end={end}"


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_isda_1.py . [ 25%]
.F.                                                                      [100%]

=================================== FAILURES ===================================
________________ test_valid_inputs[start2-asof2-end2-expected2] ________________

start = datetime.date(2007, 10, 31), asof = datetime.date(2008, 11, 30)
end = datetime.date(2008, 11, 30), expected = Decimal('1.08333333333333')

    @pytest.mark.parametrize("start, asof, end, expected", [
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28), Decimal('0.16666666666667')),
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29), Decimal('0.16944444444444')),
        (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30), Decimal('1.08333333333333')),
        (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), datetime.date(2009, 5, 31), Decimal('1.33333333333333'))
    ])
    def test_valid_inputs(start, asof, end, expected):
        with patch('pypara.dcc.datetime', autospec=True) as mock_datetime:
            result = dcfc_30_360_isda(start=start, asof=asof, end=end)
>           assert round(result, 14) == expected, f"Test failed for start={start}, asof={asof}, end={end}"
E           AssertionError: Test failed for start=2007-10-31, asof=2008-11-30, end=2008-11-30
E           assert <MagicMock name='datetime.date().day.__rsub__().__add__().__add__().__truediv__().__round__()' id='140540282463296'> == Decimal('1.08333333333333')
E            +  where <MagicMock name='datetime.date().day.__rsub__().__add__().__add__().__truediv__().__round__()' id='140540282463296'> = round(<MagicMock name='datetime.date().day.__rsub__().__add__().__add__().__truediv__()' id='140540282430672'>, 14)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_isda_1.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_isda_1.py::test_valid_inputs[start2-asof2-end2-expected2]
========================= 1 failed, 3 passed in 0.09s ==========================
"""