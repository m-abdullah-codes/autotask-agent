from pydantic import BaseModel, Field

class NotionTask(BaseModel):
    """Schema for creating a new task in Notion."""
    
    title: str = Field(description="The title or main objective of the task")
    priority: str = Field(default="Medium", description="Task priority: 'High', 'Medium', or 'Low'")

class CalendarEvent(BaseModel):
    """Schema for creating a Google Calendar event."""
    
    title: str = Field(description="The title of the calendar event")
    start_time: str = Field(description="Start time in ISO format without Z (e.g., 2026-05-02T14:00:00)")
    end_time: str = Field(description="End time in ISO format without Z (e.g., 2026-05-02T15:00:00)")