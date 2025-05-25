# 🔍 PrimeCheck API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-💨-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/github/license/yourname/primecheck-api)

Eine schnelle, API-basierte Primzahlerkennung mit **Python**, **FastAPI** und dem **Miller-Rabin-Algorithmus**.  
Ideal für mathematische Dienste, Lernzwecke oder als Microservice für größere Anwendungen.

---

## 🚀 Features

- Extrem schnelle Primzahlprüfung durch Miller-Rabin-Test
- RESTful JSON-API (`GET /is_prime`)
- Live-Dokumentation via Swagger UI
- Docker-ready ✅
- Getestet mit `pytest`

---

## 🧪 Beispiel

```bash
GET /is_prime?number=997
```

Antwort:
```json
{
  "number": 997,
  "is_prime": true
}
```

---

## 📦 Installation (lokal)

1. Projekt klonen
```bash
git clone https://github.com/deinname/primecheck-api.git
cd primecheck-api
```
2. Umgebung vorbereiten
```bash
pip install -r requirements.txt
```
3. API starten
```bash
uvicorn main:app --reload
```
👉 Swagger UI: http://localhost:8000/docs

---

## 🐳 Docker-Nutzung

🔧 Builden
```bash
docker build -t primecheck-api .
```
▶️ Starten
```bash
docker run -p 8000:8000 primecheck-api
```
👉 Zugriff: http://localhost:8000/is_prime?number=17

---

## 🧪 Tests

Unit-Tests lokal ausführen:
```bash
pytest test_main.py
```

---

## 📁 Projektstruktur
```
.
├── main.py              # API & Primzahlprüfung
├── test_main.py         # Tests der Prüflogik
├── requirements.txt     # Abhängigkeiten
└── Dockerfile           # Container-Konfiguration
```

---

## 📜 Lizenz

MIT License – frei verwendbar, auch kommerziell.

---

## 🤝 Mitwirken
Pull Requests, Ideen oder Bugs?
Starte ein Issue oder sende direkt einen PR. Danke! 😊
