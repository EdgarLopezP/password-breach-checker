[![CI](https://github.com/EdgarLopezP/password-breach-checker/actions/workflows/ci.yml/badge.svg)](https://github.com/EdgarLopezP/password-breach-checker/actions)

# 🔐 Password Breach Checker (HIBP)

Aplicación en **Python** que verifica si una contraseña aparece en filtraciones públicas usando la API de *Pwned Passwords* (Have I Been Pwned) mediante **k-anonymity**.

## 🚀 Uso rápido
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/checker.py

