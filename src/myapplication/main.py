"""Main module for the application."""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s [%(filename)s:%(lineno)s] %(message)s")
logger = logging.getLogger(__name__)

from myapplication.settings import (  # noqa: E402
    settings,
)


def hello_world() -> str:
    """Return a greeting message."""
    return "Hello World"


def main() -> None:
    """Print the value of DUMMY_CONFIG from settings."""
    logging.info(
        "The value of DUMMY_CONFIG is: %s",
        settings.dummy_config,
    )


if __name__ == "__main__":
    main()
