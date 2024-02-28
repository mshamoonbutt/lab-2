import random

def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questions.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid input! Please choose from 'easy', 'medium', or 'hard'.")
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    return difficulty

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None
    """
    if not leaderboard:
        print("Leaderboard is empty.")
    else:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        print("Leaderboard:")
        for idx, (player, score) in enumerate(sorted_leaderboard, 1):
            print(f"{idx}. {player}: {score}")

def save_score(player_name, score, file_path='scores.txt'):
    """
    Saves the player's score to a file.

    Parameters:
    - player_name (str): The name of the player.
    - score (int): The score achieved by the player.
    - file_path (str): The file path to save the score.

    Returns: None
    """
    with open(file_path, 'a') as file:
        file.write(f"{player_name}: {score}\n")

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    leaderboard = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                player, score = line.strip().split(':')
                leaderboard[player] = int(score)
    except FileNotFoundError:
        print("Leaderboard file not found. Creating a new one...")
    return leaderboard

def provide_feedback(is_correct):
    """
    Provides feedback to the player after each round.

    Parameters:
    - is_correct (bool): Indicates whether the player's answer was correct.

    Returns: None

    Example:
    - is it correct?   "Well done!"
    - is it incorrect? "Sorry, that's incorrect."
    """
    if is_correct:
        print("Well done!")
    else:
        print("Sorry, that's incorrect.")

def fifty_fifty_lifeline(correct_answer, options):
    """
    Provides a 50/50 lifeline by removing two incorrect answers, leaving the correct answer and one other incorrect answer.

    Parameters:
    - correct_answer (str): The correct answer to the current question.
    - options (list): A list containing all possible answers including the correct answer.

    Returns:
    - list: A reduced list of answers containing only the correct answer and one randomly selected incorrect answer.

    This function is designed to be used once per game session by a player who chooses to use the 50/50 lifeline. It randomly selects one incorrect answer to keep along with the correct answer and removes the other options.
    """
    incorrect_options = [opt for opt in options if opt != correct_answer]
    random.shuffle(incorrect_options)
    return [correct_answer, incorrect_options[0]]

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    if allowed_skips > 0:
        print("You have chosen to skip this question.")
        return True
    else:
        print("You have no more skips available.")
        return False
