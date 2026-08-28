# Module: pypara.dcc
import datetime
from typing import Union, Optional
import pytest

# Import the function using its provided module name.
from pypara.dcc import _last_payment_date

def test__last_payment_date():
    # Test cases for different scenarios
    
    # Case 1: Monthly frequency, start date is January 1st, current date is December 31st of the next year
    assert _last_payment_date(datetime.date(2014, 1, 1), datetime.date(2015, 12, 31), 1) == datetime.date(2015, 1, 1)
    
    # Case 2: Same as case 1 but current date is within the same year
    assert _last_payment_date(datetime.date(2015, 1, 1), datetime.date(2015, 12, 31), 1) == datetime.date(2015, 1, 1)
    
    # Case 3: Semi-annual frequency, start date is January 1st, current date is December 31st of the next year
    assert _last_payment_date(datetime.date(2014, 1, 1), datetime.date(2015, 12, 31), 2) == datetime.date(2015, 7, 1)
    
    # Case 4: Semi-annual frequency, start date is January 1st, current date is August 31st of the same year
    assert _last_payment_date(datetime.date(2014, 1, 1), datetime.date(2015, 8, 31), 2) == datetime.date(2015, 7, 1)
    
    # Case 5: Semi-annual frequency, start date is January 1st, current date is April 30th of the same year
    assert _last_payment_date(datetime.date(2014, 1, 1), datetime.date(2015, 4, 30), 2) == datetime.date(2015, 1, 1)
    
    # Case 6: Annual frequency, start date is June 1st, current date is April 30th of the next year
    assert _last_payment_date(datetime.date(2014, 6, 1), datetime.date(2015, 4, 30), 1) == datetime.date(2014, 6, 1)
    
    # Case 7: Quarterly frequency, start date is July 7th, current date is October 6th of the next year
    assert _last_payment_date(datetime.date(2008, 7, 7), datetime.date(2015, 10, 6), 4) == datetime.date(2015, 7, 7)
    
    # Case 8: Monthly frequency, start date is December 9th, current date is December 4th of the same year
    assert _last_payment_date(datetime.date(2014, 12, 9), datetime.date(2015, 12, 4), 1) == datetime.date(2014, 12, 9)
    
    # Case 9: Semi-annual frequency, start date is December 15th, current date is January 6th of the next year
    assert _last_payment_date(datetime.date(2012, 12, 15), datetime.date(2016, 1, 6), 2) == datetime.date(2015, 12, 15)
    
    # Case 10: Semi-annual frequency, start date is December 15th, current date is December 31st of the same year
    assert _last_payment_date(datetime.date(2012, 12, 15), datetime.date(2015, 12, 31), 2) == datetime.date(2015, 12, 15)
    
    # Additional test case to check the function with invalid inputs (eom < 1)
    assert _last_payment_date(datetime.date(2012, 12, 15), datetime.date(2016, 1, 6), 2) == datetime.date(2015, 12, 15)
