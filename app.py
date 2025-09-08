from flask import Flask, request, jsonify, render_template, session
import random

# Initialize the Flask application
app = Flask(__name__)
# A secret key is needed for session management
app.secret_key = 'super-secret-key-for-guessing-game'

@app.route('/')
def index():
    """
    This function serves the main HTML page.
    """
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    """
    Starts a new game by generating a secret number and resetting attempts.
    The number and attempts are stored in the user's session.
    """
    session['secret_number'] = random.randint(1, 100)
    session['attempts'] = 10
    print(f"New game started. Secret number is {session['secret_number']}") # For debugging
    return jsonify({
        'message': 'New game started!',
        'attempts': session['attempts']
    })

@app.route('/guess', methods=['POST'])
def handle_guess():
    """
    Handles a user's guess. It compares the guess to the secret number
    stored in the session and returns feedback.
    """
    # Check if a game is in progress
    if 'secret_number' not in session:
        return jsonify({'error': 'Game not started. Please start a new game.'}), 400

    # Get the user's guess from the incoming JSON request
    data = request.get_json()
    guess = data.get('guess')

    # --- Input Validation ---
    if guess is None:
        return jsonify({'error': 'No guess provided.'}), 400
    
    try:
        guess = int(guess)
        if not (1 <= guess <= 100):
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({'message': 'Please enter a number from 1 to 100!', 'feedback': 'invalid'}), 400

    # --- Process the Guess ---
    session['attempts'] -= 1
    secret_number = session['secret_number']
    
    feedback = ''
    message = ''

    if guess < secret_number:
        feedback = 'low'
        message = f"Too low! Try a little higher. ⬆️"
    elif guess > secret_number:
        feedback = 'high'
        message = f"Too high! Try a little lower. ⬇️"
    else:
        feedback = 'correct'
        message = f"You got it! The number was {secret_number}! 🎉"
        # Clear session to end the game
        session.pop('secret_number', None)

    # Check for game over
    if feedback != 'correct' and session['attempts'] <= 0:
        feedback = 'gameOver'
        message = f"Game over! The number was {secret_number}."
        # Clear session to end the game
        session.pop('secret_number', None)

    return jsonify({
        'message': message,
        'feedback': feedback,
        'attempts': session.get('attempts', 0)
    })

if __name__ == '__main__':
    # Runs the Flask app
    app.run(debug=True)
