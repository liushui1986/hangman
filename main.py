from flask import Flask, render_template, request, redirect, url_for, session
import random
from hangman_words import word_list
from hangman_art import logo, stages

app = Flask(__name__)
app.secret_key = 'hangman_secret_key'

@app.route('/')
def index():
    session.clear()
    session['lives'] = 6
    session['chosen_word'] = random.choice(word_list)
    session['placeholder'] = '_' * len(session['chosen_word'])
    session['correct_letters'] = []
    return render_template('index.html', logo=logo, placeholder=session['placeholder'], stages=stages[session['lives']])

@app.route('/guess', methods=['POST'])
def guess():
    if 'chosen_word' not in session:
        return redirect(url_for('index'))
    
    guess = request.form['guess'].lower()
    chosen_word = session['chosen_word']
    lives = session['lives']
    correct_letters = session['correct_letters']
    placeholder = list(session['placeholder'])

    if guess in correct_letters or guess in placeholder:
        return render_template('index.html', logo=logo, placeholder=' '.join(placeholder), stages=stages[lives], message=f'You already guessed "{guess}".')

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                placeholder[i] = guess
        session['placeholder'] = ''.join(placeholder)
        if '_' not in session['placeholder']:
            return render_template('index.html', logo=logo, placeholder=' '.join(placeholder), stages=stages[lives], message='Congratulations! You won!')
    else:
        lives -= 1
        session['lives'] = lives
        if lives == 0:
            return render_template('index.html', logo=logo, placeholder=' '.join(placeholder), stages=stages[lives], message=f'Game Over! The correct word was "{chosen_word}".')

    return render_template('index.html', logo=logo, placeholder=' '.join(placeholder), stages=stages[lives])

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
