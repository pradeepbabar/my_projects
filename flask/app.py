from flask import Flask, render_template, request

app = Flask(__name__)


# Define the list of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest continent?",
        "options": ["Africa", "Asia", "Europe", "South America"],
        "answer": "Asia"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Dollar", "Euro", "Yen", "Pound"],
        "answer": "Yen"
    }
]

@app.route("/")
def quiz():
    return render_template("quiz.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    for q in questions:
        if request.form.get(q["question"]) == q["answer"]:
            score += 1
    return f"You scored {score}/{len(questions)}"

if __name__ == "__main__":
    app.run(debug=True)















'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def oddeven():
    name = request.form['name']
    num = request.form['num']
    x = num

    if x % 2 == 0:
        print('number is even')
    else:
        print('number is odd')

    return render_template('oddeven.html', name=name, num=x)


if __name__ == '__main__':
    app.run(debug=True)

'''