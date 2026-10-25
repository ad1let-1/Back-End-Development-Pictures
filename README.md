# Back-End-Development-Pictures

This is the public README for my **Back-End-Development-Pictures** repository:
https://github.com/ad1let-1/Back-End-Development-Pictures/blob/main/README.md

Flask REST service for Djirection concert photographs. Based on the IBM Skills Network course template, licensed under Apache 2.0. The REST handlers are implemented and the included test suite passes.

## Run locally

```sh
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m flask --app app run --port 8082
```

On Windows, use `.venv\\Scripts\\python.exe` in place of `.venv/bin/python`.

## API

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/health` | Service status |
| GET | `/count` | Number of stored photos |
| GET | `/picture` | All photos |
| GET | `/picture/<id>` | One photo |
| POST | `/picture` | Add a photo |
| PUT | `/picture/<id>` | Update a photo |
| DELETE | `/picture/<id>` | Remove a photo |

Data is loaded from `backend/data/pictures.json` at startup. Writes are held in memory for this course exercise.

## Test

```sh
python -m pytest -v tests/test_api.py
```

The included suite contains 11 tests covering health, count, GET, POST, PUT, and DELETE behavior.
