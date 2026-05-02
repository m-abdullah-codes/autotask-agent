import os
from dotenv import load_dotenv
from langchain_fireworks import ChatFireworks
from langchain.tools import tool

# Load environment variables (FIREWORKS_API_KEY)
load_dotenv()

@tool
def summarize_text(text: str) -> str:
    """Summarizes a given piece of text. Useful for condensing long emails or articles."""
    
    # Initialize the Fireworks LLM. We are using Llama 3.1 8B because it's insanely fast and great at summarizing.
    # accounts/fireworks/models/llama-v3-8b
    llm = ChatFireworks(
        model="accounts/fireworks/models/qwen3-8b",
        temperature=0.3 # Low temperature so the summary is factual, not creative
    )
    
    # Prompt the LLM
    response = llm.invoke(f"Please provide a very brief, 1-2 sentence summary of the following text:\n\n{text}")

    # --- CLEANING LOGIC ---
    # If the model uses <think> tags, we strip them out
    if "</think>" in response.content:
        response.content = response.content.split("</think>")[-1].strip()
    
    return response.content

# --- STANDALONE TESTING ---
if __name__ == "__main__":
    print("🧠 Initializing Summarizer Tool...")
    
    # A dummy email to test our tool
    sample_long_email = """
    Hi team, I just wanted to give you a quick update on the Q3 marketing campaign. 
    We've decided to pivot slightly away from Facebook ads and double down on LinkedIn, 
    as our B2B engagement there has been 3x higher. The budget will remain the same at $10k, 
    but marketing will be entirely focused on the enterprise sector. Please let me know 
    if you have any questions before the all-hands meeting on Thursday.
    """
    
    print("\n📝 Original Text Length:", len(sample_long_email), "characters")
    print("⏳ Generating summary using Fireworks AI...\n")
    
    try:
        # We invoke the tool with a dictionary matching the 'text' argument
        result = summarize_text.invoke({"text": sample_long_email})
        print("✅ SUMMARY:")
        print("-" * 50)
        print(result)
        print("-" * 50)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Did you forget to add FIREWORKS_API_KEY to your .env file?")