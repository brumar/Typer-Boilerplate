import typer

app = typer.Typer()

def a_function_that_adds_one(x :int)->int:
    return x + 1

@app.command()
def add_one_please(x: int):
    """this function adds one"""
    new_result = a_function_that_adds_one(x)
    typer.echo(f"Result is : {new_result}")

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
