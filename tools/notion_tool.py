import os
from dotenv import load_dotenv
from notion_client import Client
from langchain.tools import tool

# Load env
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)


@tool
def create_notion_task(title: str, priority: str = "Medium") -> str:
    """
    Creates a task in Notion database.

    Args:
        title: Task title
        priority: High, Medium, Low
    """

    response = notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {
                "title": [
                    {
                        "text": {"content": title}
                    }
                ]
            },
            "Priority": {
                "select": {"name": priority}
            },
            "Status": {
                "status": {"name": "Not started"}
            }
        }
    )

    return f"Task created in Notion: {response['url']}"


# Standalone test
if __name__ == "__main__":
    result = create_notion_task.invoke({
        "title": "Finish AI agent project",
        "priority": "High"
    })
    print(result)