
import pytest
from ansible.vars.reserved import _RESERVED_NAMES
from unittest.mock import patch

def warn_if_reserved(myvars, additional=None):
    ''' this function warns if any variable passed conflicts with internally reserved names '''

    if additional is None:
        reserved = _RESERVED_NAMES
    else:
        reserved = _RESERVED_NAMES.union(additional)

    varnames = set(myvars)
    varnames.discard('vars')  # we add this one internally, so safe to ignore
    for varname in varnames.intersection(reserved):
        print('Found variable using reserved name: %s' % varname)

@pytest.mark.parametrize("myvars, additional", [
    (['var1', 'var2', 'vars'], None),
    (['var1', 'var2'], {'myvar'}),
    (None, None)
])
def test_warn_if_reserved(myvars, additional):
    with patch('builtins.print') as mock_print:
        warn_if_reserved(myvars, additional)
        
        if myvars is None and additional is None:
            assert not mock_print.called
        elif 'vars' in (myvars or []) and additional is None:
            mock_print.assert_called_once_with('Found variable using reserved name: vars')
        elif 'myvar' in (myvars or []) and additional == {'myvar'}:
            mock_print.assert_called_once_with('Found variable using reserved name: myvar')
