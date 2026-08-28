
import pytest
from ansible.vars.manager import VarsWithSources


def test_initialization_with_data():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    assert isinstance(vs.data, dict)
    assert len(vs.data) == 2

def test_accessing_variable_without_source():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    with pytest.raises(KeyError):  # Accessing a non-existent source should raise KeyError
        print(vs['var3'])  # This will trigger the debug message without source information

def test_setting_and_accessing_variable_source():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    vs.sources['var1'] = 'file_name:line_number'
    assert vs.sources['var1'] == 'file_name:line_number'
    with pytest.raises(KeyError):  # Accessing a non-existent source should raise KeyError
        print(vs['var3'])  # This will trigger the debug message without source information