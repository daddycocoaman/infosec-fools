import typer
from rich import print
from rich.prompt import Confirm

app = typer.Typer(
    name="infosec_fools", help="CLI tool to determine if you are an infosec fool"
)


@app.command()
def main():
    prompt = Confirm.ask(
        ":question_mark: Hi, are you going to Hacker Summer Camp 2022?"
    )
    if prompt:
        print(
            ":clown_face: :clown_face: :clown_face: [yellow]You are an infosec fool![/yellow] :clown_face: :clown_face: :clown_face:\n"
        )
    else:
        print(
            ":crown: :crown: :crown: [green]You are not an infosec fool![/green] :crown: :crown: :crown:"
        )


if __name__ == "__main__":
    app()
