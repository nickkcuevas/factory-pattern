"""
API endpoints for notification system.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from .notifiers import NotifierFactory

router = APIRouter()


class NotificationRequest(BaseModel):
    """Notification request payload."""
    notification_type: str
    message: str
    recipient: str
    config: Dict[str, Any]


@router.post("/notifications/send")
async def send_notification(request: NotificationRequest):
    """Send notification using Factory pattern."""
    try:
        notifier = NotifierFactory.create(
            request.notification_type,
            request.config
        )
        result = notifier.send(request.message, request.recipient)
        return {
            "status": "success",
            "type": request.notification_type,
            "recipient": request.recipient,
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/notifications/types")
async def get_notification_types():
    """Get list of available notification types."""
    return {
        "types": ["email", "sms", "push"],
        "description": "Available notification types"
    }