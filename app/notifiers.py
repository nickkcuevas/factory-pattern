from abc import ABC, abstractmethod


class Notifier(ABC):
    """Base class for all notifiers."""
    
    @abstractmethod
    def send(self, message: str, recipient: str) -> bool:
        raise NotImplementedError


class NotifierFactory:
    '''
    Disclaimer: This Notifier will be modified every time a new notification type is being added.
    The goal here is that we are actually not modifying the business logic, but instead
    adding a new Notifier every time is needed here. 
      So for example if we add an SlackNotifier, we could start by just adding tests, making sure that 
    that factory actually does what we want, and only after that, we should add it here.
    '''
    
    @staticmethod
    def create(notification_type: str, config: dict) -> Notifier:
        """Create a notifier instance based on type."""
        if notification_type == "email":
            return EmailNotifier(
                smtp_server=config.get("smtp_server", "smtp.example.com"),
                port=config.get("port", 587),
                username=config.get("username")
            )
        elif notification_type == "sms":
            return SMSNotifier(
                api_key=config.get("api_key"),
                provider=config.get("provider", "twilio")
            )
        elif notification_type == "push":
            return PushNotifier(
                app_id=config.get("app_id"),
                api_secret=config.get("api_secret")
            )
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")


# ============================================
# Implementations
# ============================================

class EmailNotifier(Notifier):
    """Email notification implementation."""
    
    def __init__(self, smtp_server: str, port: int, username: str):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
    
    def send(self, message: str, recipient: str) -> bool:
        print(f"[Email] Sending to {recipient} via {self.smtp_server}:{self.port}")
        print(f"Message: {message}")
        return True


class SMSNotifier(Notifier):
    """SMS notification implementation."""
    
    def __init__(self, api_key: str, provider: str):
        self.api_key = api_key
        self.provider = provider
    
    def send(self, message: str, recipient: str) -> bool:
        print(f"[SMS] Sending to {recipient} via {self.provider}")
        print(f"Message: {message}")
        return True


class PushNotifier(Notifier):
    """Push notification implementation."""
    
    def __init__(self, app_id: str, api_secret: str):
        self.app_id = app_id
        self.api_secret = api_secret
    
    def send(self, message: str, recipient: str) -> bool:
        print(f"[Push] Sending to {recipient} (App ID: {self.app_id})")
        print(f"Message: {message}")
        return True