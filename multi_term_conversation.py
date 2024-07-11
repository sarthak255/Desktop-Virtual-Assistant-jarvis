import openai

# Function to maintain multi-term conversation using OpenAI API
def multi_term_conversation(context, user_input):
    prompt = f"{context}\nUser: {user_input}\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Test the multi-term conversation function
if __name__ == "__main__":
    context = "The user is asking about the weather."
    user_input = "What is the weather like today?"
    response = multi_term_conversation(context, user_input)
    print(f"Response: {response}")
