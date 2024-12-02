import requests
from dotenv import load_dotenv
import os
import typer
from rich.console import Console
from rich.text import Text

# Load variables from the .env file
load_dotenv()
app = typer.Typer()
console = Console()
session_id = os.getenv('AOC_SESSION')


@app.command()
def init_day(day: int, year: int) -> None:
    # creating folder
    path = str(year) + '/day' + str(day)
    os.makedirs(path, exist_ok=True)

    # get data
    url = 'https://adventofcode.com/' + \
        str(year) + '/day/' + str(day) + '/input'
    cookies = {'session': session_id}

    r = requests.get(url, cookies=cookies)

    # create file
    file_path_program = os.path.join(path, 'day' + str(day)+'.py')
    file_path_input = os.path.join(path, 'input.txt')
    if not os.path.exists(file_path_program):
        with open(file_path_program, 'w') as file:
            pass
        console.print(Text(f"File {file_path_program} created.", style="green"))
    else:
        console.print(Text(f"File {file_path_program} already exists; skipping creation.", style="yellow"))

    if not os.path.exists(file_path_input):
        with open(file_path_input, 'w') as file:
            file.write(r.text)
            console.print(Text(f"File {file_path_input} created and data written.", style="green"))
    else:
        console.print(Text(f"File {file_path_input} already exists; skipping creation.", style="yellow"))


if __name__ == "__main__":
    app()
