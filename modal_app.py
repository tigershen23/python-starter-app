import modal

image = modal.Image.debian_slim().poetry_install_from_file("./pyproject.toml")

app = modal.App("myapplication", image=image)


@app.function()
def square(x):
    print("This code is running on a remote worker!")  # noqa: T201
    return x**2


@app.local_entrypoint()
def main():
    from myapplication.main import main as myapp_main

    myapp_main()
    print("the square is", square.remote(42))  # noqa: T201


if __name__ == "__main__":
    main()
