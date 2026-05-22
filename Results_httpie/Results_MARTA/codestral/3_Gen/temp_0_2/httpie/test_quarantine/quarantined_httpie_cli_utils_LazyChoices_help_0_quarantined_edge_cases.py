
import unittest
from httpie.cli.utils import LazyChoices
from typing import Callable, Iterable, Optional

class TestLazyChoices(unittest.TestCase):
    def test_lazy_choices_initialization(self):
        getter = lambda: [1, 2, 3]
        choices = LazyChoices(getter=getter)
        self.assertEqual(list(choices.load()), [1, 2, 3])

    def test_lazy_choices_with_sorting(self):
        getter = lambda: [3, 1, 2]
        choices = LazyChoices(getter=getter, sort=True)
        self.assertEqual(list(choices.load()), [1, 2, 3])

    def test_lazy_choices_with_caching(self):
        getter = lambda: [4, 5, 6]
        choices = LazyChoices(getter=getter)
        first_load = choices.load()
        second_load = choices.load()
        self.assertIs(first_load, second_load)

    def test_lazy_choices_without_caching(self):
        getter = lambda: [7, 8, 9]
        choices = LazyChoices(getter=getter, cache=False)
        first_load = choices.load()
        second_load = choices.load()
        self.assertIsNot(first_load, second_load)

    def test_lazy_choices_with_isolation_mode(self):
        getter = lambda: [10, 11, 12]
        choices = LazyChoices(getter=getter, isolation_mode=True)
        first_load = choices.load()
        second_load = choices.load()
        self.assertIsNot(first_load, second_load)

    def test_lazy_choices_with_help_formatter(self):
        getter = lambda: ["apple", "banana", "cherry"]
        help_formatter = lambda items, isolation_mode: "\n".join([str(item) for item in items])
        choices = LazyChoices(getter=getter, help_formatter=help_formatter)
        self.assertEqual(choices.help(), "apple\nbanana\ncherry")

    def test_lazy_choices_with_sorting_and_isolation_mode(self):
        getter = lambda: ["c", "a", "b"]
        choices = LazyChoices(getter=getter, sort=True, isolation_mode=True)
        self.assertEqual(list(choices.load()), ['a', 'b', 'c'])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_utils_LazyChoices_help_0_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_cli_utils_LazyChoices_help_0_test_edge_cases.py:42:25: E1102: choices.help is not callable (not-callable)


"""