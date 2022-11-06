from flask import Flask
from dotenv import load_dotenv, find_dotenv

# === PURPOSE: getting time =======
from datetime import datetime

# === get necessaries from Flask ==========
from flask import render_template, jsonify, request

app = Flask(__name__)


# === SHOW screen from index ===============
@app.route("/", methods=['GET', 'POST'])
# PURPOSE: to show content in the URL: '/', which also means 'localhost:5000' as defaut
def show_screen():
    # PURPOSE: the frontend/UI application would be 'html' file
    # 'render_template': use the file as the UI/frontend of the app
    return render_template('index.html')


@app.route("/chat/<room>", methods=['GET', 'POST'])
# PURPOSE: to show content in the URL: '/', which also means 'localhost:5000' as defaut
def show_screen1(room):
    # PURPOSE: the frontend/UI application would be 'html' file
    # 'render_template': use the file as the UI/frontend of the app
    return render_template('index.html')


# === GET full message from room ===============
@app.route("/<room>", methods=['GET', 'POST'])
# PURPOSE: to show content in the URL: '/<room>', which also means 'localhost:5000/<room>'
# NOTE: <room> is any given number
def get_message(room):
    # PURPOSE: the frontend/UI application would be 'html' file
    # 'render_template': use the file as the UI/frontend of the app
    return render_template('index.html')


# === GET and POST messages ===========================
# PURPOSE: to show content in the URL: '/api/chat/<room>', which also means 'localhost:5000/api/chat/<room>'
# and collecting data from database or form
@app.route("/api/chat/<room>", methods=['GET', 'POST'])
def get_chat(room):
    # test with 'no comments' or '' string
    content = ''
    html_string = ''

    # create the link
    database_link = 'database/' + room + '.txt'

    # adding time state
    current_time_str = str(datetime.utcnow().strftime("[%Y-%m-%d %H:%M:%S] "))

    # if the database is not exist, create one
    with open(database_link, 'a') as fwrite:
        fwrite.write(content)
    fwrite.close()

    # read the txt file
    with open(database_link, 'r') as fread:
        html_string = fread.read()

    # read info from the 'form', by POST request
    if request.method == 'POST':
        name = request.form['username']
        mess = request.form['message']
        input_string = current_time_str + name + ': ' + mess + '\n'

        # append the message
        with open(database_link, 'a') as fappend:
            fappend.write(input_string)
            fappend.close()

    fread.close()
    # PURPOSE: always return the message from txt file
    return f"{html_string}"

    # 'jsonify': print the content as a JSON format
    # return jsonify(content)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='localhost')