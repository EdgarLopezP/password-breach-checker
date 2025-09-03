import pytest
from src.checker import hash_password

def test_hash_password():
    # Compruebo que el hash SHA-1 de "password" es el esperado
    assert hash_password("password") == "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8"
