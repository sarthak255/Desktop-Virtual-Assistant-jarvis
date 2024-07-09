# src/study_helper.py
import openai

# OpenAI API key (replace with your actual key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to get answers from ChatGPT
def get_study_help(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Test the study helper function
if __name__ == "__main__":
    question = "Explain the theory of relativity."
    answer = get_study_help(question)
    print(f"Answer: {answer}")
