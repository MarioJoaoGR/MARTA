# Module: tornado.util
import unittest
from tornado.util import doctests

def test_module():
    suite = doctests()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
