import json
import typer
from rich import print
from src.checker import check_password

app = typer.Typer(help="Password Breach Checker (HIBP k-anonymity)")

@app.command()
def check(pwd: str, json_out: bool = False):
    """
    Comprueba una contraseña concreta.
    """
    count = check_password(pwd)
    if json_out:
        print(json.dumps({"password": pwd, "pwned": count > 0, "count": count}))
    else:
        if count:
            print(f"[bold yellow]⚠️ '{pwd}' apareció {count} veces en filtraciones[/]")
        else:
            print(f"[bold green]✅ '{pwd}' no aparece en filtraciones[/]")

@app.command()
def batch(file: str, json_out: bool = False):
    """
    Comprueba varias contraseñas desde un archivo de texto.
    """
    results = {}
    with open(file, "r", encoding="utf-8") as fh:
        for line in fh:
            pwd = line.strip()
            if not pwd:
                continue
            results[pwd] = check_password(pwd)
    if json_out:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for pwd, count in results.items():
            if count:
                print(f"[bold yellow]⚠️ '{pwd}' apareció {count} veces[/]")
            else:
                print(f"[bold green]✅ '{pwd}' no aparece[/]")

if __name__ == "__main__":
    app()
