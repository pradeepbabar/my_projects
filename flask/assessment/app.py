from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.permanent_session_lifetime = timedelta(minutes=2)

# Define the list of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "answer": "4"
    },
    {
        "question": "Write a function to return the sum of two numbers",
        "answer": "def add_numbers(a, b):\n    return a + b"
    }
]

# Define the index route
@app.route('/')
def index():
    session['question_index'] = 0
    session['start_time'] = datetime.now()
    session['end_time'] = session['start_time'] + timedelta(minutes=2)
    return redirect(url_for('question'))






# Define the question route
@app.route('/question/<int:question_index>', methods=['GET', 'POST'])
def question(question_index):
    # Ensure that expire_time key exists in session
    if 'expire_time' not in session:
        return redirect(url_for('index'))

    # Get the current time in UTC timezone
    now = datetime.utcnow()

    # Calculate the time left for the current question
    time_left = (session['expire_time'] - now).seconds

    # Ensure that the user has not run out of time
    if time_left < 0:
        return redirect(url_for('result'))

    # Get the current question
    question = questions[question_index]

    # Process the user's answer to the current question
    if request.method == 'POST':
        answer = request.form['answer']
        session['score'] += question.check_answer(answer)
        if question_index == len(questions) - 1:
            return redirect(url_for('result'))
        else:
            # Pass in question_index argument to url_for function
            return redirect(url_for('question', question_index=question_index+1))

    # Render the question template
    return render_template('question.html', question_index=question_index, question=question, time_left=time_left)



# Define the result route
@app.route('/result')
def result():
    score = session['score']
    total_questions = len(questions)
    time_taken = datetime.now() - session['start_time']
    session.pop('question_index', None)
    session.pop('score', None)
    session.pop('start_time', None)
    session.pop('end_time', None)
    return render_template('result.html', score=score, total_questions=total_questions, time_taken=time_taken)




if __name__ == '__main__':
    app.run(debug=True)
