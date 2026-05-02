import os
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from langchain_google_community import GmailToolkit

def get_gmail_tools():
    """
    Authenticates with Google and returns the list of Gmail tools.
    """
    # Step 1: Handle Authentication
    # This looks for your credentials.json and will pop up a browser window
    # the first time you run it. It saves your login state in token.json.
    credentials = get_gmail_credentials(
        token_file="token.json",
        scopes=[    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.modify"], # Full access so the agent can read/send later
    )
    
    # Step 2: Build the API Resource
    api_resource = build_resource_service(credentials=credentials)
    
    # Step 3: Initialize the Toolkit
    toolkit = GmailToolkit(api_resource=api_resource)
    
    # Return the raw tools (Search, Get Message, Send Message, etc.)
    return toolkit.get_tools()

# --- STANDALONE TESTING ---
# This block ONLY runs if you run this file directly (python tools/gmail_tool.py)
# It will NOT run when you import these tools into your agent later.
if __name__ == "__main__":
    print("🛠️ Initializing Gmail Toolkit...")
    tools = get_gmail_tools()
    
    # Print out the tools LangChain built for us
    print(f"✅ Loaded {len(tools)} tools: {[t.name for t in tools]}")
    
    # Find the specific tool used for searching emails
    search_tool = next(t for t in tools if t.name == "search_gmail")
    
    print("\n📥 Fetching 5 recent emails from your inbox...")
    
    try:
        # We invoke the tool with a dictionary matching its expected inputs
        results = search_tool.invoke({
            "query": "in:inbox", 
            "max_results": 5
        })
        print("\n🎉 Success! Here is the raw data we found:")
        print("-" * 50)
        print(results)
        print("-" * 50)
    except Exception as e:
        print(f"\n❌ Error fetching emails: {e}")