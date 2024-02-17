from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['password']
        correct_password = "bestfriendpannagapunganiggahappybirthday"
        
        if user_input == correct_password:
            return render_template('success.html')
        else:
            return render_template('failure.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
