
import pytest
from unittest.mock import patch, MagicMock
from pypara.accounting.journaling import JournalEntry, Posting
from datetime import date

# Test scenario 1: Valid credits should return only credit postings

# Test scenario 2: JournalEntry with no postings should return an empty iterable
def test_no_postings():
    with patch('pypara.accounting.journaling.JournalEntry') as mock_journal_entry:
        # Arrange
        mock_journal_entry.return_value.postings = []

        journal_entry = mock_journal_entry()

        # Act
        credit_postings = journal_entry.credits()

        # Assert
        assert list(credit_postings) == [], "Expected an empty list for no postings"

# Test scenario 3: JournalEntry with only debit postings should return an empty iterable
def test_only_debits():
    with patch('pypara.accounting.journaling.JournalEntry') as mock_journal_entry:
        # Arrange
        mock_debit_posting = MagicMock()
        mock_debit_posting.is_credit = False
        mock_journal_entry.return_value.postings = [mock_debit_posting]

        journal_entry = mock_journal_entry()

        # Act
        credit_postings = journal_entry.credits()

        # Assert
        assert list(credit_postings) == [], "Expected an empty list for only debits"