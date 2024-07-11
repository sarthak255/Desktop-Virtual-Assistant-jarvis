from trello import TrelloClient

# Initialize Trello client
def init_trello(api_key, api_secret, token, token_secret):
    client = TrelloClient(
        api_key=api_key,
        api_secret=api_secret,
        token=token,
        token_secret=token_secret
    )
    return client

# Function to create a new Trello board
def create_trello_board(client, board_name):
    return client.add_board(board_name)

# Function to add a card to a Trello list
def add_card_to_list(board, list_name, card_name, description):
    trello_list = next((lst for lst in board.all_lists() if lst.name == list_name), None)
    if trello_list:
        return trello_list.add_card(card_name, description)
    else:
        print("List not found.")

# Test the project management functions
if __name__ == "__main__":
    api_key = "your_trello_api_key"
    api_secret = "your_trello_api_secret"
    token = "your_trello_token"
    token_secret = "your_trello_token_secret"
    
    client = init_trello(api_key, api_secret, token, token_secret)
    board = create_trello_board(client, "New Project")
    add_card_to_list(board, "To Do", "Sample Task", "This is a sample task.")
