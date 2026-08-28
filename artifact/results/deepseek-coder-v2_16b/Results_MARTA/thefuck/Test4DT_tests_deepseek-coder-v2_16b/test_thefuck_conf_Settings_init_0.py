
import pytest
from thefuck.conf import Settings
import argparse

def test_init_with_default_args():
    settings = Settings()
    settings.init()
    assert hasattr(settings, 'debug') and not getattr(settings, 'debug'), "Default debug setting should be False"


def test_init_with_env_var():
    import os
    os.environ['THEFUCK_DEBUG'] = 'True'
    
    settings = Settings()
    settings.init()
    assert hasattr(settings, 'debug') and getattr(settings, 'debug'), "Debug setting should be enabled with environment variable"