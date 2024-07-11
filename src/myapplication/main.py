def hello_world() -> str:
    return "Hello World"


def main() -> None:
    print(hello_world())  # noqa: T201


if __name__ == "__main__":
    main()
