# Module: pypara.dcc
import datetime
from decimal import Decimal
import pytest
import calendar
from typing import List, Optional

# Import the function correctly
def dcfc_act_act(start: datetime.date, asof: datetime.date, end: datetime.date, freq: Optional[Decimal] = None) -> Decimal:
    """
    Computes the day count fraction for "Act/Act" convention.

    :param start: The start date of the period.
    :param asof: The date which the day count fraction to be calculated as of.
    :param end: The end date of the period (a.k.a. termination date).
    :param freq: The frequency of payments in a year.
    :return: Day count fraction.
    """
    years = {year: calendar.isleap(year) for year in range(start.year, asof.year + 1)}
    buffer: List[int] = [0, 0]
    for date in _get_date_range(start, asof):
        if years[date.year]:
            buffer[1] += 1
        else:
            buffer[0] += 1
    return Decimal(buffer[0]) / Decimal(365) + Decimal(buffer[1]) / Decimal(366)

def _get_date_range(start: datetime.date, end: datetime.date):
    current_date = start
    while current_date < end:
        yield current_date
        current_date += datetime.timedelta(days=1)

# Test cases for dcfc_act_act function
@pytest.mark.parametrize("start, asof, expected", [
    (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), Decimal('0.16942884946478')),
    (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), Decimal('0.17216108990194')),
    (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), Decimal('1.08243131970956')),
    (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), Decimal('1.32625945055768'))
])
def test_dcfc_act_act(start, asof, expected):
    assert round(dcfc_act_act(start=start, asof=asof, end=asof), 14) == expected
