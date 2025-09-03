# Orquesto la CLI y delego en check_password()
import json
import typer
from rich import print
from src.checker import check_password

app = typer.Typer(help="Password Breach Checker (HIBP k-anonymity)")

@app.command()
def check(pwd: str, json_out: bool = False):
    # Aquí resuelvo un único password desde argumento (no echo por seguridad)
    count = check_password(pwd)
    if json_out:
        print(json.dumps({"pwned": count > 0, "count": count}))
    else:
        print(f"[bold yellow]⚠️ {count}[/] veces" if count else "[bold green]✅ No aparece[/]")

@app.command()
def batch(file: str, json_out: bool = False):
    # Aquí recorro un archivo con una contraseña por línea (con cuidado)
    results = {}
    with open(file, "r", encoding="utf-8") as fh:
        for line in fh:
            pwd = line.strip()
            if not pwd:
                continue
            results[pwd] = check_password(pwd)
    if json_out:
        print(json.dumps(results, ensure_ascii=False))
    else:
        for pwd, count in results.items():
            print(f"{pwd}: {count}")

if __name__ == "__main__":
    app()
