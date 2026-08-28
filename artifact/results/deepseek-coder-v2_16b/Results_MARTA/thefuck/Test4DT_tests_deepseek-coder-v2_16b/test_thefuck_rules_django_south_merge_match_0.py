
import pytest
from thefuck.rules.django_south_merge import match
from thefuck.types import Command


def test_invalid_case_without_merge():
    command = Command(script='manage.py migrate', output='Migration completed successfully')
    assert match(command) is False

def test_error_case_with_fake_initial():
    command = Command(script='manage.py migrate --fake-initial', output='Migration completed successfully')
    assert match(command) is False