from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        """Send a message via a specific channel."""
        raise NotImplementedError

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending EMAIL: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")

class PushNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending PUSH: {message}")
