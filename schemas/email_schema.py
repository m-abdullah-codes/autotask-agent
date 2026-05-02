from pydantic import BaseModel, Field
from typing import Optional

class EmailSummary(BaseModel):
    """Schema for parsing and summarizing an incoming email."""
    
    subject: str = Field(description="The subject line of the email")
    sender: str = Field(description="The email address or name of the sender")
    priority: str = Field(description="Priority of the email: 'high', 'medium', or 'low' based on urgency")
    summary: str = Field(description="A brief 1-2 sentence summary of the email's core message")

class EmailDraft(BaseModel):
    """Schema for drafting a new outbound email."""
    
    recipient: str = Field(description="The email address of the person receiving the email")
    subject: str = Field(description="The subject line for the new email")
    body: str = Field(description="The full text content of the email body")