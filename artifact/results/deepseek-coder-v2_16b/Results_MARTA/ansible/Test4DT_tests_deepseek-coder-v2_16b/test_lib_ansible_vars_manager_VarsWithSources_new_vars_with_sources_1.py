
import pytest
from ansible.vars.manager import VarsWithSources


def test_setting_source_information():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    vs.sources['var1'] = 'file_name:line_number'
    assert 'var1' in vs.sources
    assert vs.sources['var1'] == 'file_name:line_number'

def test_accessing_variable_with_source():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    vs.sources['var1'] = 'file_name:line_number'
    assert vs['var1'] == 1
    assert vs.sources['var1'] == 'file_name:line_number'