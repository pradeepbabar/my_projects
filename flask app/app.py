from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def exam():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        # Get the form data
        name = session['user']['name']
        # Get the radio button value
        radio_value = request.form['radio']
        # Get the checkbox values
        checkbox_values = request.form.getlist('checkbox')
        # Get the textarea value
        textarea_value = request.form['textarea']
        # Save the result to a text file
        with open('result.txt', 'a') as f:
            f.write(f'{name},{radio_value},{checkbox_values},{textarea_value}\n')
        return 'Thank you for taking the exam!'
    return render_template('exam.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        # Check if the name and password are correct
        if name == 'your-full-name' and password == 'your-password':
            # Create a dictionary of user data
            user = {'name': name}
            session['user'] = user
            return redirect(url_for('exam'))
        else:
            error = 'Invalid full name or password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
