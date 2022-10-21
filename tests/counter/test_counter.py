from unittest.mock import patch, mock_open
import pytest
from src.counter import count_ocurrences


@pytest.fixture
def context_controlled():
    return [
        "Python python python Python",
        "Missing Typescript :(",
        "Always good to practice! Practice is life.",
    ]


def test_counter(context_controlled):
    with patch("builtins.open", mock_open(read_data=context_controlled[0])):
        assert count_ocurrences("src/jobs.csv", "PYTHON") == 4

    with patch("builtins.open", mock_open(read_data=context_controlled[1])):
        assert count_ocurrences("src/jobs.csv", "typescript") == 1

    with patch("builtins.open", mock_open(read_data=context_controlled[2])):
        assert count_ocurrences("src/jobs.csv", "Practice") == 2
