"""
Tests for notifiers module.
"""
import pytest
from app.notifiers import (
    NotifierFactory,
    EmailNotifier,
    SMSNotifier,
    PushNotifier,
)


def test_email_notifier_creation():
    """Test email notifier creation."""
    config = {
        "smtp_server": "smtp.test.com",
        "port": 587,
        "username": "test@test.com"
    }
    notifier = NotifierFactory.create("email", config)
    assert isinstance(notifier, EmailNotifier)
    assert notifier.smtp_server == "smtp.test.com"
    assert notifier.port == 587


def test_sms_notifier_creation():
    """Test SMS notifier creation."""
    config = {
        "api_key": "test-key",
        "provider": "twilio"
    }
    notifier = NotifierFactory.create("sms", config)
    assert isinstance(notifier, SMSNotifier)
    assert notifier.api_key == "test-key"
    assert notifier.provider == "twilio"


def test_push_notifier_creation():
    """Test push notifier creation."""
    config = {
        "app_id": "test-app-id",
        "api_secret": "test-secret"
    }
    notifier = NotifierFactory.create("push", config)
    assert isinstance(notifier, PushNotifier)
    assert notifier.app_id == "test-app-id"


def test_invalid_notification_type():
    """Test invalid notification type."""
    with pytest.raises(ValueError, match="Unknown notification type"):
        NotifierFactory.create("invalid", {})


def test_email_notifier_send():
    """Test email notifier send method."""
    notifier = EmailNotifier(
        smtp_server="smtp.test.com",
        port=587,
        username="test@test.com"
    )
    result = notifier.send("Test message", "recipient@test.com")
    assert result is True


def test_sms_notifier_send():
    """Test SMS notifier send method."""
    notifier = SMSNotifier(
        api_key="test-key",
        provider="twilio"
    )
    result = notifier.send("Test message", "+1234567890")
    assert result is True


def test_push_notifier_send():
    """Test push notifier send method."""
    notifier = PushNotifier(
        app_id="test-app-id",
        api_secret="test-secret"
    )
    result = notifier.send("Test message", "user123")
    assert result is True