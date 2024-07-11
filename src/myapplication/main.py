from myapplication.settings import settings


def hello_world() -> str:
    return "Hello World"


def main() -> None:
    print(f"The value of DUMMY_CONFIG is: {settings.dummy_config}")  # noqa: T201


if __name__ == "__main__":
    main()
