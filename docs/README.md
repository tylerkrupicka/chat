# Chat App Tutorial

> Building a simple chat website using Python!

This tutorial will go through the steps to build a simple but functional chat application. Most of the project will be done in Python, but there will be a little bit of HTML and JavaScript used to build the page the user sees.

## Background

In this project we will be building a website using the [Flask](https://flask.palletsprojects.com/en/1.1.x/) "micro" web-server project. If you have never built a website before, this may be a little confusing to start. In this section, I'll try to cover the basics of how our project is going to work. If you already have some understanding of websites, you can skip this section and just jump in to the project.

There are many different ways to build a website, but _in general_ there are a couple major pieces you need to make a full web application: a web page, and a web server.

### Web Pages

Web pages are what a user actually sees and interacts with in their browser (Chrome, FireFox, etc). Just like Microsoft Word can open a `.doc` file, web browsers can open and display `.html` files that determine how the page looks. In addition, pages can include `.js` (JavaScript) files to make the page interactive and `.css` (Cascading Style Sheets) files to add colors and layout to the page.

#### HTML

[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) is the content of the page, including all of the text and the basic layout. A basic HTML file looks like the following:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>The title that shows up in the tab</title>
    </head>
    <body>
        <p>A basic paragraph of text!</p>
        <button>Click me!</button>
    </body>
</html>
```

#### JavaScript

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)is code that you can run in your page to make it interactive. There's _a lot_ that you can do with JavaScript, but for this exercise we'll be focusing on the basics: event handlers and requests. In the following example, we'll make the button from the HTML example print a message when clicked.

```js
// The `document` variable gives you access to the current HTML page
// We are searching for a `button` on the page and setting it equal to a variable
const button = document.querySelector('button');

// Now we can run code when the button is clicked!
button.addEventListener('click', () => {
    // Console is how you print messages in JavaScript.
    // You can use console.warn or console.error to print colored messages as well
    console.log('Button was clicked!')
})
```

#### CSS

[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) allows you to change the appearance of your page. By default, buttons are gray with square corners. If you would like to make the buttons blue with rounded corners, CSS is how you would do it. In this project all of the CSS will be supplied, but you can always change it!

```css
button {
    background-color: blue;
    color: white;
    border-radius: 4px;
}
```

### Web Servers

A web server, in its most basic form, is a program that can send or receive [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) 'requests'. In this project we'll be using `Flask` to make our web server in Python. I'll cover some of the basic concepts below.

<p align="center">
  <img src="https://mdn.mozillademos.org/files/8659/web-server.svg" alt="Server diagram" width="400px"/>
</p>


#### Routing (URLs)

You are probably familiar with the "URLs" you use to reach popular websites. In a very basic web server, the different `/route/paths` are actually folders going to different HTML files. In our web server, we'll be using it to run different functions in our Python program. Here's a basic example:

```python
@app.route('/')
def home():
  return "I am the homepage!"

@app.route('/profile')
def home():
  return "I am profile page!"
```

A user navigating to `http://oursite.xyz/` would get the first message while `http://oursite.xyz/profile` would get the second one. If you want to learn more about URLs, I recommend the [MDN guide](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL).

#### Returning HTML

So we know how to return some text, but in the last section we showed how HTML files are the real content of a web page. How do we display those using Flask? It's pretty simple:

```py
@app.route('/')
def home():
  # index.html is a html file in our 'templates' folder
  return render_template("index.html") 
```

Our HTML file is called a "template", because we can add variables to it. Here's an example:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{{ page_title}}</title>
    </head>
</html>
```

```py
@app.route('/')
def home():
  # We can change the page title by passing a variable in Python
  return render_template("index.html", page_title="Home Page") 
```

#### Receiving Data

Just like our Flask app can return pages and data to the browser, pages can send our Flask app data. We'll create a URL that the page can send data to, and then get the information we were sent using `get_json()`. [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) is a data format very similar to a Python [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), and the `get_json` function will convert it in to a Python dictionary for us.

```py
@app.route('/send_json')
def send_json():
  # data = { "message": "hello server""}
  data = request.get_json()
  print(data["message"]) # We will see "hello server" printed
```

#### Sending Data

Similarly, we can send data to the page in the JSON format by converting our Python variables to JSON.

```py
@app.route('/get_json')
def get_json():
  data = {"message" : "hello page" }
  return jsonify(data)
```

#### Status Codes

Every time our server sends or receives some data, it adds a [status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to let the page know whether the action worked. You may be already familiar with status code `404`, which means you tried to go to a page that doesn't exist. There are a lot of different codes, but the most common are `200` (Success) and `400` (Bad Request). There's also some obscure ones like [418](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418) "I'm a teapot".

By default when we `return` anything Flask will send along a `200` response code to say it succeeded. What if it fails? The page could send us data in the wrong format, and we need to indicate that we didn't complete it.

```py
@app.route('/send_json')
def send_json():
  # We are expecting data = { "message": "hello server""}
  data = request.get_json()
  if ("message" not in data):
    # They did not add a message to their data
    return "Bad data", 400
  return "Good data" # 200 is automatic
```

## Getting Started

### Creating your Repl

For this tutorial, we will be using [Repl It](https://repl.it) to run our site. If you haven't already:

[Clone this REPL](https://repl.it/github/tylerkrupicka/chat)

When that is completed, you should have a new REPL with a directory structure like this:

```
main.py
templates/
static/
docs/
README.md
```

For this project, we will mostly be working in the `main.py` file and `templates/` folder.

### Running the REPL

To make sure everything works, click the `Run` button on the top of the screen. You should see the Flask application start, and open a webpage.

<p align="center">
  <img src="./images/initial_run.png" alt="First run hello world"/>
</p>

Congratulations! You have a working Flask website.

## New User Sign Up

We're building a chat application so the first thing we should do is make it possible to send messages, right? Well, not quite. We need to know who is sending each message, which means we need to make users create a `username` before joining the chat.

### Showing the New User Template

Navigate to the `main.py` file and look for the `new_user_page` function. It will look like this:

```py
@app.route('/')
def new_user_page():
```

Notice the `app.route` above the function. The `/` route is our homepage, which means a new user will see this page first when they go to our website.

To start, this function is just returning the text `Hello, Flask`. Can you update it to render the `new_user.html` template based on the Flask tutorial above?

After you make a change, you'll need to stop and start your program to get the latest updates. You may also need to hit the reload button on the website preview. When you have the template rendering it should look like this:

<p align="center">
  <img src="./images/new_user_page.png" alt="New user page"/>
</p>

### Sending a Username

Now we need to write some JavaScript to make the page work. When a user clicks the `Submit` button, we need to:

1. Get the text of the username they want to use.
2. Check that it is valid.
3. Send the username to our Flask app.
4. Check the response and either show an error, or sign them in.

Since this project is more about learning Python than JavaScript. A lot of this code will be provided.

Open the `templates/new_user.html` file and locate the `<script>` area near the bottom. This will be where we write our code.

```html
<script>
// Write your JavaScript here
</script>
```

#### Basic Structure

Add the following code to your script area:

```js
// Write your JavaScript here
const button = document.getElementById("submit-username");
const input = document.getElementById("username");

async function sendUsername() {
  // Get the username
  
  // Check if it is not empty

  // Send it to our Python program

  // Check the results
}

button.addEventListener("click", sendUsername);
```

Let's break down what that is doing. If you look in at the `<button>` higher up in the file, it has an `id` of `submit-username`. On the first line, we use that ID to get the button as a JavaScript variable. We do the same thing for the text input on the next line. Going forward, we can use these variables to find out what the user typed and when the click the button. 

On the next line, we create a function called `sendUsername` which will send the username.

On the final line, we add what is called an "event listener". For this example, we are saying "whenever `button` is `clicked`, run our `sendUsername` function.

#### The Send Function

##### Get the Input Value
Now let's fill out that send function. First, we need to get what the user has typed into the input. This can be done by getting the `value` of the `input`.

```js
// Get the username
const username = input.value;
```

> The `const` creates a new `constant` variable. This means the variable can not be changed. We could also declare it with `var` or `let` if we plan on changing it. You can [read more on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const).


##### Validate the Username

Next, we need to check and make sure they have typed a username before sending. This can be done like this:

```js
// Check if it is not empty
if (username.length === 0){
  setError("Username is empty");
  return;
}
```

A few notes:

- In JavaScript you get the length of a variable using `.length`.
- The `===` equals sign is not a typo, in JavaScript you use three equals signs for [strict equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality). 
- The `setError` function is not a standard JavaScript function. I have created it for you since it might be confusing. Tricky, right?
- The `return` stops our function from continuing. We do not need to bother sending an empty username.

##### Send the Username to Flask

Next, we need to send the username to our Flask application. We can send the data using the [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) function in JavaScript.


```js
// Send it to our Python program
const response = await fetch('/add_user', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({username: username})
});
```

Some notes:

- You can mostly ignore the [await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) before fetch. In JavaScript, you can have code that runs at the same time. This `await` just indicates that we want to wait for fetch to finish before continuing.
- Method `POST` is an [HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods). `POST` usually means we want to send data, while `GET` usually means we want to get data. Since we are sending the username, we want `POST`.
- The headers tell Flask that we are sending our username in `JSON` format. This was covered in the background section.
- The body is the data we are sending, and we send it as text. `JSON.stringify` is a function that lets us send JSON as text.

##### Get the Response

We now have a variable called `response`, which will contain the response from our Flask server. We can check this to see if there were any errors. Look back at the status codes section if you are unsure about how web servers send back an error.

With that response, we can see if the username was added and let the user know.

```js
  // Check the results
  if (response.status === 200) {
    // Username was added successfully
    // We can redirect to another page later
  } else if (response.status === 400) {
    setError("Username is taken")
  } else {
    setError("An error occurred")
  }
