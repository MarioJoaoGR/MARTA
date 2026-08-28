
import pytest

def expand_abbreviations(template, abbreviations):
    """Expand abbreviations in a template name.

    :param template: The project template name.
    :param abbreviations: Abbreviation definitions.
    """
    if template in abbreviations:
        return abbreviations[template]

    # Split on colon. If there is no colon, rest will be empty
    # and prefix will be the whole template
    prefix, sep, rest = template.partition(':')
    if prefix in abbreviations:
        return abbreviations[prefix].format(rest)

    return template



def test_expand_abbreviations_no_colon():
    result = expand_abbreviations('doc', {'doc': 'documentation'})
    assert result == 'documentation'

def test_expand_abbreviations_with_colon():
    result = expand_abbreviations('proj:api', {'proj': 'project-{}'})
    assert result == 'project-api'

def test_expand_abbreviations_no_match():
    result = expand_abbreviations('unknown', {})
    assert result == 'unknown'

def test_expand_abbreviations_complex_template():
    result = expand_abbreviations('feat:user-auth', {'feat': 'feature-{}'})
    assert result == 'feature-user-auth'

def test_expand_abbreviations_no_matching_prefix():
    result = expand_abbreviations('test:case1', {})
    assert result == 'test:case1'