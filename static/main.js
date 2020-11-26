const error = document.getElementById("error");

function setError(message) {
    error.innerText = message;
    setTimeout(() => {
        error.innerText = "";
    }, 5000)
}