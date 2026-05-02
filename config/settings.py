{
  "app": {
    "name": "AutoTask Agent",
    "version": "1.0.0",
    "debug": True
  },

  "llm": {
    "provider": "fireworks",
    "model": "kimi-k2-6",
    "temperature": 0.3,
    "max_tokens": 2048
  },

  "memory": {
    "type": "buffer",
    "max_messages": 20
  },

  "tools": {
    "notion": True,
    "gmail": True,
    "calendar": True
  },

  "streamlit": {
    "page_title": "AutoTask Agent",
    "layout": "centered",
    "sidebar_state": "expanded"
  }
}