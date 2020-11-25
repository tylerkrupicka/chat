# Me Chat

> Building a simple chat website using Python!

This tutorial will go through the steps to build a simple but functional chat application. Most of the project will be done in Python, but there will be a little bit of HTML and JavaScript used to build the page the user sees.

## Background

In this project we will be building a website using the [Flask](https://flask.palletsprojects.com/en/1.1.x/) "micro" web-server project. If you have never built a website before, this may be a little confusing to start. In this section, I'll try to cover the basics of how our project is going to work. If you already have some understanding of websites, you can skip this section and just jump in to the project.

### Pieces of a Web Site

There are many different ways to build a website, but _in general_ there are a couple major pieces you need to make a full web application: a web page, and a web server.

#### Web Pages

Web pages are what a user actually sees and interacts with in their browser (Chrome, FireFox, etc). Just like Microsoft Word can open a `.doc` file, web browsers can open and display `.html` files that determine how the page looks. In addition, pages can include `.js` (JavaScript) files to make the page interactive and `.css` (Cascading Style Sheets) files to add colors and layout to the page.

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): The content of the page, including all of the text and the basic layout. A basic HTML file looks like the following:

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

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): Code that you can run in your page to make it interactive. There's _a lot_ that you can do with JavaScript, but for this exercise we'll be focusing on the basics: event handlers and requests. In the following example, we'll make the button from the HTML example print a message when clicked.

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

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Allows you to change the appearance of your page. By default, buttons are gray with square corners. If you would like to make the buttons blue with rounded corners, CSS is how you would do it. In this project all of the CSS will be supplied, but you can always change it!

```css
button {
    background-color: blue;
    color: white;
    border-radius: 4px;
}
```

#### Web Servers

A web server, in its most basic form, is a program that can send or receive [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) 'requests'. In this project we'll be using `Flask` to make our web server in Python. I'll cover some of the basic concepts below.

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



