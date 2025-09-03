import hashlib
import requests
from getpass import getpass

API_URL = "https://api.pwnedpasswords.com/range/"

def hash_password(password: str) -> str:
    # Genero el hash SHA-1 de la contraseña en mayúsculas
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

def check_password(password: str) -> int:
    # Separo el hash en prefijo (5 chars) y sufijo (resto)
    sha1 = hash_password(password)
    prefix, suffix = sha1[:5], sha1[5:]

    # Pregunto a la API solo con el prefijo (no mando tu contraseña completa)
    response = requests.get(API_URL + prefix)
    if response.status_code != 200:
        raise RuntimeError("Error al conectar con la API")

    # Recorro la respuesta de la API y busco si mi sufijo aparece
    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)

    return 0

if __name__ == "__main__":
    pwd = getpass("Introduce una contraseña: ")
    veces = check_password(pwd)
    if veces:
        print(f"⚠️ Tu contraseña aparece {veces} veces en filtraciones")
    else:
        print("✅ Tu contraseña no aparece en filtraciones")
