from .notifiers import Notifier

class NotificationService:
    """High-level service that depends on the Notifier abstraction (DIP)."""
    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    def notify(self, message: str) -> None:
        self._notifier.send(message)
