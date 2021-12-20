"""
Unit and regression test for the pylisk package.
"""

# Import package, test suite, and other packages as needed
import sys
from pylisk.account import Account


def test_pylisk_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "pylisk" in sys.modules
