#---------------------------------------
#  User Experience
#    Student C
#---------------------------------------


#---------------------------------------

def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questionsThe user is going to input their choice.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    #------------------------
    # Add your code here
    #------------------------
    print("Choose difficulty level:")
    print("Easy")
    print("Medium")
    print("Hard")
    
    difficulty=input("Enter your difficulty level:")
    while True:
        choice = input("Enter your choice (easy/medium/hard): ")
        if choice in ['easy', 'medium', 'hard']:
            return choice
        else:
            print("Invalid choice. Please enter")

    #------------------------
choose_difficulty()
#---------------------------------------

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None

    The function sorts the leaderboard by scores in descending order and prints the names and scores of the top players. If the leaderboard is empty, it prints a message indicating that there are no scores to display.
    """
    #------------------------
    # Add your code here
    #------------------------
     if not leaderboard:
        print("No scores to display.")
        return

    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

    print("Leaderboard:")
    print("{:<15} {:<10}".format("Player", "Score"))
    print("-" * 25)

    for player, score in sorted_leaderboard[:10]:
        print("{:<15} {:<10}".format(player, score))

    # Example Usage:
    leaderboard = {"Player1": 100, "Player2": 85, "Player3": 120, "Player4": 95}
    display_leaderboard(leaderboard)

    #------------------------

#---------------------------------------

def save_score(player_name, score, file_path='scores.txt'):
    """
    Saves the player's score to a file.

    Parameters:
    - player_name (str): The name of the player.
    - score (int): The score achieved by the player.
    - file_path (str): The file path to save the score.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
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
        file.write(f"{player_name},{score}\n")

def display_leaderboard(file_path='scores.txt'):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns: None
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No scores to display.")
                return

            # Parse scores from file
            leaderboard = {}
            for line in lines:
                player, score = line.strip().split(',')
                leaderboard[player] = int(score)

            # Display leaderboard
            sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
            print("Leaderboard:")
            print("{:<15} {:<10}".format("Player", "Score"))
            print("-" * 25)
            for player, score in sorted_leaderboard[:10]:
                print("{:<15} {:<10}".format(player, score))

    except FileNotFoundError:
        print(f"File '{file_path}' not found. No scores to display.")

def game():
    player_name = input("Enter your name: ")
    difficulty = choose_difficulty()

    # Play the game and calculate the score (sample logic)
    # For demonstration purposes, let's assume the player's score is 100
    score = 100

    # Save the score
    save_score(player_name, score)

    # Display the leaderboard
    display_leaderboard()

# Example usage
game()

    #------------------------

#---------------------------------------

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    #------------------------
    # Add your code here
    #------------------------
     try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            leaderboard = {}
            for line in lines:
                player, score = line.strip().split(',')
                leaderboard[player] = int(score)
            return leaderboard

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Returning an empty leaderboard.")
        return {}
    #------------------------

#---------------------------------------

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
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

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
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------



