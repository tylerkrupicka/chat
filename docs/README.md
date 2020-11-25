# Me Chat

> Building a simple chat website using Python!

This tutorial will go through the steps to build a simple but functional chat application. Most of the project will be done in Python, but there will be a little bit of HTML and JavaScript used to build the page the user sees.

## Background

In this project we will be building a website using the [Flask](https://flask.palletsprojects.com/en/1.1.x/) "micro" web-server project. If you have never built a website before, this may be a little confusing to start. In this section, I'll try to cover the basics of how our project is going to work. If you already have some understanding of websites, you can skip this section and just jump in to the project.

There are many different ways to build a website, but _in general_ there are a couple major pieces you need to make a full web application: a web page, and a web server.

#### Web Pages

Web pages are what a user actually sees and interacts with in their browser (Chrome, FireFox, etc). Just like Microsoft Word can open a `.doc` file, web browsers can open and display `.html` files that determine how the page looks. In addition, pages can include `.js` (JavaScript) files to make the page interactive and `.css` (Cascading Style Sheets) files to add colors and layout to the page.

##### HTML

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

##### JavaScript

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

##### CSS

[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) allows you to change the appearance of your page. By default, buttons are gray with square corners. If you would like to make the buttons blue with rounded corners, CSS is how you would do it. In this project all of the CSS will be supplied, but you can always change it!

```css
button {
    background-color: blue;
    color: white;
    border-radius: 4px;
}
```

#### Web Servers

A web server, in its most basic form, is a program that can send or receive [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) 'requests'. In this project we'll be using `Flask` to make our web server in Python. I'll cover some of the basic concepts below.

<p align="center">
  <img src="https://mdn.mozillademos.org/files/8659/web-server.svg" alt="Server diagram" width="400px"/>
</p>


##### Routing (URLs)

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

##### Returning HTML

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

##### Receiving Data

Just like our Flask app can return pages and data to the browser, pages can send our Flask app data. We'll create a URL that the page can send data to, and then get the information we were sent using `get_json()`. [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) is a data format very similar to a Python [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), and the `get_json` function will convert it in to a Python dictionary for us.

```py
@app.route('/send_json')
def send_json():
  # data = { "message": "hello server""}
  data = request.get_json()
  print(data["message"]) # We will see "hello server" printed
```

##### Sending Data

Similarly, we can send data to the page in the JSON format by converting our Python variables to JSON.

```py
@app.route('/get_json')
def get_json():
  data = {"message" : "hello page" }
  return jsonify(data)
```

##### Status Codes

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
