import json
from typer.testing import CliRunner
from src.cli import app

runner = CliRunner()

def test_check_command_json(monkeypatch):
    # Simulo la respuesta: la contraseña aparece 5 veces
    monkeypatch.setattr("src.cli.check_password", lambda pwd: 5)
    result = runner.invoke(app, ["check", "perro123", "--json-out"])
    assert result.exit_code == 0
    assert '"pwned": true' in result.stdout
    assert '"count": 5' in result.stdout

def test_batch_command_json(monkeypatch, tmp_path):
    # Simulo: "segura" no aparece; cualquier otra aparece 10 veces
    monkeypatch.setattr("src.cli.check_password",
                        lambda pwd: 0 if pwd == "segura" else 10)
    file_path = tmp_path / "contrasenas.txt"
    file_path.write_text("segura\nqwerty\n", encoding="utf-8")

    result = runner.invoke(app, ["batch", str(file_path), "--json-out"])
    assert result.exit_code == 0

    data = json.loads(result.stdout)
    assert data["segura"] == 0
    assert data["qwerty"] == 10
