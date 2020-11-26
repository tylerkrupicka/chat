from flask import Flask, render_template, request, jsonify

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    # Name of directory for static files (JS/CSS/Images)
    static_folder='static'
)


@app.route('/')
def new_user_page():
    """
    When a user visits our site, we need to collect their name.
    This route just renders the "new_user.html" file as the homepage.
    """
    return "Hello, Flask!"


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(
        host='0.0.0.0'  # Needed for Repl It
    )
