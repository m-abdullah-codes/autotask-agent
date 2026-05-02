import os
import datetime
from dotenv import load_dotenv

from langchain.tools import tool

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Load env variables
load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.modify"
]


def get_calendar_service():
    creds = None

    # token.json stores user access/refresh tokens
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If not valid, login again
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save credentials
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service


@tool
def create_calendar_event(title: str, start_time: str, end_time: str) -> str:
    """
    Creates a Google Calendar event.
    
    Args:
        title: Event title
        start_time: ISO format datetime (e.g. 2026-05-02T10:00:00)
        end_time: ISO format datetime (e.g. 2026-05-02T11:00:00)
    """

    service = get_calendar_service()

    event = {
        "summary": title,
        "start": {
            "dateTime": start_time,
            "timeZone": "Asia/Karachi",
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "Asia/Karachi",
        },
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    return f"Event created: {created_event.get('htmlLink')}"


# Standalone test
if __name__ == "__main__":
    result = create_calendar_event.invoke({
        "title": "Test Meeting",
        "start_time": "2026-05-04T10:00:00",
        "end_time": "2026-05-04T11:00:00"
    })
    print(result)