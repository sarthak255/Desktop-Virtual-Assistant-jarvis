# src/chatbot.py
# pip install chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize the chatbot
chatbot = ChatBot("JARVIS")
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train("chatterbot.corpus.english")

# Function to get a response from the chatbot
def get_chatbot_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Test the chatbot function
if __name__ == "__main__":
    user_input = "Hello, how are you?"
    response = get_chatbot_response(user_input)
    print(f"Chatbot response: {response}")
