from trello import TrelloClient

from dotenv import load_dotenv
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

board_name = "未タイトル"
list_name = "To Do"

load_dotenv()


def load_env() -> (str, str):
    key = os.environ.get("TRELLO_API_KEY")
    token = os.environ.get("TRELLO_API_TOKEN")
    return key, token

def get_task_lists_from_file(file_path: str) -> list:
    with open(file_path, "r") as f:
        return f.readlines()


def main():
    global client
    print("Hello from trello-uploader!")
    env = load_env()
    if env[0] == "" or env[1] == "None":
        print("Please set environment variables")
        return
    client = TrelloClient(env[0], token=env[1])
    all_boards = client.list_boards()


    # Find target board
    target_board = None
    for board in all_boards:
        if board.name == board_name:
            target_board = board
            print("Board found: " + board.id)
            break
    else:
        print("Board not found")
        return

    # Get all tasks from file
    tasks = get_task_lists_from_file("tasks.txt")
    # find target list
    target_list = None
    for list in target_board.list_lists():
        if list.name == list_name:
            target_list = list
            print("List found: " + list.id)
            break
    else:
        print("List not found")
        return
    # Add tasks to list
    for task in tasks:
        # Title, Description
        split_task = task.split(",")
        title = split_task[0]
        description = None
        if split_task[1:]:
            description = split_task[1]
        result = target_list.add_card(title,description)
        print("Added task: " + result.name + " (" + result.id +  ")" )



if __name__ == "__main__":
    main()
