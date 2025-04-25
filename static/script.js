function sendMessage() {
    const input = document.getElementById("user-input");
    const chatlog = document.getElementById("chatlog");

    const message = input.value.trim();
    if (!message) return;

    chatlog.innerHTML += `<div class="user">You: ${message}</div>`;
    input.value = "";

    fetch("/get", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        chatlog.innerHTML += `<div class="bot">Bot: ${data.response}</div>`;
        chatlog.scrollTop = chatlog.scrollHeight;
    });
}
