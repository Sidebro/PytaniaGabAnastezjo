# Losowanie pytan

Prosta strona z backendem w Pythonie. Pytania sa losowane po stronie serwera i zwracane do frontendu przez API.

## Uruchomienie lokalne

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Po uruchomieniu wejdz na adres:

```text
http://127.0.0.1:5000
```

## Railway

Projekt jest przygotowany pod Railway:

- aplikacja czyta port z `PORT`
- produkcyjny start jest przez `gunicorn`
- `Procfile` wskazuje komende startowa

Kroki:

1. Wrzuc projekt do repozytorium GitHub.
2. W Railway wybierz `New Project`.
3. Podlacz repozytorium.
4. Railway powinno automatycznie wykryc Pythona i zainstalowac zaleznosci z `requirements.txt`.
5. Po deployu otworz wygenerowany publiczny adres.

Jesli Railway nie wykryje startu automatycznie, ustaw Start Command recznie na:

```text
gunicorn app:app --bind 0.0.0.0:$PORT
```
