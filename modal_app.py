"""Modal application for the project."""

import modal

image = modal.Image.debian_slim().poetry_install_from_file(
    "./pyproject.toml",
)

app = modal.App(
    "myapplication",
    image=image,
)


@app.function()
def square(
    x: int,
) -> int:
    """Calculate the square of a number."""
    print(  # noqa: T201
        "This code is running on a remote worker!",
    )
    return x**2


@app.local_entrypoint()
def main() -> None:
    """Run the main function of the application."""
    from myapplication.main import (
        main as myapp_main,
    )

    myapp_main()
    print(  # noqa: T201
        "the square is",
        square.remote(
            42,
        ),
    )


if __name__ == "__main__":
    main()  # pyright: ignore [reportOptionalCall]
