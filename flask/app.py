from flask import Flask, render_template, request

app = Flask(__name__)

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