```

##### Try it out

If we try to submit a username now, we should see an error appear. (You may need to restart your project and reload the page to see the changes).

<p align="center">
  <img src="./images/new_user_error.png" alt="New user page"/>
</p>

Why is it an error?

Well, we haven't actually set up our Python program to have a `/new_user` route! We'll do that next.

### Add User Flask Route

#### Set up the Route

Back in `main.py` we need to add a `/new_user` route that gets the data we are sending from the page. If you remember, we're sending the data as `JSON` using a `POST` request. Here's how you would get that data using Flask:

```py
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    When a user clicks submit on the new user page,
    their username will be sent here as JSON.
    """
    data = request.get_json() # Get the data sent from the page
    print(data)
    return "Got it!"
```

If you restart your repl, and submit a new user, you should see the username now show up in the Python console!


<p align="center">
  <img src="./images/add_user_print.png" alt="Add user printed in console"/>
</p>

As you can see in the picture, we now have a Python dictionary with the username in it! We can get the username using:

```py
username = data['username']
```

#### Check if the username exists

Now we need to check if the username exists, and return a response to the page. How do we know what other usernames are taken? We need to keep track of all the usernames we have seen so far.

In Python, we can probably do this using a list:

```py
users = [] # Outside function

if username in users:
  return "Already exists", 400 # Send an error 400
else:
  users.append(username) # Add username to users
  return "OK"
```

> Note: You'll need to create the users array _outside_ of your `add_user` function. If you make it _inside_, a new users array will be created every time somebody clicks the submit button.

#### Try it out!

Now our sign up page should work! Try submitting a username; the first time you hit submit nothing will happen (we haven't done that logic yet), but the second time you should see that the username already exists!

<p align="center">
  <img src="./images/username_taken.png" alt="The username is taken"/>
</p>

## The Chat Page

### Set up the Route

We're finally done with usernames, let's make the chat page! We'll put it at the `/chat` route in our website:

```py
@app.route('/chat')
def chat_page():
    return render_template('chat.html')
```

Now we just need to change our JavaScript in `new_user.html` to redirect to the chat page after they create a username. I've created some helpful functions for you to make this easier.

```js
if (response.status === 200) {
  // Username was added successfully
  saveUsername(username); // Save the username so we can use it in chat
  navigate('/chat'); // Go to the chat page
}
```

Now you should be able to restart your program and enter a username. If it adds it successfully, you will be navigated to the `/chat` screen!

<p align="center">
  <img src="./images/chat_screen.png" alt="The chat screen"/>
</p>

### Sending a Message

We are now going to be writing some code in `chat.html`, so that we can send messages. This will hopefully look _very_ similar to the code for sending the username.

```js
// Write your JavaScript here
const input = document.getElementById("message-input");
const button = document.getElementById("send-button");

async function sendMessage() {
  // Get the message
  const message = input.value;
  // Check if it is not empty
  if (message.length === 0){
    setError("Message is empty");
    return;
  }
  // Send it to our Python program
  const response = await fetch('/send_message', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({username: getUsername(), message: message})
  });
  // Check the results
  if (response.status !== 200) {
    setError("An error occurred")
  } else {
    input.value = ""; // Clear the field if it sent
  }
}

button.addEventListener("click", sendMessage);
```

If any part of this seems confusing, look back at the `new_user.html` part of the tutorial. The only difference is we are sending JSON that looks like:

```json
{
  "username": "test",
  "message": "the text of the message"
}
```

### Send Message Flask Route

We now need a route in Flask to receive the message being sent! This will also be very similar to the route for adding a user.

```py
# In main.py
@app.route('/send_message', methods=['POST'])
def send_message():
    """
    When a user clicks submit on chat window,
    their message will be sent here in json.
    """
    data = request.get_json()
```

Try to do this next part on your own. I've provided an example below, where I've removed my code and replaced it with hint comments.

You'll need to:

- Create a list to store your messages.
- Check if the data has a username and a message.
- Save the message to the messages list.
- Return success.


```py
# Create the list to store messages

@app.route('/send_message', methods=['POST'])
def send_message():
  """
  When a user clicks submit on chat window,
  their message will be sent here in json.
  """
  # Get the JSON from the request

  # Check if "username" and "message" are included in the data
    # If they are, add it to our messages list
    # Return a 200 status
  # else
    # Return a error code 400
```

> If you are stuck, add some `print` statements. You can see what data is being sent from the page which will help you understand how it works.

If you have this working, you should be able to send a message from the page and see the text disappear when it sends successfully.

### Loading messages

You may have noticed a problem. Our chat site sends messages, but they never show on the screen! That's not very useful. So far all the work we have done on our chat page had been about sending messages, but we don't have any way to get them! Let's fix that.

In Python, we need to make a new route called `/messages` that returns our `messages` list in JSON form.

```py
# In main.py
@app.route('/messages')
def get_messages():
    return jsonify(messages)
```

Pretty simple! We take our array of messages and send it back as JSON. Now our JavaScript can load messages and show them.

Lets go back to `chat.html` and add a function to load the messages.

```js
// In chat.html
async function getMessages() {
  const response = await fetch('/messages');
  // Check the results
  if (response.status !== 200) {
    setError("Error loading messages.")
  } else {
    // Load the messages from JSON
    const messages = await response.json();
    // Loop over each message and add it to the screen
    messages.forEach(message => {
      addMessage(message.username, message.message)
    })
  }
}
```

> Note: `addMessage` is a function I have provided for you that shows the message on the page. It's a little complicated, but if you want to see how it works you can look in `main.js`.

OK, now we have a function to get messages, but when should we call it? Well, after we send a message we'd like to see it show up, right? We can call `getMessages` after we send a message, to make that work.

```js
// In the sendMessages function in chat.html
  if (response.status !== 200) {
    setError("An error occurred")
  } else {
    input.value = "";
    getMessages(); // Add this line to sendMessages
  }
```

> Note: In JavaScript, a function should be created before it can be called. Your `getMessages` function should  be before your `sendMessage` function so it exists before `sendMessage` references it.

Try it out! Now when you hit send, you should see your message appear. There's a problem though, right? Our `/messages` route returns _all_ messages every time, so every time we get messages we get them all. This will cause duplicate messages to be added!

<p align="center">
  <img src="./images/duplicate_messages.png" alt="The chat screen"/>
</p>

### Only Loading New Messages

We're going to have to make some changes to our `getMessages` code and `/messages` route to only get _new_ messages that we haven't seen.

For this we are going to use [URL parameters](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams). These are variables that we can add on to the end of a URL, and they are commonly used for uses like this. 

In our `getMessages` JavaScript function, we can add a URL parameter that tells our Python program how many messages we have seen already.

```js
// In chat.html
async function getMessages() {
  const current = getMessagesCount(); // I created the getMessagesCount function for you
  const response = await fetch(`/messages?current=${current}`);
```

For URL parameters, you add a `?`, and then set your variables. In this example we're creating a variable called `current` to tell Flask what the current message we see is. In other words, if we have seen 5 messages, we will ask our Python program for only messages after the fifth one.

In `main.py` we can change our `/messages` route to look for the `current` variable and only send new messages.

```py
@app.route('/messages')
def get_messages():
    if "amount" in request.args:
      amount = int(request.args["amount"]) # Convert it from text to number
      # Return from the amount index to the end of the list using list slicing
      return jsonify(messages[amount:])
    else:
      return jsonify(messages)
```

> Note: If you are new to Python you might not have seen the `[amount:]` syntax for splitting up the list. Here's a [guide](https://stackoverflow.com/questions/509211/understanding-slice-notation) if you want to learn more.

### Checking Periodically

So now we should no longer be seeing duplicate messages show up, but right now we are only checking for new messages when we send one. What if we get sent a message from someone else? There are a lot of ways we could make this work, but the simplest is a method called `polling`. Polling just means, check for new messages on a timer.

In JavaScript, we can run a function on a timer using [setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval). It takes two arguments, what function to run, and how much time to wait in between runs.

At the bottom of our script in `chat.html`, we can add:

```js
getMessages(); // Run when the page loads
setInterval(getMessages, 3000); // Run again every 3 seconds
```

This will check for new messages every 3 seconds (3000 milliseconds).

> Note: If this was a real product, polling would likely _not_ be the method to do this. Imagine if thousands of people were chatting at once, your Python application would be getting requests constantly checking for new messages. For this reason, there are specialized tools like [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) that can just send the page a new message when it arrives. For this small app, however, polling will work well.

### Try it out!

You should now be able to open multiple tabs of your chat site in your browser (Chrome or FireFox), and message between them! New messages will arrive after at most 3 seconds.

> The URL for your app can be found at the top of your preview window in Repl it. It will look like https://chat.yourusername.repl.co.

<p align="center">
  <img src="./images/working_chat.png" alt="The chat screen"/>
</p>

You can also open up this chat on your phone, or send it to friends to try out Congratulations, you've made a basic chat app!

## Enhancements

So far, this tutorial has provided a lot of code for you to illustrate a lot of the concepts. Now that you get the basics, you can modify and improve your chat application however you wish. In this section, I'll provide some example improvements that you can make to your app. 

### Add A Database

You may have noticed every time you stop and start our Python program, all of the users and messages disappear. Why is that?

When we create our users array:

```py
users = []
```

We are creating it as a variable that is part of our Python program. When Python quits, that data is lost like any other Python program. So how do websites store data? You may have guessed from the title: [databases](https://developer.mozilla.org/en-US/docs/Glossary/Database).

Databases can be a lot of things, from a simple file that is saved, to complicated programs that can store millions of entries easily. On Repl It, they have a simple "key value" database

```py
from replit import db
db["key"] = "value"
```

Try setting this up for your `messages` and `users`, and you'll see that they stay even after you restart the server!

If you need more documentation, click the database icon on the left of Repl it (it looks like a cylinder).

### Add Timestamps

### Send on Enter

### Better User Accounts

### Change the appearance

### Make messages disappear

### Try WebSockets