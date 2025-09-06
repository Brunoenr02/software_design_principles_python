import argparse
from notifications import (
    NotificationService,
    EmailNotifier,
    SMSNotifier,
    PushNotifier,
)

CHANNELS = {
    "email": EmailNotifier,
    "sms": SMSNotifier,
    "push": PushNotifier,
}

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Notification System Demo (SOLID)")
    parser.add_argument("--channel", choices=CHANNELS.keys(), required=True, help="Notification channel")
    parser.add_argument("--message", required=True, help="Message to send")
    return parser

def main() -> None:
    args = build_parser().parse_args()
    notifier_cls = CHANNELS[args.channel]
    service = NotificationService(notifier_cls())
    service.notify(args.message)

if __name__ == "__main__":
    main()
