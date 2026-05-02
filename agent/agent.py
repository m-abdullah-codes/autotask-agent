import os
from dotenv import load_dotenv
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_fireworks import ChatFireworks

# Import the pieces we just built!
from agent.prompts import SYSTEM_PROMPT
from agent.memory import memory

# Import your tools 
from tools.notion_tool import create_notion_task
from tools.calendar_tool import create_calendar_event
from tools.summarizer_tool import summarize_text
from tools.gmail_tool import get_gmail_tools 

load_dotenv()

# 1. Initialize the LLM
llm = ChatFireworks(
    model="accounts/fireworks/models/minimax-m2p5",
    temperature=0.1 
)

# 2. Bundle the tools
# First, call your function to get the list of Gmail tools
gmail_tools_list = get_gmail_tools()

# Next, combine your individual tools with the Gmail list using the '+' operator
tools = [create_notion_task, create_calendar_event, summarize_text] + gmail_tools_list

# 3. Construct the perfect Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# 4. Create the Agent
agent = create_tool_calling_agent(llm, tools, prompt)

# 5. Create the Executor
executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=memory, 
    verbose=True,
)