"""
Unit and regression test for the pylisk package.
"""

# Import package, test suite, and other packages as needed
import pytest
from pylisk.lisk_request import request


@pytest.mark.parametrize(
    "endpoint, query, solution",
    [
        (
            "https://testnet-service.lisk.com/api/v2/",
            "accounts?username=dakk",
            "lskghzw2xnmqshzmk6pkotowmbyebfd2tmezgcm9j",
        ),
    ],
)
def test_request(endpoint, query, solution):
    result = request(endpoint, query)
    print(result)
    assert solution == result[0]["summary"]["address"]


def test_request_exception():
    with pytest.raises(Exception):
        assert request("https://testnet-service.lisk.com/api/", "accounts?username=dakk")
