import io
import sys
from notifications import NotificationService, Notifier

class DummyNotifier(Notifier):
    def __init__(self):
        self.messages = []

    def send(self, message: str) -> None:
        self.messages.append(message)

def test_notification_service_calls_notifier():
    dummy = DummyNotifier()
    service = NotificationService(dummy)
    service.notify("hello")
    assert dummy.messages == ["hello"]

def test_cli_output_email(capsys):
    # Capture stdout for a concrete notifier without asserting exact text
    from notifications.notifiers import EmailNotifier
    service = NotificationService(EmailNotifier())
    service.notify("hi")
    captured = capsys.readouterr()
    assert "EMAIL" in captured.out
