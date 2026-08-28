
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

def test_expand_abbreviations_basic():
    """Test basic functionality of expand_abbreviations."""
    template = 'proj:api'
    abbreviations = {'proj': 'project-{}'}
    expected_result = 'project-api'
    
    result = expand_abbreviations(template, abbreviations)
    assert result == expected_result
