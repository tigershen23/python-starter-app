"""Test the main function of the application."""

from myapplication.main import (
    hello_world,
)


def test_hello_world() -> None:
    """Test the hello_world function."""
    if hello_world() != "Hello World":
        error_msg = 'Expected value to be "Hello World"'
        raise ValueError(
            error_msg,
        )
