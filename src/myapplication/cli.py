"""Command Line Interface module for the application."""

import typer

from myapplication.main import (
    hello_world,
)

app = typer.Typer()


@app.command()
def main(
    name: str,
) -> None:
    """Say hi to NAME."""
    print(  # noqa: T201
        hello_world(),
    )
    print(  # noqa: T201
        name,
    )


if __name__ == "__main__":
    app()
