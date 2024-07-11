import openai

# Function to generate content-aware response using OpenAI API
def generate_content_aware_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Test the content aware response function
if __name__ == "__main__":
    prompt = "What is the weather like today?"
    response = generate_content_aware_response(prompt)
    print(f"Response: {response}")
