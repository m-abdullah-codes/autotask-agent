# 🤖 AutoTask — Personal Productivity AI Agent

An AI-powered productivity agent that autonomously manages your Gmail, Google Calendar, and Notion — built with LangChain, Fireworks AI, and Streamlit.

---

## 🎯 What It Does

AutoTask lets you talk to your productivity tools in plain English. Give it a goal, and it figures out the steps, calls the right tools, and gets it done.

**Example prompts:**
- *"Summarize my unread emails and create Notion tasks for the urgent ones"*
- *"Schedule a 1-hour deep work block tomorrow morning"*
- *"Send a reply to John's email saying I'll get back to him by Friday"*

---

## ✨ Features

| Feature | Description |
|---|---|
| 📧 **Gmail Reading** | Reads and intelligently summarizes your emails |
| ✉️ **Gmail Sending** | Drafts and sends replies on your behalf |
| 📅 **Calendar Scheduling** | Creates and manages Google Calendar events |
| ✅ **Notion Task Creation** | Automatically creates tasks in your Notion workspace |
| 🧠 **Conversation Memory** | Remembers context across the conversation session |
| 💬 **Natural Language Interface** | Just describe what you want — no commands to learn |

---

## 🏗️ Architecture

```
User Input (Streamlit UI)
        ↓
  LangChain ReAct Agent
  (MiniMax-M1 via Fireworks AI)
        ↓
  ┌─────────────────────────────────────┐
  │         Tool Selection Loop         │
  │                                     │
  │  📧 Gmail Tool (read + send)        │
  │  📅 Google Calendar Tool            │
  │  ✅ Notion Tool                     │
  │  📝 Summarizer Tool (Qwen3-8B)      │
  └─────────────────────────────────────┘
        ↓
  Conversation Memory
  (ConversationBufferMemory)
        ↓
  Final Response → Streamlit UI
```

**How the ReAct loop works:**
1. **Reason** — The agent thinks about what tools it needs
2. **Act** — It calls the appropriate tool (Gmail, Calendar, Notion)
3. **Observe** — It reads the tool's output
4. **Repeat** — Until the goal is achieved, then returns the final answer

---

## 🧩 Tech Stack

| Component | Technology |
|---|---|
| **Agent Framework** | LangChain (ReAct Agent + AgentExecutor) |
| **Agent LLM** | MiniMax-M1 via Fireworks AI |
| **Summarizer LLM** | Qwen3-8B via Fireworks AI |
| **Email** | Gmail API (LangChain Gmail Toolkit) |
| **Calendar** | Google Calendar API (custom tool) |
| **Tasks** | Notion API (custom tool) |
| **Memory** | LangChain ConversationBufferMemory |
| **UI** | Streamlit |
| **Auth** | OAuth 2.0 (Google), API Token (Notion) |

---

## 📁 Project Structure

```
autotask-agent/
│
├── main.py                    # Entry point
│
├── agent/
│   ├── agent.py               # AgentExecutor setup
│   ├── memory.py              # Conversation memory
│   └── prompts.py             # System prompt templates
│
├── tools/
│   ├── gmail_tool.py          # Gmail read + send (LangChain toolkit)
│   ├── calendar_tool.py       # Google Calendar events (custom)
│   ├── notion_tool.py         # Notion task creation (custom)
│   └── summarizer_tool.py     # LLM-powered summarizer (custom)
│
├── schemas/
│   ├── email_schema.py        # Pydantic model for emails
│   └── task_schema.py         # Pydantic model for tasks
│
├── config/
│   └── settings.py            # Loads environment variables
│
├── ui/
│   └── app.py                 # Streamlit chat interface
│
├── .env.example               # Environment variable template
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Fireworks AI](https://fireworks.ai) account (for LLM access)
- A [Google Cloud](https://console.cloud.google.com) project with Gmail + Calendar APIs enabled
- A [Notion](https://notion.so) account with an integration created

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/autotask-agent.git
cd autotask-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Fireworks AI
FIREWORKS_API_KEY=your_fireworks_api_key

# Google (OAuth)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# Notion
NOTION_TOKEN=your_notion_integration_token
NOTION_DATABASE_ID=your_notion_database_id
```

### 5. Set Up Google OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project → Enable **Gmail API** and **Google Calendar API**
3. Create **OAuth 2.0 credentials** → Download as `credentials.json`
4. Place `credentials.json` in the project root
5. On first run, a browser window will open for you to authorize access

### 6. Set Up Notion

1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Create a new integration → Copy the token
3. In your Notion workspace, create a Tasks database
4. Share the database with your integration
5. Copy the database ID from the URL

### 7. Run the App

```bash
streamlit run ui/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💬 Usage Examples

Once running, type natural language goals into the chat:

```
"What are my unread emails from today?"
"Create a task in Notion: Review project proposal — high priority"
"Schedule a team sync tomorrow at 3pm for 1 hour"
"Send a quick reply to Sarah's email saying I'll call her tomorrow"
"Summarize the last 5 emails in my inbox"
```

---

## 🔧 How the Custom Tools Work

Each tool is a Python function decorated with LangChain's `@tool` decorator. The agent reads the function's docstring to understand when and how to use it.

```python
@tool
def create_calendar_event(title: str, date: str, duration_minutes: int) -> str:
    """Creates a Google Calendar event. Use when the user wants to schedule something."""
    # calls Google Calendar API
    ...
```

The agent autonomously decides which tools to call based on the user's goal — no hardcoded logic.

---

## 🗺️ Roadmap

- [ ] Long-term vector memory with ChromaDB (remember user preferences across sessions)
- [ ] Human-in-the-loop confirmation before sending emails
- [ ] LangGraph migration for more complex multi-step workflows
- [ ] Email thread summarization
- [ ] Slack integration

---

## 🧠 Key Concepts Demonstrated

- **Agentic AI** — LLM autonomously plans and executes multi-step tasks
- **Tool Use** — Agent selects and calls real-world APIs as tools
- **ReAct Pattern** — Reason → Act → Observe loop
- **Multi-LLM Architecture** — Different models for different tasks (agent vs. summarizer)
- **Prompt Engineering** — Structured system prompts for consistent agent behavior
- **OAuth 2.0** — Secure Google API authentication
- **Pydantic Schemas** — Structured, typed data throughout the pipeline

---

## 📄 License

MIT License — feel free to use this as a template for your own agent projects.

---

## 🙋 Author

Built as a portfolio project to demonstrate agentic AI architecture using LangChain and Fireworks AI.# autotask-agent
