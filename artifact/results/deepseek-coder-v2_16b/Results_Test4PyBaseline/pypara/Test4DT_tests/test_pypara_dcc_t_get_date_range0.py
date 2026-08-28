# Module: pypara.dcc
import pytest
import datetime
from typing import List, Iterable
from pypara.dcc import _get_date_range

# Helper function to convert list of dates to strings for easy comparison
def date_list_to_str_list(dates: List[datetime.date]) -> List[str]:
    return [date.strftime("%Y-%m-%d") for date in dates]

def test_get_date_range():
    # Define the start and end dates
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 1, 5)
    
    # Call the function
    date_range = list(_get_date_range(start_date, end_date))
    
    # Convert to string for comparison
    expected_dates = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), datetime.date(2023, 1, 4)]
    expected_str_dates = date_list_to_str_list(expected_dates)
    
    # Assert the result
    assert date_list_to_str_list(date_range) == expected_str_dates

def test_get_date_range_with_strings():
    # Define the start and end dates using strings for readability
    start_date = "2023-01-01"
    end_date = "2023-01-05"
    
    # Convert string dates to datetime.date objects
    start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    
    # Call the function
    date_range = list(_get_date_range(start_date_obj, end_date_obj))
    
    # Convert to string for comparison
    expected_dates = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), datetime.date(2023, 1, 4)]
    expected_str_dates = date_list_to_str_list(expected_dates)
    
    # Assert the result
    assert date_list_to_str_list(date_range) == expected_str_dates

def test_get_date_range_with_specific_format():
    # Define the start and end dates using a specific format
    start_date = "Jan 1, 2023"
    end_date = "Jan 5, 2023"
    
    # Convert string dates to datetime.date objects
    start_date_obj = datetime.datetime.strptime(start_date, "%b %d, %Y").date()
    end_date_obj = datetime.datetime.strptime(end_date, "%b %d, %Y").date()
    
    # Call the function
    date_range = list(_get_date_range(start_date_obj, end_date_obj))
    
    # Convert to string for comparison
    expected_dates = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), datetime.date(2023, 1, 4)]
    expected_str_dates = date_list_to_str_list(expected_dates)
    
    # Assert the result
    assert date_list_to_str_list(date_range) == expected_str_dates

# Add more test cases as needed to cover different scenarios and edge cases.
