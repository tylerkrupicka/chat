const error = document.getElementById("error");

function setError(message) {
    error.innerText = message;
    setTimeout(() => {
        error.innerText = "";
    }, 5000)
}

function navigate(path) {
    window.location.href = path;
}

function saveUsername(username) {
    sessionStorage.setItem('username', username);
}

function getUsername() {
    return sessionStorage.getItem('username');
}

function addMessage(username, message) {
    const messages = document.getElementById("messages");
    // Create list item
    const li = document.createElement("li");
    li.classList.add("message")
    if (username === getUsername()) {
        li.classList.add("mine"); // We sent this message
    }
    // Create name div
    const name = document.createElement("div");
    name.classList.add("name")
    name.innerText = username;
    // Create text div
    const text = document.createElement("div");
    text.classList.add("text");
    text.innerText = message;
    // Compose
    li.appendChild(name);
    li.appendChild(text);
    messages.appendChild(li)
}

function getMessagesCount() {
    const messages_container = document.getElementById("messages");
    const messages = Array.from(messages_container.querySelectorAll("li"));
    return messages.length;
}