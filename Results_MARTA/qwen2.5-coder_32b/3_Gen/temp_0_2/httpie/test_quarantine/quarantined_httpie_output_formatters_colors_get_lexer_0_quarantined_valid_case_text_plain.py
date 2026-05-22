
import pytest
from unittest.mock import patch, MagicMock
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name
from pygments.lexers.special import TextLexer
from pygments.lexers.json import JsonLexer
import json

def get_lexer(mime: str, explicit_json=False, body='') -> Optional[Type[Lexer]]:
    # Build candidate mime type and lexer names.
    mime_types, lexer_names = [mime], []
    type_, subtype = mime.split('/', 1)
    if '+' not in subtype:
        lexer_names.append(subtype)
    else:
        subtype_name, subtype_suffix = subtype.split('+', 1)
        lexer_names.extend([subtype_name, subtype_suffix])
        mime_types.extend([
            f'{type_}/{subtype_name}',
            f'{type_}/{subtype_suffix}',
        ])

    # As a last resort, if no lexer feels responsible, and
    # the subtype contains 'json', take the JSON lexer
    if 'json' in subtype:
        lexer_names.append('json')

    # Try to resolve the right lexer.
    lexer = None
    for mime_type in mime_types:
        try:
            lexer = get_lexer_for_mimetype(mime_type)
            break
        except ClassNotFound:
            pass
    else:
        for name in lexer_names:
            try:
                lexer = get_lexer_by_name(name)
            except ClassNotFound:
                pass

    if explicit_json and body and (not lexer or isinstance(lexer, TextLexer)):
        # JSON response with an incorrect Content-Type?
        try:
            json.loads(body)  # FIXME: the body also gets parsed in json.py
        except ValueError:
            pass  # Nope
        else:
            lexer = get_lexer_by_name('json')

    # Use our own JSON lexer: it supports JSON bodies preceded by non-JSON data
    # as well as legit JSON bodies.
    if isinstance(lexer, JsonLexer):
        lexer = EnhancedJsonLexer()

    return lexer

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:6:0: E0401: Unable to import 'pygments.lexers.json' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:6:0: E0611: No name 'json' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:9:58: E0602: Undefined variable 'Optional' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:9:67: E0602: Undefined variable 'Type' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:9:72: E0602: Undefined variable 'Lexer' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:34:15: E0602: Undefined variable 'ClassNotFound' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:40:19: E0602: Undefined variable 'ClassNotFound' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:55:16: E0602: Undefined variable 'EnhancedJsonLexer' (undefined-variable)


"""