# Software Design Principles – Notification System (Python)

[//]: # (Replace USERNAME and REPO below after pushing the repo)
[![Python application](https://github.com/USERNAME/REPO/actions/workflows/python-app.yml/badge.svg)](https://github.com/USERNAME/REPO/actions/workflows/python-app.yml)

A tiny, production-style example that demonstrates SOLID design principles using a notification service in Python.

## What’s inside
- **SRP, OCP, LSP, DIP** applied to a real scenario
- `src/notifications/` with abstractions and concrete notifiers
- Unit tests with `pytest`
- GitHub Actions workflow for CI (`.github/workflows/python-app.yml`)

## Quickstart

### 1) Set up a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 2) Install dependencies and run tests
```bash
pip install -r requirements.txt
pytest -q
```

### 3) Run the demo
```bash
python src/main.py --channel email --message "Welcome to our platform!"
python src/main.py --channel sms --message "Your OTP is 123456"
python src/main.py --channel push --message "You have a new message"
```

## Extend: add a new channel
Create a new class that implements `Notifier` (e.g., `SlackNotifier`) and pass it to `NotificationService` without touching existing classes (OCP).

```python
# src/notifications/slack_notifier.py
from .notifiers import Notifier

class SlackNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending SLACK: {message}")

# usage
# from notifications.slack_notifier import SlackNotifier
# NotificationService(SlackNotifier()).notify("Hello Slack!")
```

## CI: GitHub Actions
The pipeline installs dependencies and runs pytest on each push and pull request.

```yaml
# .github/workflows/python-app.yml
name: Python application
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest -q
```

## Project structure
```
.
├── .github/
│   └── workflows/
│       └── python-app.yml
├── src/
│   ├── main.py
│   └── notifications/
│       ├── __init__.py
│       ├── notifiers.py
│       └── service.py
├── tests/
│   └── test_notifications.py
├── .gitignore
├── requirements.txt
└── README.md
```

## License
MIT
