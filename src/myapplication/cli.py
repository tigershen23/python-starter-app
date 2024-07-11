import typer

app = typer.Typer()


@app.command()
def main(name: str, lastname: str = "", formal: bool = False) -> None:
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")  # noqa: T201
    else:
        print(f"Hello {name} {lastname}")  # noqa: T201


if __name__ == "__main__":
    app()
