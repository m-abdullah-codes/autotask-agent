from agent.agent import executor
from agent.memory import memory

def main():
    print("AutoTask Agent Initialized!")
    print("Type 'quit' or 'exit' to stop the program.\n")
    print("-" * 50)

    # The infinite conversation loop
    while True:
        try:
            # 1. Get user input
            user_input = input("\nYou: ")
            
            # 2. Check for exit commands
            if user_input.lower() in ['quit', 'exit']:
                print("\nShutting down AutoTask. Goodbye!")
                break
                
            # Skip empty inputs
            if not user_input.strip():
                continue

            print("---------------------------------------------")
            print(memory.load_memory_variables({}))  # Debug: Print current memory state
            print("---------------------------------------------")

            # 3. Pass the input to the agent
            # We pass it as a dictionary where the key "input" matches our prompt template
            print("\nThinking...")
            result = executor.invoke({"input": user_input})
            
            final_output = result['output']
            # Cleaning think tags if they exist
            if "</think>" in final_output:
                final_output = final_output.split("</think>")[-1].strip()
            
            print(f"\nAgent: {final_output}")
            print("-" * 50)

        except KeyboardInterrupt:
            # This cleanly handles if you press Ctrl+C to force quit
            print("\n\nForce quitting. Goodbye!")
            break
        except Exception as e:
            # If a tool crashes or the API fails, it catches the error so the whole loop doesn't die
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()