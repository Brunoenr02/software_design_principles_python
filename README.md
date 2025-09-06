# Software Design Principles – Notification System (Python)

[![Python application](https://github.com/Brunoenr02/software_design_principles_python/actions/workflows/python-app.yml/badge.svg)](https://github.com/Brunoenr02/software_design_principles_python/actions/workflows/python-app.yml)

A tiny, production-style example that demonstrates **SOLID design principles** using a notification service in Python.

## 🎯 Design Principles Demonstrated

### **S** - Single Responsibility Principle (SRP)
- Each notifier class has only one responsibility: sending notifications via its specific channel
- `NotificationService` has only one responsibility: orchestrating the notification process

### **O** - Open/Closed Principle (OCP)
- Easy to add new notification channels without modifying existing code
- Just implement the `Notifier` interface and plug it in

### **L** - Liskov Substitution Principle (LSP)
- All notifier implementations are interchangeable
- `EmailNotifier`, `SMSNotifier`, and `PushNotifier` can be substituted without breaking functionality

### **I** - Interface Segregation Principle (ISP)
- The `Notifier` interface is minimal and focused
- No client is forced to depend on methods it doesn't use

### **D** - Dependency Inversion Principle (DIP)
- `NotificationService` depends on the `Notifier` abstraction, not concrete implementations
- High-level modules don't depend on low-level modules

## What's inside
- **Complete SOLID implementation** with a practical notification system
- `src/notifications/` with abstractions and concrete notifiers
- Unit tests with `pytest` demonstrating testability
- GitHub Actions workflow for CI/CD
- Extensible architecture for adding new notification channels

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

## 🚀 Extend: Add a new channel (OCP in action)
Create a new class that implements `Notifier` without touching existing classes:

```python
# src/notifications/slack_notifier.py
from .notifiers import Notifier

class SlackNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending SLACK: {message}")

# Register in main.py
def create_notifier(channel: str) -> Notifier:
    notifiers = {
        "email": EmailNotifier(),
        "sms": SMSNotifier(),
        "push": PushNotifier(),
        "slack": SlackNotifier(),  # ← New channel added!
    }
    return notifiers[channel]
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

## 🏗️ Architecture Benefits

- **Maintainable**: Changes to one notifier don't affect others
- **Testable**: Easy to mock and unit test each component
- **Extensible**: Add new notification channels effortlessly
- **Readable**: Clear separation of concerns and responsibilities
- **Type-safe**: Full type hints for better IDE support

## 🧪 Testing Strategy
- Unit tests for each notifier implementation
- Integration tests for the notification service
- Mocking examples for external dependencies
- CI pipeline ensures code quality

## Project structure
```
.
├── .github/
│   └── workflows/
│       └── python-app.yml       # CI/CD pipeline
├── src/
│   ├── main.py                  # CLI demo application
│   └── notifications/
│       ├── __init__.py          # Package exports
│       ├── notifiers.py         # Abstract base + implementations
│       └── service.py           # Main service orchestrator
├── tests/
│   └── test_notifications.py   # Comprehensive test suite
├── .gitignore
├── requirements.txt
└── README.md
```

## License
MIT
