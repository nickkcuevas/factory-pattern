# Factory Pattern Example

Example implementation of the Factory Pattern in Python using FastAPI.

## Setup

1. Install dependencies:
pip install -r requirements.txt

2. python main.py

To run the tests:

$ pytest test_notifiers.py


HOW TO RUN EACH NOTIFIER:


## Email Notifier 

curl -X POST "http://localhost:8000/notifications/send" \
  -H "Content-Type: application/json" \
  -d '{
    "notification_type": "email",
    "message": "Hello from Factory Pattern!",
    "recipient": "user@example.com",
    "config": {
      "smtp_server": "smtp.example.com",
      "port": 587,
      "username": "sender@example.com"
    }
  }'


## SMS Notifier

  curl -X POST "http://localhost:8000/notifications/send" \
  -H "Content-Type: application/json" \
  -d '{
    "notification_type": "sms",
    "message": "Hello from Factory Pattern!",
    "recipient": "+1234567890",
    "config": {
      "api_key": "your-api-key",
      "provider": "twilio"
    }
  }'

## Push Notifier

  curl -X POST "http://localhost:8000/notifications/send" \
  -H "Content-Type: application/json" \
  -d '{
    "notification_type": "push",
    "message": "Hello from Factory Pattern!",
    "recipient": "user123",
    "config": {
      "app_id": "your-app-id",
      "api_secret": "your-secret"
    }
  }'
  