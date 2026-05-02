from langchain_classic.memory import ConversationBufferMemory

# Create the memory object
memory = ConversationBufferMemory(
    memory_key="chat_history",  # The variable name the prompt will use to inject past messages
    return_messages=True        # Returns history as a list of message objects (best for Chat models)
)