from flask import Flask, render_template, request, jsonify, redirect
from replit import db

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Render my index.html template
# get messages from db, pass to page, display as list


@app.route('/feed',  methods=['GET'])
def home():
    messages = db["messages"]
    return render_template('index.html', messages=messages)

# Get the latest db value and add a new message


@app.route('/send', methods=['POST'])  # submitting data ('POST')
def send():
    message_data = request.get_json()  # gets the dictionary that is sent
    """
  message_data = { "usenamer": "tyler", "text": "hello"}
  """
    messages = db["messages"]  # gets previous messages
    messages.append(message_data)  # adds new messages
    db["messages"] = messages  # saves all the messages
    return jsonify(messages)  # turns python object into text


@app.route('/updatefeed', methods=['GET'])  # getting data
def updatefeed():
    amount = request.args.get("amount")
    amount = int(amount)
    messages = db["messages"]
    if len(messages) > amount:
        return jsonify(messages[amount:])
    else:
        return jsonify([])


@app.route('/', methods=['GET'])
def newuser():
    return render_template('new_user.html',)


@app.route('/new_user', methods=['POST'])
def new_user():
    username = request.form['name']
    users = db["users"]

    if (username in users):
        return "Already exists", 400
    users.append(username)
    db["users"] = users
    return redirect("/feed?username=" + username)


if __name__ == "__main__":  # Makes sure this is the main process

    try:  # will try (won't crash if error) to clean messages
        del db["messages"]
        del db["users"]
    finally:  # run whether or not try succeeded
        db["messages"] = []
        db["users"] = []

    app.run(
        host='0.0.0.0',
        port=3000
    )
