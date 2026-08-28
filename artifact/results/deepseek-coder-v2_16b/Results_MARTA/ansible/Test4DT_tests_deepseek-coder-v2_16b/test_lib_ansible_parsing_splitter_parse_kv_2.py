
import pytest
from ansible.parsing.splitter import split_args
from ansible.errors import AnsibleParserError
from ansible.utils import to_text, unquote

def parse_kv(args, check_raw=False):
    '''
    Convert a string of key/value items to a dict. If any free-form params
    are found and the check_raw option is set to True, they will be added
    to a new parameter called '_raw_params'. If check_raw is not enabled,
    they will simply be ignored.
    '''

    args = to_text(args, nonstring='passthru')

    options = {}
    if args is not None:
        try:
            vargs = split_args(args)
        except IndexError as e:
            raise AnsibleParserError("Unable to parse argument string", orig_exc=e)
        except ValueError as ve:
            if 'no closing quotation' in str(ve).lower():
                raise AnsibleParserError("error parsing argument string, try quoting the entire line.", orig_exc=ve)
            else:
                raise

        raw_params = []
        for orig_x in vargs:
            x = unquote(orig_x)  # Decode escaped characters
            if "=" in x:
                pos = 0
                try:
                    while True:
                        pos = x.index('=', pos + 1)
                        if pos > 0 and x[pos - 1] != '\\':
                            break
                except ValueError:
                    # Ran out of string, but we must have some escaped equals,
                    # so replace those and append this to the list of raw params
                    raw_params.append(x.replace('\\=', '='))
                    continue

                k = x[:pos]
                v = x[pos + 1:]

                if check_raw and k not in ('creates', 'removes', 'chdir', 'executable', 'warn', 'stdin', 'stdin_add_newline', 'strip_empty_ends'):
                    raw_params.append(orig_x)
                else:
                    options[k.strip()] = v.strip()
            else:
                raw_params.append(orig_x)

        if len(raw_params) > 0:
            options['_raw_params'] = ' '.join(raw_params)

    return options

# Test cases
def test_valid_input_happy_path():
    args = 'key1=value1 key2="value with spaces"'
    result = parse_kv(args)
    assert result == {'key1': 'value1', 'key2': 'value with spaces'}

def test_valid_input_with_check_raw():
    args = 'arg1=value1 arg2="another value"'
    result = parse_kv(args, check_raw=True)
    assert result == {'_raw_params': 'arg1=value1 arg2="another value"'}

def test_invalid_input_error_handling():
    args = 'malformed'
    with pytest.raises(AnsibleParserError):
        parse_kv(args)
